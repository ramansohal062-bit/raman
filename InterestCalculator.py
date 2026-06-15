from tkinter import *
from math import pow

# Function to calculate SI and CI
def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    # Simple Interest
    si = (p * r * t) / 100

    # Compound Interest
    amount = p * pow((1 + r / 100), t)
    ci = amount - p

    result_label.config(
        text=f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}"
    )

# Create window
root = Tk()
root.title("SI and CI Calculator")
root.geometry("350x250")

# Labels and Entry Boxes
Label(root, text="Principal Amount").pack()
principal_entry = Entry(root)
principal_entry.pack()

Label(root, text="Rate of Interest (%)").pack()
rate_entry = Entry(root)
rate_entry.pack()

Label(root, text="Time Perio…d (years)").pack()
time_entry = Entry(root)    

time_entry.pack()

# Button
Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack()

root.mainloop()