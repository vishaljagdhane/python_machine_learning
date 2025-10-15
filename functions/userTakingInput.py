# Program: Taking user input and displaying all details at once
# Author: [Your Name]
# Date: [Add Date]
# Description:
# This script demonstrates how to take user input using multiple functions,
# return the data from each, and finally display all collected details together.

print("Taking user input example.")

# --- Function 1: Collect Basic Details ---
def basicDetails():
    # Ask user for name and age
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    # Return both values as a tuple
    return name, age

# --- Function 2: Collect Education Details ---
def educationDetails():
    # Ask user for school and grade
    school = input("Enter your school name: ")
    grade = input("Enter your grade: ")
    # Return both values
    return school, grade

# --- Function 3: Collect Address Details ---
def address():
    # Ask user for city and country
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    # Return both values
    return city, country

# --- Main Program Execution ---

# Call each function and store the returned values
name, age = basicDetails()
school, grade = educationDetails()
city, country = address()

# Final Output - Display all collected details together
print("\n----- Your Full Details -----")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"School  : {school}")
print(f"Grade   : {grade}")
print(f"City    : {city}")
print(f"Country : {country}")
print("-----------------------------")
