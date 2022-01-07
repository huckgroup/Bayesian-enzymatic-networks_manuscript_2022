---
title:  'Supporting Information'

link-references: true
figPrefix:
    - "figure"
    - "figures"
citation-style: analytical-chemistry
link-citations: true
link-bibliography: true

...

# Materials and instrumentation

## Materials

### Enzymes

### Substrates
## Instrumentation

### Spectroscopy

### High-performance liquid chromatography

### Flow experiments

## Software
Python scripts and Jupyter notebooks were used to create the Bayesian models and perform inference and predictive sampling. 
Example notebooks with explanation, and notebooks used for creating the figures in the publication can be found on the accompanying [github repository](https://github.com/huckgroup/Bayesian-enzymatic-networks_manuscript_2022).
This repository also includes version information for all software dependencies.

To determine likelihoods of partially observed enzyme networks, a custom Theano operator was written to calculate likelihoods from steady-state conditions. 
This SteadyStateOperator can be found in the [BayERN Python package](https://github.com/huckgroup/BayERN), alongside documentation, and is included in the dependencies of the manuscript github repository.

# Production and characterisation of polyacrylamide-enzyme beads

# General pipeline for experiments in flow

# Overview of experiments
  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  Demonstration of simple table syntax

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
|SNKS19|750|GDH|5.0|3|G, NAD|NADH|offline absorbance|
|SNKS20|750|G6PDH|2.0|1|G6P, NAD|NADH|online absorbance|

Table: Overview of single-enzyme experiments

| Code |flowrate|enzymes|E volume ($\mu L$)|E batch|input substrates|observed substrates|observation techniques|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|SNKS06|750|GDH,HK|10.0, 1.0|1, 1|G, NAD, ATP|NADH,ADP|offline absorbance,HPLC|
|SNNS002|750|GDH,HK|0.05, 1.0|2, 2|G, NAD, ATP|NADH|offline absorbance|
|SNNS003|750|GDH,HK|0.025, 1.5|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS004|750|GDH,HK|0.0333, 1.33|2, 2|G, NAD, ATP|NADH|offline absorbance|
|SNNS005|750|GDH,HK|0.0666, 0.666|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS006|750|GDH,HK|0.075, 0.5|2, 1|G, NAD, ATP|NADH|offline absorbance|
|SNNS007|750|GDH,HK|0.05, 1.0|2, 1|G, NAD, ATP|NADH|offline absorbance|

Table: Overview of multi-enzyme experiments

# Overview of computational methods

# References