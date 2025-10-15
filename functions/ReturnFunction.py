print("This is a simple for return function example.")

# Function to add two numbers and return the result
print("Why use return function? Because it helps return values from a function to use them later in the program.")

def addNumbers(num1, num2):  # Define function with two inputs
    result = num1 + num2     # Add the two numbers
    return result            # Return the result back

# Call the function and store result
sum_result = addNumbers(40, 60)
print("Addition is:", sum_result)
# Function to calculate sum and difference
def calculate(num1, num2):
    sum_val = num1 + num2
    diff_val = num1 - num2
    return sum_val, diff_val  # Return two values

# Call and store returned values
total, difference = calculate(100, 40)

print("Sum:", total)
print("Difference:", difference)
