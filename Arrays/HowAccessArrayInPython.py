# How to access elements in an array (list) in Python
print("How to access elements in an array in Python")

# Create a list (array) of values
collection_record = ['LaxmiAai', 'LaxmiAai_2', 'RenukaAai', 'HarHar_Mahadev', 'Ganpati_Bappa', 'Jijus']

# Print all elements in the list
print("All elements in the array:", collection_record)

# Accessing elements by index
print("\nAccessing elements one by one using index:")
print("First element:", collection_record[0])
print("Second element:", collection_record[1])
print("Third element:", collection_record[2])

# Accessing a range of elements (slicing)
print("\nAccessing a range of elements:")
print("From index 0 to 2:", collection_record[0:3])
print("From index 2 to 4:", collection_record[2:5])
print("From start to 3:", collection_record[:4])
print("From index 3 to end:", collection_record[3:])

# using for loop 
for x in collection_record:
    print(x)