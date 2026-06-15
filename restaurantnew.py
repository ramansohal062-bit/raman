import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Restaurant App")
root.geometry("300x250")


# Function to calculate bill
def place_order():
    total = 0

    fries = int(fries_entry.get() or 0)
    burger = int(burger_entry.get() or 0)
    drinks = int(drinks_entry.get() or 0)

    total += fries * 2
    total += burger * 3
    total += drinks * 1

    messagebox.showinfo("Bill", f"Total Cost = ${total}")

bg_image = Image.open("bill.png")
bg_image = bg_image.resize((100, 150))
bg_photo = ImageTk.PhotoImage(bg_image) 
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo
frames = tk.Frame(root, bg='red', bd=5)
frames.place(relx=0.5, rely=0.5, anchor='center')

# Heading
tk.Label(root, text="Restaurant Menu", font=("Arial", 16)).pack(pady=10)

# Fries
tk.Label(root, text="Fries ($2)").pack()
fries_entry = tk.Entry(root)
fries_entry.pack()

# Burger
tk.Label(root, text="Burger ($3)").pack()
burger_entry = tk.Entry(root)
burger_entry.pack()

# Drinks
tk.Label(root, text="Drinks ($1)").pack()
drinks_entry = tk.Entry(root)
drinks_entry.pack()

# Button
tk.Button(root, text="Place Order", command=place_order).pack(pady=10)

root.mainloop()