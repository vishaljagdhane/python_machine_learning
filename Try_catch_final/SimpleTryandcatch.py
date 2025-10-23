# ------------------------------------------
# Program: Try and Except Example in Python
# Purpose: To handle runtime errors gracefully
# ------------------------------------------

print("Try and Except Program")  # Initial message

# Why we use try and except:
# --------------------------
# Sometimes our program may cause an error (e.g., dividing by zero, invalid input, etc.)
# Instead of crashing the program, we can use 'try' and 'except'
# to handle the error smoothly and show a user-friendly message.

# Program structure:
# ------------------
# try:
#     (code that might cause an error)
# except ExceptionType:
#     (code that runs if there is an error)
# finally:   --> (optional)
#     (code that always runs, whether error occurs or not)

# Example program:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result =", result)

# If division by zero happens, handle it here
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")

# If user enters invalid (non-numeric) input
except ValueError:
    print("Error: Please enter valid numbers only.")

# General exception handler (for any other type of error)
except Exception as e:
    print("An unexpected error occurred:", e)

# This block will always run whether there is an error or not
finally:
    print("Program execution completed.")
