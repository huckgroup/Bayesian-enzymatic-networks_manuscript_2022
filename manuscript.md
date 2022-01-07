---
title:  'A Bayesian approach to understanding artificial enzymatic networks'
author:

- Mathieu G. Baltussen
- Jeroen van de Wiel
- Cristina Lía Fernández Regueiro
- Miglė Jakštaitė
- Wilhelm T.S. Huck

link-references: true
figPrefix:
    - "figure"
    - "figures"
citation-style: analytical-chemistry
link-citations: true
link-bibliography: true

...

# Summary/Abstract

In order to create artificial enzymatic networks capable of increasingly complex behavior, an improved methodology in understanding and controlling the kinetics of these networks is needed.
Here, we introduce a Bayesian analysis approach which allows for the accurate inference of enzyme kinetic parameters and determination of most likely reaction mechanisms, by combining data from different experiments and network topologies in a single probabilistic analysis framework.
This Bayesian approach explicitly allows us to continuously improve our parameter estimates and behavior predictions by iteratively adding new data to our models, while automatically taking into account uncertainties introduced by the experimental setups or the chemical processes in general.
We demonstrate the potential of this approach by characterizing systems of enzymes compartmentalized in beads inside flow reactors.
The approach we introduce here could be relevant to the design of artificial enzymatic networks, making the design of such networks more efficient, and robust against the accumulation of experimental errors.

<!-- **Additional talking points**
- Difference to ML: No black box, but can be used to improve understanding of underlying mechanisms and assumptions  -->

\newpage

# Introduction

Enzymatic reaction networks (ERN’s) play key roles in many cellular processes, such as energy metabolism, signaling pathways, and cell division[@Barabasi2004;@Kholodenko2006;@Boccaletti2006].
The fields of synthetic biology and systems chemistry aim to understand and reproduce the behavior of these ERNs in artificial systems[@Purnick2009;@Novak2008;@Ludlow2008;@Roekel2015;@Ashkenasy2017].
To construct functional ERNs, estimating the mechanisms and kinetics of the enzymatic reactions in these systems is essential in order to reliably predict the relevant experimental regimes in which a desired functional output will be observed[@Wong2017a].
But while the development of artificial ERNs with more complex behavior continues[@Semenov2015;@Maguire2020], methods are missing to not only obtain realistic kinetic parameter estimates, but to simultaneously allow for the evaluation of the relevance and correctness of existing kinetic models.
<!-- To understand how these ERNs produce complex behaviour, there have been many efforts to construct increasingly complex enzymatic networks from the bottom up[@Roekel2015].
Previous work has shown the implementation of network motifs[@Milo2002] by autocatalysis and delayed inhibition[@Semenov2015], photochemical control of oscillations by reversible photo-inhibitors[@Pogodaev2019], coupling to DNA-based circuits[@Meijer2017], and coupling to dynamic environments[@Maguire2020].
These enzymatic networks were designed to showcase a range of behaviours, such as robust oscillations[@Semenov2015;@Novak2008], logic-gate responses[@Ikeda2014], pattern-formation[@Zhang2018], and adaptive responses to environmental perturbations[@Helwig2018].
In recent efforts, we have developed a technique to immobilize enzymes on polyacrylamide beads (PEBs), which can be compartmentalized inside a flow reactor[@FernandezRegueiro2021].
The increased composability of this system should allow the development of more complex network topologies and behaviours.
While these advances have greatly increased the capabilities of artificial ERNs, the lack of accurate kinetic parameter estimates that can reliably predict the relevant experimental regimes in which a desired functional output will be observed, greatly limits the efficient exploration of more complex motifs.  -->
<!-- To design ERN’s and their associated complex behaviour, computational models are often used to estimate the kinetics and determine a suitable range of experimental parameters that showcase the wanted behavior. -->

This lack of accurate and experimentally realistic parameter and mechanism estimation greatly limits the efficient exploration of more complex systems.
Furthermore, while the fitting of a model to experimental data is in principle relatively simple, in practice numerous sources of uncertainty are encountered, including experimental errors and unknown inhibitory or allosteric effects.
Typically, the kinetic parameters of an enzymatic reaction are estimated from a single dataset, using least-squares regression or similar maximum likelihood estimation methods.
Although this approach is well-established, there are multiple downsides[@Efron2016].
First, sources of uncertainty must be explicitly modelled in, which would require an exact knowledge of the influence of these uncertainties on the final experimental results[@Gabor2017;@Lillacci2010].
Secondly, this approach often neglects additional sources of data, either from previous or additional experiments, or from literature.
And lastly, estimation of enzyme kinetics is often done using rather limited datasets, which should increase the uncertainty of the obtained parameter values, but in practice potentially leads to overfitting of the proposed model[@Wainer2007;@Silver2021].

To improve the kinetic analysis of enzymatic activity, we demonstrate an analysis framework based on Bayesian methods for the inference of kinetic parameters and comparison of reaction mechanisms of immobilized enzymes in a flow reactor.
Bayesian methods have been more widely implemented in recent years, mainly due to an increase in available computational power and an increase in general availability of powerful, yet accessible, algorithms.
They are used in a wide range of fields, from applications in pure physics[@Toussaint2011], medicine[@Ashby2006], and sociology[@Lynch2019], to large-scale metabolomics in systems biology[@St.John2019] and optimized peak detection in chromatographic methods[@VivoTruyols2012].

