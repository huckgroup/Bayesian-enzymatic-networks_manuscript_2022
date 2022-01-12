---
title:  'Supporting Information'

link-references: true
figPrefix:
    - "SI figure"
    - "SI figures"
citation-style: analytical-chemistry
link-citations: true
link-bibliography: true

...

# Materials and instrumentation

## Materials

All chemicals and reagents were used as received from commercial suppliers without any further
treatment unless stated otherwise.

### Enzymes

TODO: Add GDH, HK, G6PDH, ...?
### Substrates
 
TODO: Add G, G6P, NAD, NADH, ATP, ADP, ... ?

## Instrumentation

### Spectroscopy

#### Offline absorbance

TODO: Adapt to protocol used in our experiments

Absorbance measurements for enzyme activity determination were performed with a Tecan Spark 10M plate reader. 
The Absorbance intensity of wells containing 30-200 µL of the reaction mixture was monitored for 1-4 min (shaking 3s/orbital mode/amplitude 4mm) at 23 °C using top or bottom reading mode. 
λex/λem =380 nm/460 nm for 7-amino-4-methylcoumarin-based substrates.

#### Online absorbance

TODO: Adapt to protocol used in our experiments

Absorbance in flow experiments was continuously measured at the reactor's output with a JASCO FP-8300ST spectrofluorometer for 7-amino-4-methylcoumarin-based substrates with thermostat at 25°C, wavelengths excitation 380 nm, emission 460 nm, bandwidths excitation and emission each 5 nm, manual sensitivity – PMT voltage 300 V (500 V for multiplication experiments in S4.4) with use of handmade polystyrene flow cuvette with an inner tube diameter of 1 mm.

### High-performance liquid chromatography

TODO: Adapt to protocol used in our experiments

High-performance Liquid Chromatography (HPLC) was performed using Shimadzu Nexera/Prominence system under a 0.8 mL/min flow at 50 °C with a Shim-pack GIST-AQ C18 column. 
For the Shimadzu system, an 8.8 min gradient program was used starting from 20% acetonitrile in H 2 O (both with 0.1% TFA): 0.3 min – 20%, 5.5 min – 90%, 5.8 min – 90 %, 5.85 min – 20 %, 8.8 min – 20%.

