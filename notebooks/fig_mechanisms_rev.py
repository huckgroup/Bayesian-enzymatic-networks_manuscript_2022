# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy.optimize as optimize
import scipy.integrate as integrate
import sympy as sp

from numba import njit

import ast

import pymc3 as pm
import arviz as az
import xarray as xr
import theano.tensor as tt

import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns; sns.set_theme(style='ticks', context='paper', font_scale=0.8);

from bayern import ops

# %%
experiments = pd.read_csv(f"../data/kinetic_studies.csv").query(
    f'enzyme == "G6PDH"'
)
data = []
for t in experiments.itertuples():
    df = pd.read_csv(f"../data/{t.data_path}")
    df = df.assign(
        kf=t.flowrate / (60 * t.volume),
        G6PDH=t.enzyme_concentration,
        code=t.experiment_code,
    )
    data.append(df)

data = pd.concat(data).reset_index(drop=True)

data = data.assign(
    NAD_obs=data.NAD_in - data.NADH_obs,
    G6P_obs=data.G6P_in - data.NADH_obs,
    G6PdL_obs=data.NADH_obs
)

data = data.groupby(['code', 'G6P_in', 'NAD_in']).mean().reset_index()


# %%
def compile_model(data):
    exp_idx, exp_coords = data.code.factorize(sort=True)
    # obs_idx, obs_coords = data.index.factorize(sort=True)
    coords = {"exp": exp_coords, 
                # 'obs': obs_coords
            }

    with pm.Model(coords=coords) as model:
        k_cat = pm.Uniform("k_cat", 0, 500)
        K_G6P = pm.Uniform("K_G6P", 1, 4000)
        K_NAD = pm.Uniform("K_NAD", 1, 2000)
        KI_NADH = pm.Uniform("KI_NADH", 1, 10000)

        sigma = pm.Exponential("sigma", 0.5, dims='exp')


        G6PDH = pm.Data("G6PDH", data.G6PDH.values)
        NADH = pm.Data("NADH_obs", data.NADH_obs.values)
        NAD = pm.Data("NAD_obs", data.NAD_obs.values)

        G6P = pm.Data("G6P_obs", data.G6P_obs.values)
        G6PdL = pm.Data("G6PdL_obs", data.G6PdL_obs.values)

        G6P_in = pm.Data("G6P_in", data.G6P_in.values)
        NAD_in = pm.Data("NAD_in", data.NAD_in.values)
        kf = pm.Data("kf", data.kf.values)

        NADH_obs = pm.Normal("NADH", 
                    mu = k_cat*G6PDH*G6P*NAD/(kf*K_G6P*K_NAD*(1 + G6P/K_G6P)*(1+NAD/K_NAD)*(1+ NADH/KI_NADH)),
                    sigma=sigma[exp_idx],
                    observed= NADH
                    )
    return model

def select_observations(data, idx):
    return data.drop(idx), data.iloc[idx]


# %%
class PyMC3LinRegWrapper(az.SamplingWrapper):
    def __init__(self, data, data_vars, model, **kwargs):
        self.data = data
        self.data_vars = data_vars

        __selected_data, _ = self.sel_observations([0]) # Pre-compile model with LOO corrected shape
        self.pymc3_model = model(__selected_data)
        
        super(PyMC3LinRegWrapper, self).__init__(model=model, **kwargs)

    def sample(self, modified_observed_data):
        with self.pymc3_model:
            pm.set_data(
                modified_observed_data[self.data_vars]
            )
            trace = pm.sample(
                **self.sample_kwargs, 
                idata_kwargs={"log_likelihood": False}
            )
        return trace
    
    def get_inference_data(self, trace):
        idata = az.from_pymc3(trace, model=self.pymc3_model, **self.idata_kwargs)
        idata.pymc3_trace = trace
        return idata
        
    def log_likelihood__i(self, excluded_observed_data, idata__i):
        with self.pymc3_model:
            pm.set_data(excluded_observed_data[self.data_vars])
        
        print(excluded_observed_data[self.data_vars])
        # model_ex = compile_linreg_model(**excluded_observed_data)
        log_lik__i = az.from_pymc3(idata__i.pymc3_trace, model=self.pymc3_model, log_likelihood=True).log_likelihood["y"]
        return log_lik__i
        
    def sel_observations(self, idx):
        return select_observations(self.data, idx)