Our Bayesian approach is probabilistic in nature, so that any knowledge of kinetic parameters or reaction mechanisms obtained from experimental data is expressed in terms of probability-distributions, instead of specific values.
Bayesian methods allow for the explicit incorporation of any information previously obtained on the system in question through the prior, either from literature or previous experiments, resulting in a coherent framework for combining data from different sources[@Schoot2021].
Additionally, they are ideally suited for estimations that contain uncertainty and a lack of data[@McNeish2016].


Previous research on the applications of Bayesian methods in enzymatic networks have mostly been attempted from a systems biology perspective, focusing on whole-cell metabolomics[@St.John2019;@Liepe2014;@Jayawardhana2008], or focusing on simulated datasets and evaluating the feasibility of an alternative enzyme rate equation[@Choi2017].
The approach introduced here instead focusses on experimental relevance, specifically for the construction of encapsulated enzymes in flow, but is readily adoptable in most experimental enzymatic reactions setups, without requiring extensive computational expertise to employ.
<!-- Most essentially, it allows us to accurately quantify how much we do not understand about the ERNs we construct and investigate, highlighting potential sources of disagreement between experiments and models, or experimental errors, and indicating the most relevant experimental areas to explore further.  -->

<!-- We first show how kinetic parameters can be estimated in a flow-setup, and how the Bayesian approach immediately improves upon a simple linear-regression analysis for a single-substrate enzyme by automatically exploiting correlations that exist between different kinetic parameters, and different experimental conditions.
We then show how a database of experimental results from a diverse set of systems and conditions can be combined in a single analysis to create reliable parameter estimates, and subsequently can be used to evaluate the correctness of individual experiments relative to the rest of the database.

We then showcase other advantages of the approach, which we can use to estimate most likely inhibition and reaction mechanisms, and how experiments on different network topologies can be combined.
Finally, we discuss how results from these Bayesian methods should be interpreted and used, and their general importance for the development of increasingly complex artificial enzymatic reaction networks. -->

