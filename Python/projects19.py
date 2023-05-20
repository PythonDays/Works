# Import the necessary libraries
import pandas as pd
import numpy as np

# Read in the data
data = pd.read_csv("data.csv")

# Create a list of all the columns
columns = list(data.columns)

# Create an empty dictionary to store the results
results = {}

# Iterate through each column in the data
for column in columns:
  # Calculate the mean of each column and store in the results dictionary
  results[column] = data[column].mean()

  # Calculate the standard deviation of each column and store in the results dictionary
  results[column + "_std"] = data[column].std()

  # Calculate the median of each column and store in the results dictionary
  results[column + "_med"] = data[column].median()

# Print the results
for key, value in results.items():
  print("{}: {}".format(key, value))
