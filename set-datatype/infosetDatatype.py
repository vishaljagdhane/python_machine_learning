print("Information about set datatype")
print("A set is a data type in Python that can store multiple values in a single variable using the set() function.")
print("Set is one of 4 built-in data types in Python used to store collections of data. The other 3 are List, Tuple, and Dictionary — each with different qualities and use cases.")
print("A set is a collection that is unordered, unchangeable*, and unindexed.")
print("*Note: 'Unchangeable' means the items themselves cannot be changed, but you can add or remove items.")

example_set = {"apple", "banana", "cherry"}  # A set storing multiple values
print("Example Set:", example_set)
print("Duplicates Not Allowed in Set")
duplicate_set = {"apple", "banana", "cherry", "apple", "banana"}  # Duplicate values will be removed
print("Set with Duplicates Removed:", duplicate_set)
