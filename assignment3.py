import numpy as np

# Part 1: Saving and Loading data with text files
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Save array to a text file
np.savetxt('array_data.txt', array1)

# Load array from a text file
loaded_array1 = np.loadtxt('array_data.txt')
print("Text File Data:\n", loaded_array1)

# Part 2: Saving and Loading data with binary files
# Save array to a binary file
np.save('array_data.npy', array1)

# Load array from a binary file
loaded_array2 = np.load('array_data.npy')
print("Binary File Data:\n", loaded_array2)

# Part 3: Saving and Loading data with CSV files
# Save array to a CSV file
np.savetxt('array_data.csv', array1, delimiter=',')

# Load array from a CSV file
loaded_array3 = np.genfromtxt('array_data.csv', delimiter=',')
print("CSV File Data:\n", loaded_array3)

# Part 4: Demonstrating loading from text files again
# Save array to a text file
np.savetxt('array_data_v2.txt', array1)

# Load array from a text file
loaded_array4 = np.loadtxt('array_data_v2.txt')
print("Text File Data (v2):\n", loaded_array4)

# Part 5: Demonstrating loading from binary files again
# Save array to a binary file
np.save('array_data_v2.npy', array1)

# Load array from a binary file
loaded_array5 = np.load('array_data_v2.npy')
print("Binary File Data (v2):\n", loaded_array5)
