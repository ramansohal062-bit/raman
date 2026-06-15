from tkinter import *
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text="Computer: " + computer_choice + "\n" + result
    )

# Create window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x250")

# Heading
Label(root, text="Choose One", font=("Arial", 14)).pack(pady=10)

# Buttons
Button(root, text="Rock", width=10,
       command=lambda: play("Rock")).pack(pady=5)

Button(root, text="Paper", width=10,
       command=lambda: play("Paper")).pack(pady=5)

Button(root, text="Scissors", width=10,
       command=lambda: play("Scissors")).pack(pady=5)

# Result Label
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()