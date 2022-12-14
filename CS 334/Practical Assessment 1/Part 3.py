import numpy as np
import math


# def calc_entropy(column):
#     """
#     Calculate entropy given a pandas series, list, or numpy array.
#     """
#     # Compute the counts of each unique value in the column
#     counts = np.bincount(column)
#     # Divide by the total column length to get a probability
#     probabilities = counts / len(column)
#
#     # Initialize the entropy to 0
#     entropy = 0
#     # Loop through the probabilities, and add each one to the total entropy
#     for prob in probabilities:
#         if prob > 0:
#             # use log from math and set base to 2
#             entropy += prob * math.log(prob, 2)
#
#     return -entropy
#
#
# def calc_information_gain(data, split_name, target_name):
#     """
#     Calculate information gain given a data set, column to split on, and target
#     """
#     # Calculate the original entropy
#     original_entropy = calc_entropy(data[target_name])
#
#     # Find the unique values in the column
#     values = data[split_name].unique()
#
#     # Make two subsets of the data, based on the unique values
#     left_split = data[data[split_name] == values[0]]
#     right_split = data[data[split_name] == values[1]]
#
#     # Loop through the splits and calculate the subset entropies
#     to_subtract = 0
#     for subset in [left_split, right_split]:
#         prob = (subset.shape[0] / data.shape[0])
#         to_subtract += prob * calc_entropy(subset[target_name])
#
#     # Return information gain
#     return original_entropy - to_subtract
#
#
# def highest_info_gain(data, columns, y):
#     # Intialize an empty dictionary for information gains
#     information_gains = {}
#
#     # Iterate through each column name in our list
#     for col in columns:
#         # Find the information gain for the column
#         information_gain = calc_information_gain(data, data[col], y)
#         # Add the information gain to our dictionary using the column name as the ekey
#         information_gains[col] = information_gain
#
#         # Return the key with the highest value
#     return max(information_gains, key=information_gains.get)


data = {
    "x1" : [5, 10, 8, 8, 7, 6, 11, 2, 10, 1],
    "x2" : [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    "x3" : [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    "y" : [1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
}
columns = ["x1","x2","x3"]
print(highest_info_gain(data, columns, "y"))
