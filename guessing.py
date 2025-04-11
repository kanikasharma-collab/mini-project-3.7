import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("350x250")
        self.root.configure(bg="grey")

        self.number_to_guess = None
        self.attempts = 0

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()

        self.title_label = tk.Label(self.root, text="Welcome to Number Guessing Game!", bg="grey", font=("Arial", 12))
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, width=15)
        self.start_button.pack()

    def start_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.clear_screen()

        self.label = tk.Label(self.root, text="Guess a number between 1 and 100:", bg="grey")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", bg="grey")
        self.result_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low. Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high. Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.show_play_again()

    def show_play_again(self):
        self.clear_screen()

        congrats = tk.Label(self.root, text=f"🎉 You won in {self.attempts} attempts!", bg="grey", font=("Arial", 12))
        congrats.pack(pady=20)

        play_again_btn = tk.Button(self.root, text="Play Again", command=self.start_game, width=15)
        play_again_btn.pack(pady=5)

        exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit, width=15)
        exit_btn.pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()