print("How remove tuple variable works in python")
Main_Tuple_data =("vishal","Haribhau","jagdhane","Aurangabad")
print("Main Tuple Data is : ",Main_Tuple_data)
# Remove Tuple Variable
print("Remove Single Tuple Variable")
Remove_Tuple_Variable = list(Main_Tuple_data) # Convert Tuple into List
Remove_Tuple_Variable.remove("Aurangabad") # Remove Variable from List
Adding_Tuple_Variable = list(Remove_Tuple_Variable) # Convert List into Tuple
Adding_Tuple_Variable.append("Waluj,MIDC ,Aurangabd") # Add Variable into List
print("After Remove Tuple Variable : ",Remove_Tuple_Variable) # Convert List into Tuple
print("After Adding Tuple Variable : ",Adding_Tuple_Variable)
# Remove_Tuple_variable = Main_Tuple_data[1:3] # It will remove first and last variable from tuple
# print("After Remove Tuple Variable : ",Remove_Tuple_variable)