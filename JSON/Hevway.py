# Import JSON module
import json

# Create a Python dictionary (key–value pairs)
json_file = {
    "fname": "Vishal",
    "mname": "Haribhau",
    "lastName": "Jagdhane",
    "mobile": 8983780269,
    "email": "vishal.jagdhane87@gmail.com",
    "Address": "Aurangabad",
}

# Convert Python dictionary to JSON string
# dumps() = "dump string" → converts dict → JSON format
y = json.dumps(json_file)

# Print full JSON data
print("Full JSON data:", y)

# ----------------------------------------------
# 🧠 Accessing single values from the dictionary
# ----------------------------------------------

# You can print any single value directly using its key
print("First Name:", json_file["fname"])
print("Middle Name:", json_file["mname"])
print("Last Name:", json_file["lastName"])
print("Mobile Number:", json_file["mobile"])
print("Email ID:", json_file["email"])
print("Address:", json_file["Address"])

# ----------------------------------------------
# 🧩 Convert JSON string back to dictionary
# ----------------------------------------------

# loads() = "load string" → converts JSON string → Python dict
data = json.loads(y)

print("\nAfter converting back from JSON string:")
print("First Name:", data["fname"])
print("Email:", data["email"])