<!-- # Background -->
<!-- ![**Title** **a,** description](#link_to_figure){#fig:label} -->

# Methods

## Bead production

TODO: Add bead-production protocol

## Flow experiments

Flow experiments were conducted similar to description in previous work, in which the desired volume of PEBs is charged to a CSTR [ref @FernandezRegueiro2021]. 
The openings of the reactors are sealed with Whatman Nuclepore polycarbonate membranes (5 µm poresize). 
Cetoni Low-Pressure High-Precision Syringe Pumps neMESYS 290N were used to control the dispense of the different solutions, prepared in Gastight Hamilton syringes (2500 – 10000 µL), into the CSTR. 
The precise flow profile of the desired flowrates was programmed using the Cetoni neMESYS software.

To detect and determine outflow concentrations from the CSTR both online and offline detection was employed. 
Online absorbance detection was achieved with an Avantes AvaSpec2048 Fiber Optic spectrometer and Avantes AvaLight 355 nm LED combined with a custom designed flow cuvette provided to us by LabM8. 
Alternatively, offline measurement could be achieved by means of connecting the outflow to a BioRad Model 2110 fraction collector. 
These fractions could subsequently be probed for NADH absorbance using a Tecan Spark M10 platereader, or probed for ATP, ADP, NAD+ and NADH using a Shidmadzu Nexera X3 HPLC.

Details of the exact experimental protocols can be found in the Supporting Information.

## Modelling of enzyme kinetics in flow
<!-- 
![**Inference of kinetics in a flow setup** **A,** Reactors are used to create enzymatic networks with compartmentalized beads and substrates that can flow in and out. **B,** Reactor output of R-AMC cleavage by Trypsin, measuring the fluorescent signal of the product AMC. Substrate input concentration is changed multiple times, and measurements are taken at steady-state (indicated in gray). **C,** Steady-state output concentrations plotted against substrate input concentration. A least-squares fit (red dashed line) is obtained from a flow-modified Michaelis-Menten equation, resulting in parameter estimates $k_{cat} = 102.6 \pm 4.3$ and $K_M = 121.7 \pm 14.4$. **D,** Bayesian fit of the steady-state output concentrations, including mean posterior predictions (black dashed line) and 95% confidence interval (light purple). **E,** Parameter correlations (purple) automatically obtained from the posterior sampling distributions, and corresponding least-squares estimates and error bars (red) without correlation. **F,** Bayesian probability-distributions of the kinetic parameters $k_{cat}$, $K_M$ with corresponding least-squares estimates (red dashed lines), and noise estimate $\sigma$. ](figures/fig_setup.svg){#fig:setup}

TODO: Update section to connect better to previous experimental sections -->

<!-- All experiments are performed in a microfluidic setup, with the relevant enzymes encapsulated in beads and compartmentalized in a Continuously Stirred Tank Reactor (CSTR), while relevant substrates, inhibitors, and buffer are flown in via syringes attached to a pump setup, as shown in [@fig:setup]A-B and described in more detail in [ref @FernandezRegueiro2021]. -->
We generally assume that the enzymatic reactions behave according to a Michaelis-Menten-like mechanism, although other mechanisms might also be considered, and add flow-dependent terms to model the dynamics of the flow reactor.
Inclusion of these flow-terms yields the following system of Ordinary Differential Equations (ODEs) for a single-substrate single-product reaction:
<!-- $$\frac{d[P]}{dt}=\frac{V_{max} [S]}{K_M+[S]}-k_f [P]$$

$$\frac{d[S]}{dt}=\frac{-V_{max}[S]}{K_M+[S]}+k_f([S]_{in}-[S])$$ -->

$$
\mathbf{f}(\mathbf{C}, \phi, \theta): \begin{cases}
\frac{d[P]}{dt}&=\frac{V_{max} [S]}{K_M+[S]}-k_f [P]\\
\frac{d[S]}{dt}&=\frac{-V_{max}[S]}{K_M+[S]}+k_f([S]_{in}-[S])
\end{cases}
$$

Where $V_{max}=k_{cat}[E]$ and $K_M$ are the kinetic parameters $\phi$ that generally need to be estimated, and where we introduce a set of control parameters $\theta$, in the form of $\left[S\right]_{in}$, the effective substrate concentration flown into the reactor, and $k_f=\frac{flowrate\ \left(\frac{\mu L}{min}\right)}{reactor\ volume\left(\mu L\right)}$ the flow-constant.
Measurements of the product-concentration are performed when the system has reached steady-state conditions ($\frac{d\mathbf{C}}{dt}=0$), resulting in a set of steady-state concentrations $[P]_{ss}$ and $[S]_{ss}$.
These values can then be used in a fitting procedure to obtain kinetic parameter estimates.
<!-- 
Because $[S]$ is the substrate concentration inside the reactor, which is not necessarily equal to the input concentration, we substitute it by the stoichiometric conservation law $\left[S\right]=[S]in-[P]$.
This law necessarily always holds at steady-state conditions.
After rewriting, we obtain $[P]$ as a function of $[S]$:

$$\left[P\right]_{ss}=\frac{1}{2}\left(\frac{V_{max}}{k_f}+\ K_M+\left[S\right]_{in}\right)-\frac{1}{2}\sqrt{\left(\frac{V_{max}}{k_f}+\ K_M+\left[S\right]_{in}\right)^2-4\frac{V_{max}\left[S\right]_{in}}{k_f}}$$
$$=f\left(\left[S\right]_{in},\ k_f;V_{max},K_M\right)$$ -->

<!-- A typical example of this is shown in [@fig:setup]B for the cleavage of Cbz-Arg-7-amino-4-methylcoumarin (R-AMC) by Trypsin PEBs, for different substrate input concentrations. -->
<!-- Using the steady-state condition has the additional benefit of allowing us to collect an arbitrary number of samples from the same condition, in contrast to the transient states of initial reaction velocity measured in enzyme batch experiments.  -->
<!-- Usually, kinetic parameter estimates for these types of systems are obtained via a standard linear-regression approach, performing for example a least-squares fit ([@fig:setup]C), resulting in a specific set of values and error estimates. -->
<!--
allowing us to write the product outflow-concentration as a function of substrate-concentration:

$$k_f\left[P\right]=\frac{V_{max}\left[S\right]}{K_M+\left[S\right]}$$

Using the steady-state condition has the additional benefit of allowing us to collect an arbitrary number of samples from the same condition, in contrast to the transient states of initial reaction velocity measured in enzyme batch experiments.
An example of collecting such steady-state data at different substrate input-concentrations is shown in Figure 1B.
Because $[S]$ is the substrate concentration inside the reactor, which is not necessarily equal to the input concentration, we substitute it by the stoichiometric conservation law $\left[S\right]=[S]in-[P]$.
This law necessarily always holds at steady-state conditions.
After rewriting, we obtain $[P]$ as a function of $[S]$:

$$\left[P\right]_{ss}=\frac{1}{2}\left(\frac{V_{max}}{k_f}+\ K_M+\left[S\right]_{in}\right)-\frac{1}{2}\sqrt{\left(\frac{V_{max}}{k_f}+\ K_M+\left[S\right]_{in}\right)^2-4\frac{V_{max}\left[S\right]_{in}}{k_f}}$$
$$=f\left(\left[S\right]_{in},\ k_f;V_{max},K_M\right)$$ -->

<!-- The above equation relates the observed product steady-state concentration to the controlled experimental parameters (flowrate k_f and substrate input concentration $\left[S\right]_{in}$) and the kinetic parameters $V_{max}$ and $K_M$ that we want to estimate from experimental observations.  -->

## Creation of Bayesian models

In a Bayesian approach, the probability distributions for parameters of interest are obtained by application of Bayes’ theorem

$$P\left(\phi\middle| y\right)\propto P\left(\phi\right)P\left(y\middle|\phi\right)$$

which relates the posterior probability $P\left(\phi\middle| y\right)$ of a specific parameter value $\phi$ given the data $y$ observed during an experiment, to the likelihood $P\left(y\middle|\phi\right)$ of observing that specific data given the parameter value, and any previously available information of the parameter, the prior $P(\phi)$.
As the likelihood is a function of both the observed data and the values of the kinetic parameters, and not a probability distribution, we write $P\left(y\middle|\phi\right) = \mathcal{L}(y, \phi)$.

In the case of a single-substrate, steady-state enzymatic network, the observed data $y$ is given simply by the set of observed steady-state concentrations $\left[P\right]_{ss}$ at specific experimental conditions $\left[S\right]_{in}$ and $k_f$, while the parameter $\phi$ can be any of the kinetic parameters that is unknown, such as $k_{cat}$ or $K_M$.
Furthermore, because the data we collect is inherently noisy, we assume that the concentrations we observe are part of a normal distribution $[P]_{obs}\sim N([P]_{ss},\sigma)$ with a mean equal to the true steady-state concentration and an unknown standard-deviation $\sigma$.
This assumption allows us to write down the form of the likelihood:

$$\mathcal{L}(y,\phi) = \mathcal{N}\left([P]_{ss}-[P]_{obs},\sigma\right)$$
where $[P]_{ss} = g(\phi, \theta)$ is a function of the kinetic parameters and the experimental conditions.
The likelihood incorporates most sources of uncertainty, such as the intrinsic fluctuations of product concentration at steady-state and noise from the used measurement technique, inside the uncertainty-term $\sigma$.
This parameter is then inferred simultaneously with the kinetic parameters $k_{cat}$ and $K_M$, allowing us to directly estimate the uncertainty in our observations as well.
Any other sources of uncertainty, such as inconclusive data, or a wrong assumed reaction-mechanism, are implicitly encoded into the posterior probability distributions of the kinetic parameters.

We use the Python package PyMC3 [@Salvatier2016] and custom-written likelihood functions for observed steady-state concentrations, from which we can sample with the No-U-Turn Sampler (NUTS[@Hoffman2011]) by inclusion of likelihood gradients.
The steady-states can be obtained either by symbolically solving $\textbf{f}(\textbf{C}, \phi, \theta) = 0$, or by numerical root-finding of the vector-function $\textbf{f}$.
The gradients for the numerical steady-states are obtained from the Implicit Function Theorem, which relates the sensitivity of the steady-state concentrations $\frac{\partial g}{\partial \phi}$ to the kinetic parameters without needing to explicitly write down an expression for the steady-state concentrations, via $\frac{\partial g}{\partial \phi}(\phi, \theta) = - \Big[\frac{\partial f}{\partial C}(\textbf{C}, \phi, \theta)\Big]^{-1}\Big[\frac{\partial f}{\partial \phi}(\textbf{C}, \phi, \theta)\Big]$ , while gradients for symbolic steady-states are automatically obtained via automatic differentiation in PyMC3.
Using the NUTS-algorithm, we can obtain correlated probability distributions for the value of every kinetic parameter of interest.
<!-- An example of the resulting fit and parameter estimates for a simple, one-substrate enzyme system are shown in [@fig:setup]D-F. -->
Implementations of the models used in this paper and the scripts to generate the figures can be found in the Supporting Information. 

TODO: Add reference to SI/notebooks/Github at the end.

# Results and Discussion

## Obtaining improved accuracy from correlated parameter estimates

![**Improving parameter estimates by exploiting correlations** **A,** Steady-state concentrations of R-AMC cleavage by Trypsin, with and without inhibitor (AAA-AMC). **B,** Posterior parameter estimates obtained from the data without inhibitor present (blue) and with inhibitor present (red). Combining both datasets in one model yields more precise posterior estimates (dashed, purple) **C,** Posterior correlation plots of $k_{cat}$ and $K_I$ from the data without inhibitor present (blue, left), showing no correlation, and with inhibitor present (red, right), showing high nonlinear correlation. **D,** Combining data from both experiments yields a new posterior distribution (purple) that exactly corresponds to the intersection from the two experiments separately. **E,** Comparison of posterior $K_I$ estimates from the individual datasets (blue, red) to the estimate obtained from the combined dataset (purple).](figures/fig_correlations.svg){#fig:correlations}

We first show the relevancy of our Bayesian approach by estimating the kinetic parameters of Trypsin PEBs cleaving a substrate (Cbz-Arg-7-amino-4-methylcoumarin, R-AMC) while in the presence of an inhibitor (Suc-Ala-Ala-Ala-7-amino-4-methylcoumarin, AAA-AMC), shown in [@fig:correlations].
Two experiments were performed, one where the inhibitor was absent and one where the inhibitor was present ([@fig:correlations]A).
Both experiments on their own did not yield enough information to obtain conclusive estimates of all kinetic parameters involved ($k_{cat}$, $K_M$, $K_I$), as shown in [@fig:correlations]B.
Clearly, from the experiment without inhibitor relatively precise estimates can be obtained on $k_{cat}$ and $K_M$, but no information is obtained on the value of the inhibition constant $K_I$.
Thus, our posterior estimate of the inhibition constant is equivalent to our prior estimate (a uniform distribution between $1$ and $10*10^3$ $\mu M$).
In contrast, from the experiment with inhibitor present, a posterior estimate for the inhibition constant can be obtained, albeit not a precise one.
Additionally, from this experiment alone, the posterior estimates for the other kinetic parameters are also uncertain.

However, while the posterior estimates of the individual parameters remain uncertain, we do obtain additional information by analyzing the posterior correlations, shown in [@fig:correlations]C.
While the experiment without inhibitor does not show any correlation between the value of the estimated $k_{cat}$ and $K_I$ values, the experiment with inhibitor present shows a nonlinear correlation between low estimated values of $k_{cat}$ and high values of $K_I$, and vice versa.

Combining data from both experiments in a single likelihood function allows us to combine the certainty of the parameter estimates present in the first experiment with the highly correlated parameter estimates of the second experiment, to obtain a posterior distribution that is essentially an intersection of those obtained from the individual experiments ([@fig:correlations]D).
As expected, this allows us to obtain a much more precise estimate of the inhibitor constant, as shown in [@fig:correlations]E.
Moreover, this procedure yields improved estimates for every parameter in the system, not just the inhibition constant, which can be observed in [@fig:correlations]B.

<!-- Data from experiments is loaded in a long-form format,  where every observation is a single row in a table (Figure 3A) which records the value of every experimental parameter, in this case substrate (R) and inhibitor (AAA) input concentrations, flow constant (kf), and enzyme concentration (Tr), as well as the observed product concentration (AMC).
This data is used in a probabilistic model, shown in Figure 3B, which defines the relationship between the likelihood function and the kinetic parameters, and defines priors on those parameters.
For enzyme kinetics with no previous data, we generally choose to use diffuse priors, specifying the range of possible values with a uniform probability.
If previous estimates have been obtained, or if parameter values have been obtained from literature sources, then these can be specified instead of a diffuse prior.
If the parameter estimates converge to the upper boundary and accordingly have a hard cut-off at the boundary, then this is a good indication that either the range of possible values need to be increased or that the underlying kinetic model is incorrect.
After specification of the model and parameter priors, we typically run the inference procedure using the No-U-Turn Sampler (NUTS) and {10}^5 samples, resulting in a converged posterior distribution of parameter estimates.
From this posterior distribution we can directly obtain useful statistics about the inferred parameter, such as the mean, the maximum probability estimate, and a range of quantiles, shown in Table 1.
We can also sample parameter values from the posterior distribution and generate corresponding model predictions.
In Figure 3C we have plotted the resulting predictions of an experiment where the peptide R-AMC is cleaved by Trypsin  to yield AMC as a product, inhibited by AAA-AMC.
Shown are the confidence intervals for the model predictions, overlayed with the observed data points, as well as probability distributions for the values of the kinetic parameters V_{max} and K_M in Figure3C-D.  -->

Consequently, the Bayesian approach greatly simplifies the iterative addition of experimental data to update parameter estimates.
As shown here, subsequent measurements of enzyme activity in the presence of an inhibitor will not only allow an estimation of the inhibition constant, but also retro-actively improves the estimates for the Michaelis constant $K_M$ and the turnover number $k_{cat}$.
<!-- Moreover, this inclusion of all data can significantly increase the precision of parameter estimates that would remain highly uncertain if a single-experiment data approach is taken, where the parameter estimations for the kinetic constants become more precise after the incorporation of inhibition data in the model.  -->
<!-- Combining all data in one probabilistic model leads to more accurate results than just combining the resulting parameter estimates of both datasets. -->

## Combining diverse experimental datasets

<!-- Experiments performed on different systems, such as different combinations of enzymes cannot be combined in a trivial manner. However, in the Bayesian framework, parameters that occur in multiple systems can be accurately inferred by the usage of multiple likelihood functions. This method allows for correlated paremeter estimates across any number of different experimental setups, as long as at least 1 parameter is shared in both setups. -->
<!-- ![**Combining diverse experimental datasets** **A,** Three different ERN topologies are used in different reactors, and at different experimental conditions (varying input concentrations and volume of PEBs). **B,** Plots showing all collected observations at different input concentrations of glucose (x-axis) and co-factor (color intensity). The observed species is topology-dependent. **C,** Schematic of the causal network relating the observation likelihoods $\mathcal{L}_x$ to the inferable parameters, where likelihoods corresponding to either the GDH or HK topology only relate to a subset of the parameters. The combined GDH,HK likelihood relates to every kinetic parameter in the probabilistic model. **D,E** Posterior parameter estimates obtained from the model combining all three (GDH, HK, GDH+HK) observation likelihoods. For the GDH $k_{cat}$, two estimates are obtained because PEBs with two different enzyme concentrations were used in different experiments.](figures/fig_datafusion.svg){#fig:datafusion} -->
![**Combining diverse experimental datasets** **A,** Three different ERN topologies are used in different reactors, and at different experimental conditions (varying input concentrations and volume of PEBs). **B,** Plots showing all collected observations at different input concentrations of glucose (x-axis) and co-factor (color intensity). The observed species is topology-dependent. **C,** Schematic of the causal network relating the observation likelihoods $\mathcal{L}_x$ to the inferable parameters, where likelihoods corresponding to either the GDH or HK topology only relate to a subset of the parameters. The combined GDH,HK likelihood relates to every kinetic parameter in the probabilistic model. **D,E** Posterior parameter estimates obtained from the model combining all three (GDH, HK, GDH+HK) observation likelihoods. For the GDH $k_{cat}$, two estimates are obtained because PEBs with two different enzyme concentrations were used in different experiments.](figures/fig_datafusion_alta.svg){#fig:datafusion}


More complex ERNs introduce a number of additional challenges in modelling the system's behavior.
One of these challenges is combining data from a diverse range of experiments, both with variations in experimental conditions, and variations in network topologies due to the enzymes that are present.
Additionally, for some experiments only partial data can be obtained, for example in the case where only substrates involved in a single reaction can be observed, while substrates from a different reaction remain undetected.

In [@fig:datafusion], we show how data obtained from these different types of experiments can be captured in a single probabilistic model.
In [@fig:datafusion]A, we distinguish between 3 different network topologies, two with only a single type of enzyme PEB present, either glucose-dehydrogenase (GDH) or hexokinase (HK), and one where both enzymes PEBs are present simultaneously.
For all three topologies, multiple experiments are performed at different conditions, such as different substrate input-concentrations and PEB volumes used.
For the two single-enzyme topologies, detection of a single substrate is enough for full observability of the network (through stoichiometric conservation), while for the combined GDH+HK topology, only NADH is observed.
Thus, the substrates involved in the hexokinase-reaction are not directly detected.
These observations are shown in [@fig:datafusion]B.

All three topologies have a corresponding likelihood function that relates the observations to the kinetic parameters in question, as shown schematically in [@fig:datafusion]C (see the SI for the programmatic implementation of these likelihoods).
While the GDH+HK system does not allow for full observability of the network, its likelihood does allow us to correlate the GDH and HK kinetic parameters, consequently leading to improved estimates of all parameters involved.

![**Iterative posterior updating **  **A,B** Posterior parameter estimates obtained from the model combining all three (GDH, HK, GDH+HK) observation likelihoods. For every parameter, the distributions are shown for 3 different dataset sizes, with respectively 4, 6, and 16 experiments included. Distributions are shifted and scaled to increase visibility. For the GDH $k_{cat}$, two estimates are obtained because PEBs with two different enzyme concentrations were used in different experiments.](figures/fig_datafusion_altb.svg){#fig:datafusion2}

The resulting posterior estimates of combining all available data are shown in [@fig:datafusion2].
For the GDH PEB’s, two different batches were used with different enzyme concentration, resulting in two distinct effective $k_{cat}$ parameters.
Estimation of their respective values are performed under the assumption that the $K_M$ for the two substrates remain the same for both batches.
By directly encoding this assumption into the combined likelihood functions, observations on both batches become relevant for estimation of all the parameters involved.

Correlating the parameter estimates of the individual enzymes through a joint likelihood function allows us to potentially improve parameter estimates by observing a system not directly related to those parameters.
Thus, as more and more observations are made, any parameter estimates will increase in accuracy simply by the inclusion of more data. 
This iterative improvement of estimates as more data becomes available is shown by the gradual shrinkage of posterior distributions, implying that the estimates become more precise.
This improvement is most pronounced when little data is available (for example from 4 to 6 experiments), but gradually becomes less for larger datasets (for example from 10 to 16 experiments, see SI).

![**Evaluating uncertainty estimates** **A,** Posterior experimental uncertainty estimates for two specific HK-experiments, obtained from the posterior distributions calculated from the full dataset of all experiments. One experiment (green, SNKS04) has a low estimated uncertainty, while the other experiment (blue, SNCA18) has a much higher estimated uncertainty. **B, ** Associated observed datapoints of the low-uncertainty experiment, the posterior predictive distribution of expected observations, and 95% CI quantiles (black) **C, ** Associated observation datapoints of the high-uncertainty experiment, the posterior predictive distributions of the expected observations, and 95% CI quantiles (black).](figures/fig_datafusionb.svg){#fig:datafusionb}


Additionally, by estimating the uncertainty in every experiment individually, it becomes more practical for a large number of experiments to determine which ones have corresponding results, and which ones are potential outliers or contain experimental errors.
This can be observed especially in the uncertainty estimates for two specific HK experiments, as shown in [@fig:datafusionb]
One experiment, with experiment code SNKS04, has a relatively low uncertainty estimates ([@fig:datafusionb]A) and correspondingly, the posterior predictions obtained from the model are similar to the actual observations ([@fig:datafusionb]B).
However, another experiment stands out with a much higher uncertainty estimate ($\sigma\sim 400-600\ \mu M$), which indicates some unknown error in the observations made during that experiment.
Consequently, the posterior predictions show a very large spread and do not correlate well with the actual observations ([@fig:datafusionb]C).
Importantly, these uncertainty estimates are obtained by conditioning of the individual observations on the complete dataset of all experiments.
Large uncertainty estimates therefore imply results that do not correspond with most other performed experiments.

By estimating the uncertainty parameters alongside all of the kinetic parameters, individual experiments are allowed to be 'wrong', and consequently influence the final parameter estimates less than other experiments.
While not a solution for badly performed experiments, it does protect against drawing incorrect conclusions from incorrect data.
Consequently, the uncertainty estimates indirectly act as an automatic weighting factor for individual experiments, where experiments with higher estimated uncertainty are less relevant towards the kinetic parameter estimations.
It can also function as a key indicator for experiments influenced by an unknown source of error or systematic bias, especially in cases where large datasets collected over longer time periods are involved.

<!-- TODO: Connect/imply data lakehouse concepts -->

<!-- For more complicated enzymatic reactions or enzyme networks, a closed-form equation like $\left[P\right]_{ss}=\ f\left(\left[S\right]_{in},\ k_f;V_{max},K_M\right)$ cannot be obtained directly.
Instead, we can perform inference directly on the steady-state condition, $\frac{d\left[P\right]}{dt}=\ d[S1]dt=d[S2]dt=0$, or more explicitly by comparison of the outflow-terms and reaction rate terms $k_f\left[P\right]_{ss}=\ v\left(\left[S_1\right]_{ss},\left[S_2\right]_{ss};V_{max},K_{M,1},\ K_{M,2}\right)$.
This requires a careful consideration of the stoichiometric conservation laws, from which the steady-state substrate concentrations can be derived but is generally possible for most enzymatic networks.
Multi-substrate enzymes, like hexokinase, can often not be properly characterized within a single flow-experiment.
Instead, multiple experiments at different experimental conditions are required.
As every datapoint collected in every experiment is just another observation, all data can be combined and used in the same probabilistic model.
This is shown in Figure 6, where the improvement of parameter estimates is shown by inclusion of more experiments.
While inclusion of only the first 2 experiments does not yield precise estimates, the 3rd experiment greatly improves the estimates of all kinetic parameters, as it investigates a previously unexplored range of substrate input concentrations.
Inclusion of the 4th experiments does not actually make the estimates more precise, and slightly decreases the precision again.
This is eventually to be expected, as not all experiments will always agree with each other.
In this case, the 4th experiment is from a small enzymatic network containing both hexokinase (HK) and Glucose-dehydrogenase (GDH), and the estimates are obtained from an appropriately modified model that estimates both the HK and GDH kinetic parameters, thus correlating the posteriors of these parameters.
This continuous updating of posteriors as more data is collected is an essential feature of the Bayesian approach.
As more and more observations are made, any parameter estimates will increase in accuracy and become more robust to outlier experiments.  -->

## Comparing reaction mechanism hypotheses
<!-- For most enzymes it is not immediately obvious what type of reaction mechanism best describes the functionality of the enzyme. Especially when combining multiple datasets, the additional uncertainty of the correctness of observations -->

![**Comparing reaction mechanism hypotheses** **A,** Steady-state concentrations obtained during two experiments, from a G6PDH system at different glucose-6-phosphate input concentrations and NAD input concentrations. **B,** Four different hypotheses for Michaelis-Menten mechanisms without ($H_0$), and with NADH product inhibition ($H_1$-$H_3$). Only the reaction-rate is shown, but full sets of ODE's with additional flow-terms are used in the probabilistic model. **C,** Posterior parameter estimates for all four hypotheses. $H_0$ does not include an inhibition constant $KI_{NADH}$, but all other hypotheses do. **D,** Comparison of the PSIS-LOO information criterion for all four hypotheses (colored), and standard errors of the difference in information criterion with respect to the top-ranked model (grey). ](figures/fig_mechanisms.svg){#fig:mechanisms}

TODO: Update figure and text with latest data when available

The microscopic mechanisms underlying enzymatic reactions often allow for the creation of more complex kinetic models than simple Michaelis-Menten kinetics.
However, a more complex model, with more kinetic parameters, does not necessarily imply a more useful model.
Instead, in the presence of uncertain data, it can lead to overfitting and unrealistically high certainty in the estimates.

In [@fig:mechanisms] we show how the posterior estimates obtained using our Bayesian approach, can be used to compare different hypotheses for the reaction mechanism and associated kinetics of glucose-6-phosphate dehydrogenase (G6PDH) PEBs.
From a set of experiments performed at varying experimental conditions ([@fig:mechanisms]A), we propose a number of different hypotheses describing the suspected mechanism of product inhibition by NADH on the reaction rate ([@fig:mechanisms]B).
We also include a 0-hypothesis describing a mechanism where the formation of NADH has no inhibiting effect, although the inclusion of a 0-hypothesis is not necessary for using this methodology.

We consider 3 modes of NADH inhibition: competitive inhibition of the NAD-binding site ($H_1$), competitive inhibition of the G6P-binding site ($H_2$), and cooperative non-competitive inhibition of the enzyme activity ($H_3$).
All four hypotheses result in posterior distributions that give well-defined parameter estimates ([@fig:mechanisms]C), from which it is difficult to conclude the most likely hypothesis.
Instead, because the experimental noise per experiment is estimated alongside the kinetic parameters, the zero-hypothesis yields unrealistically precise estimates, due to the algorithm indicating that under the assumption that this hypothesis is true, one of the experiments included must contain very large errors (see SI).
The three hypotheses that do model the influence product-inhibition have similar precisions in their parameter estimates.

To compare all hypotheses, and determine the most (and least) likely ones, we perform a Pareto Smoothed Importance Sampling Leave-one-out (PSIS-LOO) cross-validation directly from the posterior probability distributions [@Vehtari2017].
This test efficiently determines the model that approximates the observed data best, while taking into consideration the complexity of the models (e.g. the number of kinetic parameters involved) to prevent overfitting.
From this hypothesis comparison we can conclude that given the experiments performed up to this point, a cooperative non-competitive inhibition is the most likely product-inhibition mechanism occurring in the G6PDH PEBs, although the other reaction mechanisms cannot yet be assumed out-of-question.
Similarly, while the zero-hypothesis is likely not correct, a small chance exists that indeed one experiment does contain large experimental errors and is therefore unreliable.

# Conclusion & Outlook

<!-- - Improved uncertainty estimates
- More efficient experimental data gathering
- Informed conclusions about reaction mechanism likelihoods
- Relevant for creating increasingly complex chemical systems (systems chemistry!) -->

We have demonstrated how a Bayesian approach towards analyzing enzymatic reaction networks allows for more accurate inference of the kinetics in these networks, while simultaneously taking into account any experimental or model-related uncertainties.
Using this approach, we have shown how experimental data can be combined in one coherent framework, in order for us to correlate the findings in these experiments and improve the estimation of parameters, as well as outlier detection.
This approach essentially allows us to continuously improve these estimates further by iteratively adding more experimental data to our models.
Moreover, this means that any new experiment might have the potential to unlock more information from older experiments in the process, enabling much more efficient data gathering.
Lastly, we have shown how this approach can be used to compare the likelihood of different reaction mechanism hypothesis. 
Comparing reaction mechanisms from a probabilistic perspective is a potentially powerful tool that can be used to make informed decisions about the next best experiments to perform when a lot of different mechanisms are under consideration.
Importantly, it can equally be used in re-analyzing old datasets in light of newly discovered or proposed mechanisms, or when new data becomes available.
However, care should be taken in interpreting the results from these comparisons as final conclusions.
Tt is not a suitable method to make statements about the absolute truth of a hypothesis, as the test only check the predictive power of each hypothesis relative to all other hypotheses under consideration.
Therfore, if no correct reaction mechanism is included in the hypotheses, then it will also not be considered in the test.

Bayesian methods open up multiple new areas of possibilities for the design of more complex enzymatic reaction networks, and for systems chemistry in general.
In addition to the findings presented here, a lot of potential exists in the usage of knowledge from literature for more realistic prior distributions, which could improve the obtained estimates further, and could allow for direct comparison between new results and previous studies.
Furthermore, more advanced hierarchical models and the inclusion of latent variables could potentially aid in discovering previously unknown interactions or hidden factors affecting the behavior of ERNs[@Engelhardt2017], both from a chemical point-of-view (allosteric effects, influence of pH) and an experimental point-of-view (systematic measurement errors, equipment deterioration).
Finally, calculation of the full posterior probability distributions opens the door for determining optimal experimental designs[@Huang2020].
These designs could be aimed at a variety of different goals, such as experimental conditions for the maximum information gain for a certain kinetic parameter, but also the maximum production of a specific substrate or set of substrates, taking automatically into account any uncertainties that still exist about the behavior of these systems.

We do note that the methods introduced here are still computationally relatively expensive, and some of the sampling techniques are not yet suitable for every type of data.
Additionally, while our approach can indicate the presence of bad data and experimental errors, it does not guarantee the absence of sources of error.
Care should still be taken to avoid a false sense of security when precise parameter estimates are obtained.

In conclusion, we have shown that the Bayesian approach we demonstrate here is highly relevant for the construction of complex enzymatic networks, allowing researchers to increase the predictability and reproducibility of artificial enzymatic networks, and allowing the field of enzymatic reaction networks to mature beyond toy models and proof-of-concepts.

# Associated Content

**Supporting Information**

TODO: add description of supporting information and link to Github

# Author Information

TODO: Add all author information

**Corresponding Author**

Wilhelm T.S. Huck - Institute for Molecules and Materials, Radboud University Nijmegen, 6525 AJ, Nijmegen, the Netherlands

**Author Contributions**

# Acknowledgments
We wish to thank Max Derks (LabM8) for his help and work in designing the flow cuvette used for online absorbance detection. 
We wish to thank Arjan H. de Kleine for his help and work in the design and manufacturing of the CSTRs.
This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (ERC Adv. Grant Life-Inspired, grant agreement no. 833466) and the Dutch Ministry of Education, Culture and Science (Gravity program 024.001.035).

# References