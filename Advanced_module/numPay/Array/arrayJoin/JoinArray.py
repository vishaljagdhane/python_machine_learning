import numpy as np 
array1= np.array(['Vishal','Haribahu','jagdhane'])
array2= np.array(['Plot 39,Neharu Nagar','Ranjagaon SP','Auranagabad'])
mergeArray = np.concatenate((array1,array2))
print (mergeArray)
# result= np.char.join( ' - ', (array1,array2))
# print (result)
for x in mergeArray:
    print (x)