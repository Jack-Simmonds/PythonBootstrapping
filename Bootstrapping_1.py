import numpy as np
import matplotlib.pyplot as plt

def bootstrap(data,num_iterations): #data: 1d array of values. #num_iterations: integer value of bootstrap iterations.
    bootstrap_samples = []
    length=len(data)

    for i in range(num_iterations):
        bootstrap_samples.append(np.random.choice(data,length,replace=True))

    return bootstrap_samples

data = np.array([1,2,3,4,5]) #Data is input here. For example, 1 2 3 4 and 5 are used.
num_iterations = 1000 #The number of iterations is put here. For more accurate results use a higher number of iterations.
bootstrap_samples = bootstrap(data,num_iterations)

''' 
To print all of the samples, use the code below:
#for i in range(len(bootstrap_samples)):
    #print(i) --> sample number 0-->n-1 where n = length of samples.
    #print(bootstrap_samples[i])
'''

def collate(bootstrap_samples): #This function collates the data in a dictionary with an input of the bootstrap samples.
    length_data = len(data)
    values = {} #create empty dictionary
    key = 0 #key increases when a new key is added. so it should reach 5.

    for i in range(num_iterations): #0--> n-1
        for j in range(length_data): #0 --> 5 in this example.
            key_string = "key_" + str(bootstrap_samples[i][j]) #key_4, for example.
            values[key_string] = int(values.get(key_string, 0)) + 1
            #print(values)
    return values
    
values = collate(bootstrap_samples)

'''
Displaying values from the dictionary:
for key_name, count in values.items():
    print(f"{key_name}: {count}") #f --> format
'''

def graph_mean(bootstrap_samples): #This function graphs the mean of the data using matplotlib. The input is the bootstrap samples.
    bootstrap_means = []
    for i in range(num_iterations):
        mean = np.mean(bootstrap_samples[i])
        bootstrap_means.append(mean)

    plt.hist(bootstrap_means, bins=30, edgecolor='black') #bins = the number of intervals that the data is divided into.
    plt.title('Distribution of Bootstrap Means')
    plt.xlabel('Mean of Bootstrap Sample')
    plt.ylabel('Frequency')
    plt.show()

graph_mean(bootstrap_samples)

#confidence interval:
def confidence_mean(bootstrap_samples,confidence):
    lower_limit = (100-confidence)/2
    upper_limit = (100+confidence)/2
    
    return


confidence(bootstrap_samples, 95)
