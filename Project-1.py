# Importing necessary libraries
import numpy as np
from numpy import random

# Operations on one array
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:4])
for i in arr1:
    print(i)

# Operations on another singular array
arr2 = np.array([[1,2,3,5], [3,4,5,6]])
print(arr2.shape)
print(arr2.reshape(8,1))


arr3 = np.array([1,2,3,4,4])

# Joining two different arrays
Arr = np.concatenate((arr1, arr3))
print(Arr)

# Sorting values of the "Arr" array in an ascending order
print(np.sort(Arr))

# Creating a data table
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# The actual data, matching the defined structure
students_detail = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# Creating the structured array
students = np.array(students_detail, dtype=data_type)

# The result of the data table
print("Original array:")
print(students)

# Sorting data by height in an ascending order
print("\nSort by height")
sorted_students = np.sort(students, order='height')
print(sorted_students)