# Demonstration: Using a for loop to print each value from an array (list)
print("Array using for loop — printing array values one by one")

# Create a list (array) of values
collection_record = ['LaxmiAai', 'LaxmiAai_2', 'RenukaAai', 'HarHar_Mahadev', 'Ganpati_Bappa', 'Sai_Baba']

# Add one more value to the array using append()
collection_record.append('Jijus')

# Print each element in the array using a for loop
print("\nPrinting each array element:")
for loop_item in collection_record:
    print(loop_item)