## Software
Python scripts and Jupyter notebooks were used to create the Bayesian models and perform inference and predictive sampling. 
Example notebooks with explanation, and notebooks used for creating the figures in the publication can be found on the accompanying [github repository](https://github.com/huckgroup/Bayesian-enzymatic-networks_manuscript_2022).
This repository also includes version information for all software dependencies.
PDF reproductions of the example notebooks are also included in this supporting information.

To determine likelihoods of partially observed enzyme networks, a custom Theano operator was written to calculate likelihoods from steady-state conditions. 
This SteadyStateOperator can be found in the [BayERN Python package](https://github.com/huckgroup/BayERN), alongside documentation, and is included in the dependencies of the manuscript github repository.

# Production and characterisation of polyacrylamide-enzyme beads

## Empty bead production method

The microfluidics device described in *Fernández Regueiro, et al.*[@FernandezRegueiro2021] was used to produce gel beads with a 20 µm wide T-junction, following an adapted procedure from *Rivello et al*[@Rivello2020]. 
The gel solution phase consisted of 9.6% (w/v) acrylamide, 0.4% (w/v) N,N'-methylenebisacrylamide, 0.5% (w/v) acrylic acid and 1.5% (w/v) 2,2′Azobis(2-methylpropionamidine) dihydrochloride. 
The oil phase contained 1.5% (v/v) Pico-Surf&trade; 1 in fluorinated fluid HFE-7500 (3M). 
The flow rates for gel phase and oil phase were 600 µL/h and 900 µL/h, respectively. 
The outflow emulsion was collected in the tube which was filled with 100 µL mineral oil. 
Afterwards beads were polymerised using UV lamp for 10 minutes at 70% gain. 
After polymerisation the lowest layer containing fluorocarbon phase was carefully removed with a P200 pipette. 
The remaining beads were washed 3 times with 20% (v/v) 1H,1H,2H,2H-Perfluoro-1-octanol in HFE-7500 (3M), then 3 times with 1% (v/v) Span 80 in hexane, 3 times with 0.1% (v/v) Triton X-100 in Milli-Q and finally 3 times with Milli-Q. 
Every washing step was finalised with mixing the tube using vortex, centrifuging at 5000 x g for 3 min and removing the layer which was not containing beads. 
Furthermore, beads were flash frozen using nitrogen and freeze dried overnight. 
After re-wetting beads, their size was determined using light microscope with 40x magnitude objective. 
The average size was 50 µm in diameter.

## General Enzyme Immobilisation after Polymerisation (ELAP)

Empty acrylamide beads were re-dissolved in Milli-Q at a concentration of 0.0322 mg/µL.
1-(3-Dimethylaminopropyl)-3-ethylcarbodiimide hydrochloride (100 mM) and N-Hydroxysuccinimide (100 mM) were added to the reaction mixture.
The total volume of the activation solution was 5-fold of the beads volume. 
The reaction mixture tube was put on the roller bank for 30 min. 
After this, beads were centrifuged at 5000 x g for 3 min. 
The supernatant was carefully removed using P200 pipette. 
Beads were washed 3 times by adding Milli-Q, mixing using vortex, centrifuging and removing the supernatant.
Furthermore, enzyme (xxx conc, units, Jeroen?, maybe add protocols/values for specific experiments below?) was added to the beads.
The tube was put on the roller bank for 2 h coupling step. 
Sequentially, beads were washed 8 times by adding Milli-Q, centrifuging and removing the supernatant. 
Finally, beads were flash frozen using nitrogen and freeze dried overnight.

# Overview of experiments

Data from these experiments can be found on the accompanying [github repository](https://github.com/huckgroup/Bayesian-enzymatic-networks_manuscript_2022) in the `data` folder as csv-files.
The files are directly used during analysis performed in the Jupyter notebooks.

| Code |flowrate|enzymes|E volume ($\mu L$)|E batch|input substrates|observed substrates|observation techniques|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|SNCA14|750|GDH|10|1|G, NAD|NADH|offline absorbance|
|SNCA15|750|GDH|10|1|G, NAD|NADH|offline absorbance|
|SNCA17|750|HK|10|1|G, ATP|G6P|G6P assay|
|SNCA18|750|HK|1|1|G, ATP|G6P|G6P assay|
|SNKS03|750|HK|1|1|G, ATP|G6P|G6P assay|
|SNKS04|750|HK|1|1|G, ATP|G6P,ATP|G6P assay,HPLC|
|SNKS08|750|G6PDH|10|1|G6P, NAD|NADH|offline absorbance|
|SNKS11|750|GDH|0.5|2|G, NAD|NADH|offline absorbance|
|SNKS12|750|GDH|0.5|2|G, NAD|NADH|offline absorbance|
|SNKS18|750|GDH|2.0|3|G, NAD|NADH|offline absorbance|
|SNKS20|750|G6PDH|2.0|1|G6P, NAD|NADH|online absorbance|

Table: Overview of single-enzyme experiments

| Code |flowrate|enzymes|E volume ($\mu L$)|E batch|input substrates|observed substrates|observation techniques|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|SNKS06|750|GDH,HK|10.0, 1.0|1, 1|G, NAD, ATP|NADH,ADP|offline absorbance,HPLC|
|SNNS002|750|GDH,HK|0.5, 1.0|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS003|750|GDH,HK|0.25, 1.5|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS004|750|GDH,HK|0.333, 1.33|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS005|750|GDH,HK|0.666, 0.666|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS006|750|GDH,HK|0.75, 0.5|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS007|750|GDH,HK|0.5, 1.0|2, 1|G, NAD, ATP|NADH|offline absorbance|

Table: Overview of multi-enzyme experiments

# Overview of computational methods
All computational studies were performed with Jupyter notebooks. Datasets were loaded in from csv-files with Pandas, and if relevant, concatenated together into larger objects.

The Bayesian model, including the determination of prior probabilities and likelihood function, was created using PyMC3.
Generally, prior probabilities for Michaelis-Menten parameters were chosen as uniform distributions over a specified interval.
These distributions were used as uninformative priors to ensure no subjective information would enter the model, while garanteeing correct sampling and estimation of parameters.
Priors for the uncertainty estimations (denoted by `sigma` in the notebooks) were given an exponential distribution, which also acted as an uninformative distribution, while garanteeing correct sampling.
In larger models, where multiple likelihoods were combined, hyperpriors were placed on the $k_{cat}$ and $\sigma$ priors to increase convergence of the sampling algorithm.

All sampling was peformed using the No-U-Turn Sampler (NUTS), which is an adaptive step-size  Hamiltonian Monte Carlo sampler. 
When (automatically, or via a custom operator) the gradients of the likelihoods with respect to the kinetic parameters were given, this samples is much more efficient then a classical Metropolis Monte Carlo sampler, showing faster convergence and needing less samples for precise posterior estimations.
Generally, sampling was performed using 4 or 8 independent chains on 4 or 8 cpu cores, all with 1000 tuning steps, and 1000 sampling steps, and a target step acceptance probability of 0.95.
These values were found to yield good sampling results without becoming computatially inefficient.

The samples obtained from the posterior distribution were further analysed using standard statistical tools in Python, the Numeric Python package and the Scientific Python package (NumPy and Scipy).
To ensure the accessibility and reproducibility of these results the datasets and Jupyter notebooks, used for the analysis and creation of figures found in the publication, are made available as additional Supporting Information, and directly on github at https://github.com/huckgroup/Bayesian-enzymatic-networks_manuscript_2022 .

# Extended iterative combination of experiments

![**Extended iterative posterior updating **  **A,B** Posterior parameter estimates obtained from the model combining all three (GDH, HK, GDH+HK) observation likelihoods. For every parameter, the distributions are shown for 15 different datasets, with each following dataset containing an extra experiment, added in chronological order. Distributions are shifted and scaled to increase visibility. For the GDH $k_{cat}$, two estimates are obtained because PEBs with two different enzyme concentrations were used in different experiments.](figures/fig_progression.svg){#fig:progression}



# References