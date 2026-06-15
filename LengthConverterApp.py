from tkinter import *

# Function to convert inches to centimeters
def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text="Length in cm = " + str(cm))

# Create window
root = Tk()
root.title("Inches to CM Converter")

# Label
Label(root, text="Enter Length in Inches").pack()

# Entry box
entry = Entry(root)
entry.pack()

# Button
Button(root, text="Convert", command=convert).pack()

# Result label
result = Label(root, text="")
result.pack()

# Run the window
root.mainloop()
