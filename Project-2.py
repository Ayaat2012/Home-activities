# Importing necessary libraries 
import pandas as pd
import numpy as np

# Creating a dictionary cosisting the following values
dataSet = {
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO'],
    'Salary': [100, 200, 0, 0]
}

# Creating a dataframe from the dictionary
df = pd.DataFrame(dataSet, index=[1,2,3,4])
print(df)

# Printing the initial 2 values of the dataframe
print("The initial 2 values:", df.iloc[0,[0,1]])

# Checking the total number of null values
print("Total null values:", df.isnull().sum())

# Printing the detailed info of the dataframe
print("Detailed information of dataframe:", df.info())