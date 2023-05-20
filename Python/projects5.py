# importing the necessary libraries
import numpy as np
import pandas as pd


# creating a function to calculate the sum of two numbers
def sum_func(num1, num2):
  sum = num1 + num2
  return sum


# creating a function to calculate the product of two numbers
def product_func(num1, num2):
  product = num1 * num2
  return product


# creating a function to calculate the mean of a list of numbers
def mean_func(list_num):
  mean = np.mean(list_num)
  return mean


# creating a function to convert a pandas dataframe to a dictionary
def df_to_dict(df):
  df_dict = df.to_dict()
  return df_dict


# creating a main function to call the other functions
def main():
  # create sample data
  data = {'A': [1, 2, 3, 4, 5],
          'B': [6, 7, 8, 9, 10]}
  df = pd.DataFrame(data)
