print("concatenate Method using merge Multiple Arrays")
import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])
merged_array =np.concatenate((array1, array2))
print(merged_array)
merged_array2 =np.concatenate((merged_array,array3))
print(merged_array2)