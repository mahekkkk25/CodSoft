import tkinter as tk
from tkinter import messagebox
import random

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    player_choice = var.get()

    result = check_winner(player_choice, computer_choice)

    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.title("Rock-paper-siccsor game")
window.geometry("925x500+300+200")
window.state("zoomed")
window.configure(bg="white")
       

# Create a label
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:",bg='white',fg='blue',font=('Fort',40,'bold'))
label.place(x=250,y=50)

# Create a radio button for each choice
var = tk.StringVar()
var.set("Rock")

rock_button = tk.Radiobutton(window, text="Rock", variable=var, value="Rock",bg='white',fg='blue',font=('Fort',25,'bold'))
rock_button.place(x=330,y=250)

paper_button = tk.Radiobutton(window, text="Paper", variable=var, value="Paper",bg='white',fg='blue',font=('Fort',25,'bold'))
paper_button.place(x=530,y=250)

scissors_button = tk.Radiobutton(window, text="Scissors", variable=var, value="Scissors",bg='white',fg='blue',font=('Fort',25,'bold'))
scissors_button.place(x=730,y=250)


# Create a button to play the game
play_button = tk.Button(window, text="Play", command=play,bg='white',fg='blue',font=('Fort',25,'bold'))
play_button.place(x=520,y=400,width=200)

# Run the main loop
window.mainloop()
