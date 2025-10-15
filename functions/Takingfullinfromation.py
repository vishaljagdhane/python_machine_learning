# print("Taking user input example.")
# def user_info(name, mobile, city):
#     return name, mobile, city
# name = input("Enter your name: ")
# mobile = input("Enter your mobile number: ")    
# city = input("Enter your city: ")
# print(user_info(name, mobile, city))
# print("User information taken successfully.")
print("Taking user input example.")

# Function to collect and return 20 fields
def user_info(name, mobile, city, age, gender, email, country, state, zipcode, address,
              education, college, course, grade, blood_group, height, weight, dob, nationality, language):
    
    return name, mobile, city, age, gender, email, country, state, zipcode, address, \
           education, college, course, grade, blood_group, height, weight, dob, nationality, language

# --- Taking inputs from the user ---
name = input("Enter your name: ")
mobile = input("Enter your mobile number: ")
city = input("Enter your city: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
email = input("Enter your email: ")
country = input("Enter your country: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")
address = input("Enter your full address: ")
education = input("Enter your highest education: ")
college = input("Enter your college name: ")
course = input("Enter your course name: ")
grade = input("Enter your grade or percentage: ")
blood_group = input("Enter your blood group: ")
height = input("Enter your height (in cm): ")
weight = input("Enter your weight (in kg): ")
dob = input("Enter your date of birth (DD/MM/YYYY): ")
nationality = input("Enter your nationality: ")
language = input("Enter your preferred language: ")

# --- Call the function and store result ---
user_data = user_info(name, mobile, city, age, gender, email, country, state, zipcode, address,
                      education, college, course, grade, blood_group, height, weight, dob, nationality, language)

# --- Discplay the information clearly ---
print("\n User Information Collected Successfully:\n")
labels = ["Name", "Mobile", "City", "Age", "Gender", "Email", "Country", "State", "Zipcode", "Address",
          "Education", "College", "Course", "Grade", "Blood Group", "Height", "Weight", "Date of Birth", "Nationality", "Language"]

for label, value in zip(labels, user_data):
    print(f"{label:15}: {value}")

