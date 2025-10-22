# Demonstration: Removing elements from an array (list)
print("Array remove methods in Python")

# Create a list (array)
collection_record = ['LaxmiAai', 'RenukaAai', 'HarHar_Mahadev', 'Ganpati_Bappa', 'Sai_Baba', 'Jijus']
print("Original array:", collection_record)

# 1️⃣ Remove by value using remove()
collection_record.remove('Sai_Baba')
print("\nAfter removing 'Sai_Baba':", collection_record)

# 2️⃣ Remove by index using pop()
# pop() removes element at a specific index (default: last element)
# collection_record.pop(2)
# print("After removing index 2 element:", collection_record)
# Remove with the Array value name wise 
# collection_record.remove('Sai_Baba')
# print("After Remove Sai_Baba",collection_record)

# 3️⃣ Delete using del statement
# del collection_record[0]
# print("After deleting first element using del:", collection_record)

# 4️⃣ Clear the entire array
# collection_record.clear()
# print("After clearing all elements:", collection_record)

# try to use condition thow 
if 'Sai_baba' in collection_record:
    collection_record.remove('Sai_baba')
    print("Remove Sai bab")
else:
    print("There is not avaible now ")

