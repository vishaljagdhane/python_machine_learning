# -------------------------------------------
# Example: Class with Object and User Input
# -------------------------------------------

class ClassWithObject:
    # Constructor (called automatically when object is created)
    def __init__(self, name):
        self.name = name
        print(f"I am {self.name}")

# Take input from user
gettingValue = input("Please enter your Name: ")

# Create an object and pass the value
obj = ClassWithObject(gettingValue)
