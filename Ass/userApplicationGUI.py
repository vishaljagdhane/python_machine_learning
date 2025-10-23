import tkinter as tk
import json

# Create main window
root = tk.Tk()
root.title("User Store Record System")
root.geometry("800x800")
root.configure(bg="#e3f2fd")  # light blue background

# -------------------------------
# Header Label
# -------------------------------
title_label = tk.Label(root, text="User Information Form", font=("Arial", 24, "bold"), bg="#e3f2fd", fg="#0d47a1")
title_label.pack(pady=20)

# -------------------------------
# Form Labels and Entry Fields
# -------------------------------
form_frame = tk.Frame(root, bg="#e3f2fd")
form_frame.pack(pady=10)

tk.Label(form_frame, text="First Name:", font=("Arial", 16), bg="#e3f2fd").grid(row=0, column=0, sticky="e", pady=5, padx=10)
fname_entry = tk.Entry(form_frame, font=("Arial", 16), width=25)
fname_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Last Name:", font=("Arial", 16), bg="#e3f2fd").grid(row=1, column=0, sticky="e", pady=5, padx=10)
lname_entry = tk.Entry(form_frame, font=("Arial", 16), width=25)
lname_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Mobile Number:", font=("Arial", 16), bg="#e3f2fd").grid(row=2, column=0, sticky="e", pady=5, padx=10)
mobile_entry = tk.Entry(form_frame, font=("Arial", 16), width=25)
mobile_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Email Address:", font=("Arial", 16), bg="#e3f2fd").grid(row=3, column=0, sticky="e", pady=5, padx=10)
email_entry = tk.Entry(form_frame, font=("Arial", 16), width=25)
email_entry.grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="Address:", font=("Arial", 16), bg="#e3f2fd").grid(row=4, column=0, sticky="e", pady=5, padx=10)
address_entry = tk.Entry(form_frame, font=("Arial", 16), width=25)
address_entry.grid(row=4, column=1, pady=5)

# -------------------------------
# Save Function
# -------------------------------
def save_info():
    user_data = {
        "First Name": fname_entry.get(),
        "Last Name": lname_entry.get(),
        "Mobile": mobile_entry.get(),
        "Email": email_entry.get(),
        "Address": address_entry.get()
    }

    # Save to JSON file
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

    # Show success message
    success_label.config(text="✅ User information saved successfully!", fg="green")

    # Clear the form fields
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# -------------------------------
# Buttons
# -------------------------------
btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=20)

save_btn = tk.Button(btn_frame, text="Save Info", font=("Arial", 16), bg="#64b5f6", fg="white", width=12, command=save_info)
save_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", font=("Arial", 16), bg="#ef5350", fg="white", width=12, command=root.destroy)
exit_btn.grid(row=0, column=1, padx=10)

# Success Message Label
success_label = tk.Label(root, text="", font=("Arial", 14), bg="#e3f2fd")
success_label.pack()

# -------------------------------
# Run the main loop
# -------------------------------
root.mainloop()
