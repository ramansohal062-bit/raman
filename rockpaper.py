from tkinter import *
import random

root=Tk()
root.title("Rock Paper Scissor Game")
root.configure(bg="light blue")
root.geometry("400x400")

choices=["Rock","Paper","Scissors"]

user_label=Label(root, text="Your choice:", font=("Arial", 14))
user_label.pack(pady=10)

computer_label=Label(root,text="Computer choice:", font=("Arial", 14))
computer_label.pack(pady=10)

result_label=Label(root, text="Result:", font=("Arial", 16))
result_label.pack(pady=20)

def play(user_choice):
    computer=random.choice(choices)
    user_label.configure(text="Your choice:"+ user_choice)
    computer_label.configure(text="Computer choice:"+ computer)

    if user_choice==computer:
        result="Draw"
    elif (user_choice=="Rock" and computer=="Scissors")or(user_choice=="Paper" and computer=="Rock")or(user_choice=="Scissors" and computer=="Paper"):
        result="You Win!"
    else:
        result="Computer Wins!"
    result_label.configure(text="Result:"+result)
def reset():
    user_label.configure(text="Your choice:")
    computer_label.configure(text="Computer choice:")
    result_label.configure(text="Result:")

Button(root, text="Rock",width=10, command=lambda:play("Rock"), bg="red", fg="white").pack(pady=5)
Button(root, text="Paper",width=10, command=lambda:play("Paper"), bg="red", fg="white").pack(pady=5)
Button(root, text="Scissors",width=10, command=lambda:play("Scissors"), bg="red", fg="white").pack(pady=5)

Button(root, text="Reset", command="reset", bg="green", fg="white").pack(pady=20)
    
root.mainloop()