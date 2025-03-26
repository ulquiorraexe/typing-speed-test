import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.words = ["apple", "banana", "cherry", "grape", "orange", "pear", "watermelon", "kiwi", "pineapple", "strawberry"]
        self.current_word = tk.StringVar()
        self.user_input = tk.StringVar()
        self.result_label = tk.Label(self.root, text="", font=("Arial", 18))

        self.setup_ui()

    def setup_ui(self):
        self.current_word.set(random.choice(self.words))
        self.word_label = tk.Label(self.root, textvariable=self.current_word, font=("Arial", 24))
        self.word_label.pack(pady=50)

        self.input_entry = tk.Entry(self.root, textvariable=self.user_input, font=("Arial", 18))
        self.input_entry.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test, font=("Arial", 16))
        self.start_button.pack(pady=20)

        self.result_label.pack(pady=20)

    def start_test(self):
        self.start_time = time.time()
        self.input_entry.config(state="normal")
        self.input_entry.focus()
        self.start_button.config(state="disabled")
        self.input_entry.bind("<Return>", self.check_input)

    def check_input(self, event):
        user_text = self.user_input.get().strip()
        if user_text == self.current_word.get():
            elapsed_time = round(time.time() - self.start_time, 2)
            words_per_minute = round((len(user_text.split()) / elapsed_time) * 60)
            self.result_label.config(text=f"Words Per Minute: {words_per_minute}", fg="green")
        else:
            self.result_label.config(text="Incorrect! Try again.", fg="red")

        self.current_word.set(random.choice(self.words))
        self.user_input.set("")
        self.input_entry.focus()

def main():
    root = tk.Tk()
    typing_test = TypingSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
