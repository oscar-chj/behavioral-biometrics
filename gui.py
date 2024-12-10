import tkinter as tk
from time import time
from utils import save_profile, preprocess_data

class TypingGUI:
    def __init__(self):
        self.typing_data = []
        self.phrase = "The quick brown fox jumps over the lazy dog."
        self.start_time = None

    def record_keypress(self, event):
        if self.start_time is None:
            self.start_time = time()
        key_data = {
            "key": event.char,
            "time": time() - self.start_time
        }
        self.typing_data.append(key_data)
        self.start_time = time()

    def finish_typing(self, is_owner, filename):
        processed_data = preprocess_data(self.typing_data)
        if is_owner:
            save_profile(filename, processed_data)
            print("Owner profile saved.")
        else:
            print("Typing data collected for analysis.")
        self.typing_data = []  # Reset for next session

    def start(self, is_owner, filename):
        self.window = tk.Tk()
        self.window.title("Typing Test")

        instructions = tk.Label(self.window, text="Type the following phrase:")
        instructions.pack()

        display_phrase = tk.Label(self.window, text=self.phrase)
        display_phrase.pack()

        text_entry = tk.Entry(self.window, width=50)
        text_entry.bind("<KeyPress>", self.record_keypress)
        text_entry.pack()

        finish_button = tk.Button(
            self.window,
            text="Finish",
            command=lambda: [self.finish_typing(is_owner, filename), self.window.destroy()]
        )
        finish_button.pack()

        self.window.mainloop()
