# ------------------------------------------
# Program: Simple Calculator using Tkinter
# ------------------------------------------

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("600x600")

# Entry widget to display the input/output
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the screen
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the result
def calculate():
    try:
        result = eval(entry.get())  # evaluate expression safely
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

# Run the main loop
root.mainloop()
