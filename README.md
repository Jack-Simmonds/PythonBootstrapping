# Python Bootstrapping
An in-progress Python project that calculates confidence intervals by resampling data. 

For a quick demo of its capabilities, open "Demo1.py" and run after installing the necessary packages.

## Available Functions:
- Bootstrap: Resamples the input data by randomising 'num_iterations' times.
- Collate: Collates the resampled data by assigning each resample possibility to a string key, then assigns the number of times this has been resampled to the key's value.
- Graph_mean: Graphs the resampled data's means using matplotlib.
- Confidence_mean: Calculates the confidence interval of the mean based on an inputted confidence value (as a percentage).

## Current Restrictions:
- Data input must be 1-dimensional.
- Inflexible functionality.
