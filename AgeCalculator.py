from tkinter import *

# Function to calculate age
def find_age():
    birth_year = int(entry.get())
    age = 2026 - birth_year
    result.config(text="Your Age is: " + str(age))

# Create window
root = Tk()
root.title("Age Calculator")
root.geometry("300x150")

# Label
Label(root, text="Enter Your Birth Year").pack()

# Entry box
entry = Entry(root)
entry.pack()

# Button
Button(root, text="Calculate Age", command=find_age).pack()

# Result label
result = Label(root, text="")
result.pack()

# Run window
root.mainloop()