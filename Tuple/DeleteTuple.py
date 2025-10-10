Base_Tuple = ("Python", "Django", "Flask", "JavaScript", "ReactJS")
print("Before deleting:", Base_Tuple)

del Base_Tuple

try:
    print(Base_Tuple)
except NameError:
    print(" Base_Tuple deleted successfully!")
else:
    print(" Base_Tuple still exists:", Base_Tuple)
