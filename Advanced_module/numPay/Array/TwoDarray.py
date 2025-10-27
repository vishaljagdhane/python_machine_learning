# Print a message
print("This is a two-dimensional array example")

# Import the NumPy library with alias 'np'
import numpy as np

# Create a 2D NumPy array
twoD = np.array([
    ['Vishal', 'Vishu', 'Shubhangi'],
    ['Deogiri', 'UDMS', 'Vivekand']
])

# Print the 2D array
print("The 2D array is:\n", twoD)

# Check the number of dimensions of the array
print("Number of dimensions of the array:", twoD.ndim)

# Loop through the array row by row and print each row
for row in twoD:
    print(row)
