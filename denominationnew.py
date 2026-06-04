from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root= Tk()
root.title("Denomination calculator")
root.geometry("400x400")
root.configure(bg="light blue")
def calculate():
    try:
    amount=int(entry.get())
    note2000=amount//2000
    amount=amount%2000
    note500=amount//500
    amount=amount%500
    note100=amount//100
    result1.config(text="2000 Notes: "+str(note2000))
    result2.config(text="500 Notes: "+str(note500))
    result3.config(text="100 Notes: "+str(note100))
    except:
img=Image.open("denomination.jpg")
img=img.resize((150,100))
photo=ImageTk.PhotoImage(img)
label_img=Label(root,image=photo,bg="light blue")
label_img.image=photo
label_img.pack(pady=10)
heading=Label(root,text="denomination calculator",font=("Arial",16,"bold"),bg="light blue")
heading.pack(pady=10)
entry=Entry(root,font=("Arial",14,))
btn=Button(root,text="calculate",command=calculate,bg="green",fg="white")
btn.pack(pady=10)
result1=Label(root,text="",font=("Arial",12),bg="light blue")
result1.pack()
result2=Label(root,text="",font=("Arial",12),bg="light blue")
result2.pack()
result3=Label(root,text="",font=("Arial",12),bg="light blue")
result3.pack()
root.mainloop()