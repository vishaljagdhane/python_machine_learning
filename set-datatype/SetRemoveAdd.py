print("This Method adding set value , if value is already present it will not add again")
Adding_newValue = {"apple", "banana", "cherry"}
print("Base Set Value:", Adding_newValue)
print("Adding_newValue.add('banana') This add method ")  # Trying to add a duplicate value
Adding_newValue.add("orange")
print("After Adding New Value:", Adding_newValue)

print("\nThis Method removing set value , if value is not present it will raise an error")
Adding_newValue.remove("banana")
print("After Removing Value:", Adding_newValue)
print("Adding_newValue.remove('grapes') This remove method will raise an error if value is not present")
# Uncommenting the next line will raise a KeyError

print("This update method adding multiple set values , if value is already present it will not add again")
Adding_newValue = {"apple", "banana", "cherry"}
print("Base Set Value:", Adding_newValue)
new_datavalues={"orange", "mango", "grapes"}
Adding_newValue.update(new_datavalues)
print("After Adding New Values:", Adding_newValue)