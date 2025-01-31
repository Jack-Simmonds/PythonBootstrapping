import numpy as np
import matplotlib.pyplot as plt

from Bootstrapping_1 import *

data = np.array([1, 2, 3, 4, 5])  # Data is input here. For example, 1 2 3 4 and 5 are used.
num_iterations = 10000  # The number of iterations is put here.
samples = bootstrap(data, num_iterations)

''' 
To print all of the samples, use the code below:
#for i in range(len(bootstrap_samples)):
    #print(i) --> sample number 0-->n-1 where n = length of samples.
    #print(bootstrap_samples[i])
'''

values = collate(samples, num_iterations)

'''
Displaying values from the dictionary:
for key_name, count in values.items():
    print(f"{key_name}: {count}") #f --> format
'''

graph_mean(samples, num_iterations)

[lower, upper] = confidence_mean(samples, num_iterations, 95)

print(f'The mean has a 95% certainty of being between {lower} and {upper}.')
