import userRecord
print("This Main File — Showing All Modules")

# Take user input
user_first = input("Please enter your first name: ")
user_last = input("Please enter your last name: ")
user_mobile = input("Please enter your mobile number: ")
user_pan = input("Please enter your PAN number: ")
user_email = input("Please enter your email address: ")
user_address = input("Please enter your address: ")
userRecord.show_user_info(user_first, user_last, user_mobile, user_pan, user_email, user_address)