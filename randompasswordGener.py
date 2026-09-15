import tkinter as tk
import random
import string

# Create window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x250")

# Create a frame
frame = tk.Frame(window)
frame.pack(pady=20)

# Label
label = tk.Label(frame, text="Your Password:")
label.pack()

# Entry box
entry = tk.Entry(frame, width=30)
entry.pack(pady=10)

# Function to generate password
def generate_password():
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(8):
        password += random.choice(characters)

    entry.delete(0, tk.END)
    entry.insert(0, password)

# Button
button = tk.Button(
    frame,
    text="Generate Password",
    command=generate_password
)
button.pack()

# Run the program
window.mainloop()