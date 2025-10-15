print("Using while loop with break statement in python")
print("Break statement is used to exit the loop when a certain condition is met.")
print("Syntax of while loop with break statement in python")
a = 1  # Initialize a variable
while a <= 10:  # Condition to check to continue the loop
    print("This is a while loop iteration:", a)  # Print statement
    if a == 5:  # Condition to check for break
        print("Breaking the loop as a is equal to 5")
        break  # Exit the loop when a is equal to 5
    a = a + 1  # Increment the value of a by 1 before next check