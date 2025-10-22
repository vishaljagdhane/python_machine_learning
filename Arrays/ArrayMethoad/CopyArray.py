print("Copy Array Method")
collection_record = ['LaxmiAai', 'RenukaAai', 'HarHar_Mahadev', 'Ganpati_Bappa', 'Sai_Baba', 'Jijus']

for x in collection_record:
    print(x)
copyArray = collection_record.copy()
print("After copay",copyArray)
# copy to single Array 
# copySingleArray = collection_record.copy()
copy_whole_by_slice = collection_record[:]     # full copy using slice
copy_part = collection_record[0:4]             # elements index 0,1,2,3
print("copy_whole_by_slice:", copy_whole_by_slice)
print("copy_part (0:4):", copy_part)