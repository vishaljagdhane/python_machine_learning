print("cunstructors and self")
class person:
    def __init__(self):
        pass
    def personDetails(self,name,age):
        self.name=name
        self.age=age
        print("Name is ",self.name)
        print("Age is ",self.age)
p1=person()
p1.personDetails("John",36)
p2=person()
p2.personDetails("Doe",25)
#A class is like a blueprint or template to create objects.