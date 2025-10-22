# UserModule.py
print("✅ User Module Loaded Successfully")

def show_user_info(first_name, last_name, mobile, pan, email, address):
    """
    Function to display user details
    """
    print("\n----- USER INFORMATION -----")
    print(f"👤 Full Name : {first_name} {last_name}")
    print(f"📱 Mobile    : {mobile}")
    print(f"🪪 PAN       : {pan}")
    print(f"📧 Email     : {email}")
    print(f"🏠 Address   : {address}")
    print("------------------------------")
    print(f"Welcome, {first_name}! 🎉")
