import numpy as np
import matplotlib.pyplot as plt

from Bootstrapping_1 import *


data = np.array([1, 2, 3, 4, 5])  # Data is input here. For example, 1 2 3 4 and 5 are used.
num_iterations = 1000  # The number of iterations is put here.
# For more accurate results use a higher number of iterations.
bootstrap_samples = bootstrap(data, num_iterations)

''' 
To print all of the samples, use the code below:
#for i in range(len(bootstrap_samples)):
    #print(i) --> sample number 0-->n-1 where n = length of samples.
    #print(bootstrap_samples[i])
'''
