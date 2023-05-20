# importing necessary libraries
import pandas as pd
import numpy as np


# creating a function to read the csv file
def read_csv_data(filename):
  data = pd.read_csv(filename)
  return data


# creating a function to aggregate the data
def aggregate_data(data):
  grouped_data = data.groupby('State')['Population'].sum()
  return grouped_data


# creating a function to plot the data
def plot_data(data):
  data.plot(kind='bar', title='Total Population by State')


# main function
def main():
  # reading the csv file
  data = read_csv_data('data.csv')
  # aggregating the data
  grouped_data = aggregate_data(data)
  # plotting the data
  plot_data(grouped_data)


if __name__ == "main":
  main()