# %%
sample_kwargs = {"draws": 1000, "tune": 1000, "chains": 4, 'target_accept': 0.92, 'progressbar': True, 'return_inferencedata': False}
with compile_model(data=data) as model:
    trace = pm.sample(**sample_kwargs)

# %%
idata = az.from_pymc3(trace, model=model)

loo_orig = az.loo(idata, pointwise=True)
print(loo_orig)

# %%
pymc3_wrapper = PyMC3LinRegWrapper(
    model=compile_model, data=data, 
    data_vars=['G6PDH','NADH_obs','NAD_obs','G6P_obs','G6PdL_obs','G6P_in','NAD_in','kf'],
    sample_kwargs=sample_kwargs, idata_kwargs=dict()
)

# %%
loo_relooed = az.reloo(pymc3_wrapper, loo_orig=loo_orig)

# %%
print(loo_relooed)

# %%
# exp_idx, exp_coords = data.code.factorize(sort=True)
# obs_idx, obs_coords = data.index.factorize(sort=True)
# coords = {"exp": exp_coords, 'obs': obs_coords}

# G6P, G6PdL, NAD, NADH = sym_x = sp.symbols("G6P, G6PdL, NAD, NADH")
# k_cat, K_G6P, K_NAD, KI_NADH = sym_phi = sp.symbols("k_cat, K_G6P, K_NAD, KI_NADH")
# G6PDH, G6P_in, NAD_in, kf = sym_theta = sp.symbols("G6PDH, G6P_in, NAD_in, kf")

# sym_rate = k_cat*G6PDH*G6P*NAD/(kf*K_G6P*K_NAD*(1 + G6P/K_G6P)*(1+NAD/K_NAD)*(1+ NADH/KI_NADH))
# sym_ode = [
#     -sym_rate + kf*(G6P_in - G6P),
#     sym_rate - kf*G6PdL,
#     -sym_rate + kf*(NAD_in - NAD),
#     sym_rate - kf*NADH,
# ]

# def generate_model(sym_x, sym_phi, sym_theta, sym_ode, data_set):
#     sym_jac_x = sp.Matrix(sym_ode).jacobian(sym_x)
#     sym_jac_phi = sp.Matrix(sym_ode).jacobian(sym_phi)
#     sym_jac_theta = sp.Matrix(sym_ode).jacobian(sym_theta)
#     t = sp.symbols('t')
#     num_rate_equations = njit(sp.lambdify([sym_x, sym_phi, sym_theta], sym_ode, "numpy"))
#     num_jac_x = njit(sp.lambdify([sym_x, sym_phi, sym_theta], sym_jac_x, "numpy"))
#     num_jac_phi = njit(sp.lambdify([sym_x, sym_phi, sym_theta], sym_jac_phi, "numpy"))
#     num_jac_theta = njit(sp.lambdify([sym_x, sym_phi, sym_theta], sym_jac_theta, "numpy"))

#     def find_root(fun, jac, phi, theta):
#         return optimize.root(fun=fun, x0=[theta[0],theta[1],0.0, theta[2]], jac=jac, args=(phi, theta)).x
#     num_grad_phi = njit(lambda x,phi,theta: np.dot(-np.linalg.inv(num_jac_x(x,phi,theta)),num_jac_phi(x,phi,theta)))
#     num_grad_theta = njit(lambda x,phi,theta: np.dot(-np.linalg.inv(num_jac_x(x,phi,theta)),num_jac_theta(x,phi,theta)))

#     def compile_model(xdata, ydata):
#         SteadyStateOp = ops.SteadyStateDatasetOp(num_rate_equations, num_jac_x, num_grad_phi, num_grad_theta, find_root, theta_set=xdata[sym_theta].values)

#         with pm.Model() as model:
#             x = pm.Data("x", xdata)
#             k_cat = pm.Uniform("k_cat", 0, 500)
#             K_G6P = pm.Uniform("K_G6P", 1, 4000)
#             K_NAD = pm.Uniform("K_NAD", 1, 2000)
#             KI_NADH = pm.Uniform("KI_NADH", 1, 10000)
#             sigma = pm.Exponential("sigma", 0.5, dims='exp')

#             y = pm.Normal("y", 
#                     mu=SteadyStateOp(tt.stack([k_cat, K_G6P, K_NAD, KI_NADH]))[:, 3], 
#                     sigma=sigma, 
#                     observed=ydata
#                 )
                
#         return model


