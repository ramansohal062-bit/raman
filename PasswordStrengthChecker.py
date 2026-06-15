from tkinter import *

# Function to check password strength
def check_password():
    password = password_entry.get()
    length = len(password)

    if length < 5:
        result_label.config(text="Weak Password")
    elif length < 8:
        result_label.config(text="Medium Password")
    else:
        result_label.config(text="Strong Password")

# Create window
root = Tk()
root.title("Password Strength Checker")

# Labels and Entry
Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)

password_entry = Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Button
Button(root, text="Check Strength", command=check_password).grid(
    row=1, column=0, columnspan=2, pady=10
)

# Result Label
result_label = Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()