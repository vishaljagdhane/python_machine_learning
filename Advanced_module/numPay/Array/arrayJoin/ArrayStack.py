# Program to demonstrate the use of np.stack to join multiple arrays
print("Use of Stack Method to Join Multiple Arrays ")

print("What is stack method?") 
print("Stack method is used to join multiple arrays along a new axis, like 'same index items' are paired together.")

import numpy as np

# Array of mobile brands
mobile_info = np.array(['Vivo','Apple','Oppo','Blackberry'])

# Array of corresponding mobile prices
price_info = np.array([15000, 70000, 20000, 25000])

# Using np.stack to join arrays
# axis=0 means stacking along the first axis (creates rows from each array)
stacked_array = np.stack((mobile_info, price_info), axis=1)

# If we used axis=1, it would pair same-index elements as rows
# stacked_array = np.stack((mobile_info, price_info), axis=1) 
# Result would be: 
# [['Vivo', 15000],
#  ['Apple', 70000],
#  ['Oppo', 20000],
#  ['Blackberry', 25000]]

print("Stacked Array with axis=0 (rows = each array):")
print(stacked_array)

# Explanation:
# We use stack method when we want to combine multiple arrays along a **new dimension**.
# - axis=0 → each original array becomes a row
# - axis=1 → items with the same index are paired together into a row
# This is useful when we want structured data, like pairing items with their corresponding values.
