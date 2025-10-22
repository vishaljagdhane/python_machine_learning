#A class is like a blueprint or template to create objects.
#It groups related data (variables) and behavior (functions/methods) together.
#Useful when you want to create multiple objects with similar structure.

class LearningOop:
    def learningClassMethod(self,multipleData,):
        name = str(input("Enter Your full name "))
        print("Learning OOP is fun " + name, multipleData)

#Creating an object of the class
obj = LearningOop()
obj.learningClassMethod(multipleData="I love Python")