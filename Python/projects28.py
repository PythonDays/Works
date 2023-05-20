#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating a list of values
values = [1,2,3,4,5,6,7,8,9,10]

#creating a dataframe from the list and naming it df
df = pd.DataFrame(values, columns=['Number'])

#adding a new column 'Power_of_two' to the dataframe
df['Power_of_two'] = df['Number']**2

#creating a plot of the dataframe
plt.scatter(df['Number'], df['Power_of_two'])
plt.xlabel('Number')
plt.ylabel('Power of two')
plt.title('Power of Two vs Number')
plt.show()
