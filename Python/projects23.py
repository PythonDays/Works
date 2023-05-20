# Project 23 - Simple Python Project

# Import necessary packages
import pandas as pd
import numpy as np


# Define a function for creating a new DataFrame
def create_dataframe(df):
  # Create dataframe from input
  new_df = pd.DataFrame(df)

  # Return the new DataFrame
  return new_df


# Define a function for calculating the mean
def calc_mean(data):
  # Calculate the mean of the data
  mean = np.mean(data)

  # Return the mean
  return mean


# Define a function for calculating the median
def calc_median(data):
  # Calculate the median of the data
  median = np.median(data)

  # Return the median
  return median


# Define a function for calculating the standard deviation
def calc_std(data):
  # Calculate the standard deviation of the data
  std = np.std(data)

  # Return the standard deviation
  return std


# Main function
def main():
  # Create a sample data
  data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # Create a DataFrame from the data
  df = create_dataframe(data)

  # Calculate the mean of the data
  mean = calc_mean(df)

  # Calculate the median of the data
  median = calc_median(df)

  # Calculate the standard deviation of the data
  std = calc_std(df)

  # Print the results
  print("Mean:", mean)
  print("Median:", median)
  print("Standard Deviation:", std)


# Run the main function
if __name__ == "__main__":
  main()
