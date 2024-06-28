import numpy as np

def bootstrap(data,num_iterations): 
    '''
    data --> 1d array of values
    num_iterations --> integer number of bootstrap iterations
    '''
    bootstrap_samples = []
    length=len(data)

    for i in range(num_iterations):
        bootstrap_samples.append(np.random.choice(data,length,replace=True))

    return bootstrap_samples

#main:
data = np.array([1,2,3,4,5]) #--> replace with actual data.
num_iterations = 10

bootstrap_samples = bootstrap(data,num_iterations)

#DEBUGGING: printing all samples:


#Collating bootstrap data:
def collate(bootstrap_samples):
    length_data = len(data) #in this example its 5.
    values = {} #create empty dictionary
    key = 0 #key increases when a new key is added. so it should reach 5.
    for i in range(num_iterations): #0--> n-1
        for j in range(length_data): #0 --> 5 in this example.
            key_string = "key_" + str(bootstrap_samples[i][j]) #key_4, for example.
            values[key_string] = int(values.get(key_string, 0)) + 1
            #print(values)
                
    return values
    
values = collate(bootstrap_samples)

for key_name, count in values.items():
    print(f"{key_name}: {count}") #f --> format


#confidence interval:
