import numpy as np
import matplotlib.pyplot as plt


def bootstrap(data, num_iterations):
    """
    Function bootstrap resamples the input data by randomising 'num_iterations' times.

    Parameters:
        data (1d array): The 1D array of values.
        num_iterations (int): The number of bootstrapping iterations.

    Returns:
        bootstrap_samples (2d array): An array containing all randomised samples.
    """
    bootstrap_samples = []
    length = len(data)

    for i in range(num_iterations):
        bootstrap_samples.append(np.random.choice(data, length, replace=True))

    return bootstrap_samples


def collate(bootstrap_samples, num_iterations):
    """
    Function collate, collates the resampled data by assigning each resample possibility to a string key,
    then assigns the number of times this has been resampled to the key's value.

    Parameters:
        bootstrap_samples (1d array): A 1D array of samples.
        num_iterations (int): The number of bootstrapping iterations.
    Returns:
        values (dictionary): The collated data stored as a dictionary.
    """
    length_data = len(bootstrap_samples[0])
    values = {}  # Create empty dictionary
    key = 0  # Key increases when a new key is added. so it should reach 5.

    for i in range(num_iterations):  # 0--> n-1
        for j in range(length_data):  # 0 --> 5 in this example.
            key_string = "key_" + str(bootstrap_samples[i][j])  # key_4, for example.
            values[key_string] = int(values.get(key_string, 0)) + 1
            # print(values)
    return values
    

def graph_mean(bootstrap_samples, num_iterations):
    """
    Function graph_mean graphs the mean of the data using matplotlib.

    Parameters:
        bootstrap_samples (1d array): A 1D array of samples.
        num_iterations (int): The number of bootstrapping iterations.
    Returns:
        None.
    """
    bootstrap_means = []
    for i in range(num_iterations):
        mean = np.mean(bootstrap_samples[i])
        bootstrap_means.append(mean)

    plt.hist(bootstrap_means, bins=30, edgecolor='black') # bins = the number of intervals that the data is divided into.
    plt.title('Distribution of Bootstrap Means')
    plt.xlabel('Mean of Bootstrap Sample')
    plt.ylabel('Frequency')
    plt.show()


# Confidence interval:
def confidence_mean(bootstrap_samples, num_iterations, confidence):
    """
    Function confidence_mean calculates the confidence interval of the mean based on an inputted confidence
    value (as a percentage).

    Parameters:
        bootstrap_samples (1d array): A 1D array of samples.
        num_iterations (int): The number of bootstrapping iterations.
    Returns:
        lower_limit (float): The lower limit of confidence.
        upper_limit (float): The upper limit of confidence.

    Preconditions:
        The confidence interval should be expressed as a percentage, for example, confidence=95 represents a confidence
        interval of 95%.
    """

    bootstrap_means = []
    for i in range(num_iterations):
        mean = np.mean(bootstrap_samples[i])
        bootstrap_means.append(mean)

    lower_limit = (100-confidence)/2
    upper_limit = (100+confidence)/2

    lower_bound = np.percentile(bootstrap_means, lower_limit)
    upper_bound = np.percentile(bootstrap_means, upper_limit)
    
    return [lower_bound, upper_bound]

