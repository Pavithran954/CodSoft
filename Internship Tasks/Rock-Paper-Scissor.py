import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("350x350")

        self.user_choice = None
        self.computer_choice = None
        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.create_button("Rock")
        self.create_button("Paper")
        self.create_button("Scissors")

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def create_button(self, choice):
        button = tk.Button(self.buttons_frame, text=choice, command=lambda: self.play(choice))
        button.pack(side=tk.LEFT, padx=5)

    def play(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        result = self.determine_winner()

        self.result_label.config(text="User: {}   Computer: {}".format(self.user_choice, self.computer_choice))

        if result == "Win":
            self.user_score += 1
        elif result == "Lose":
            self.computer_score += 1

        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "Tie"
        elif ((self.user_choice == "Rock" and self.computer_choice == "Scissors") or
            (self.user_choice == "Paper" and self.computer_choice == "Rock") or
            (self.user_choice == "Scissors" and self.computer_choice == "Paper")):
            return "Win"
        else:
            return "Lose"

    def play_again(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)

    #icon
    Image_icon=PhotoImage(file="rps.png")
    root.iconphoto(False,Image_icon)
    
    root.mainloop()