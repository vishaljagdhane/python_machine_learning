class ClassWithMoreFunction:
    def __init__(self):
        pass

    def userInformation(self, fname, mname, lname):
        print(f"First Name: {fname}")
        print(f"Middle Name: {mname}")
        print(f"Last Name: {lname}")


fname = input("Enter First Name: ")
mname = input("Enter Middle Name: ")
lname = input("Enter Last Name: ")

obj = ClassWithMoreFunction()
obj.userInformation(fname, mname, lname)  