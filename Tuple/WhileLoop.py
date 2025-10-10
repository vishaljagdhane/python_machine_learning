print("Tuple Using While Loop")  
# Print a heading to indicate the start of tuple iteration using a while loop

While_loop_Tuple = (10, 20, 30, 40, 50)  
# Define a tuple with 5 integer elements; tuples are immutable collections

i = 0  
# Initialize index variable i to 0; used to access tuple elements by position

while i < len(While_loop_Tuple):  
    # Loop while i is less than the length of the tuple (which is 5)
    # Using len() ensures we don’t access indexes outside the tuple, avoiding errors

    print(While_loop_Tuple[i])  
    # Print the element at the current index i

    i += 1  
    # Increment i by 1 to move to the next element in the next loop iteration

print("End of an Application")  
# After the loop finishes, print this message to indicate the program finished iterating

print("--------------------------------------------------")  
# Print a separator line for clarity between sections of output


# Second while loop starts here
while i < 3:  
    # Loop while i is less than 3
    # Note: 'i' is currently 5 after the first loop, so this loop **will not run** because 5 < 3 is False

    print(While_loop_Tuple)  
    # Print the entire tuple (not individual elements) during each iteration of the loop

    i += 1  
    # Increment i by 1 (though this won't be executed in this case since loop doesn't run)

print("End of an Application")  
# Print message indicating the end of the second loop/application
