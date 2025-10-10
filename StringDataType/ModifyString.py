print("This is Modify String Data Type")
String_Data="Vishal jagdhne"
print(String_Data)
print(String_Data.lower())
print(String_Data.upper())
print(String_Data.replace("Vishal","vishu"))
print(String_Data.split(" "))
print(String_Data.strip())
print(String_Data.find("jagdhne"))
print(String_Data.index("jagdhne"))
print(String_Data.isalnum())
print(String_Data.isalpha())
print(String_Data.islower())
print(String_Data.isspace())
print(String_Data.istitle())
print(String_Data.startswith("Vishal"))
print(String_Data.endswith("jagdhne"))
# Negative indexing
print("Last character using negative indexing:", String_Data[-1])
# Reversing a string using slicing
print("Reversed string:", String_Data[::-1])
# String formatting 
print("Formatted string: My name is {}".format("Vishal"))
print(String_Data.split(","))