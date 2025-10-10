# TupleMultiple_Data =("Vishal","haribhau","Jagdhane","Aurangbad")
# print(TupleMultiple_Data)
# adding_TupleData = list(TupleMultiple_Data)
# adding_TupleData.append("Pune")
# TupleMultiple_Data = tuple(adding_TupleData)
# print(TupleMultiple_Data)


# Try to self logic and understand 
# Tuple are immutable but we can convert into list and add new data and again convert into tuple
# This is called as appending the data in tuple
# Tuple are immutable but we can convert into list and add new data and again convert into tuple
# This is called as appending the data in tuple
TrySelfTupleDataLogic = ("Pooja","Vishal","Jagdhane","Aurangbad ")
adding_TupleMoreValue = list(TrySelfTupleDataLogic)
adding_TupleMoreValue.append("Pune")
TrySelfTupleDataLogic = tuple(adding_TupleMoreValue)
print(TrySelfTupleDataLogic)
print(type(TrySelfTupleDataLogic))
print(len(TrySelfTupleDataLogic))
print(TrySelfTupleDataLogic[0:8:2])