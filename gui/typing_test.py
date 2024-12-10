"""
Typing Test GUI.

This module creates the interface for users to complete a typing test.
It includes sentence selection, typing input, a timer, and live stats.
"""

import tkinter as tk
from time import time
from gui.base_theme import BaseTheme  # Import BaseTheme
from utils.data_manager import save_typing_result
from utils.charts import show_wpm_chart, show_accuracy_chart

class TypingTestGUI:
    def __init__(self):
        self.typing_data = []
        self.start_time = None
        self.end_time = None
        self.phrase = "The quick brown fox jumps over the lazy dog."
        self.user_input = ""

    def start_timer(self):
        """Start the timer when typing begins."""
        if self.start_time is None:
            self.start_time = time()

    def calculate_wpm(self):
        """Calculate Words Per Minute (WPM)."""
        elapsed_time = self.end_time - self.start_time
        word_count = len(self.user_input.split())
        return (word_count / elapsed_time) * 60

    def calculate_accuracy(self):
        """Calculate typing accuracy."""
        correct_chars = sum(1 for a, b in zip(self.phrase, self.user_input) if a == b)
        return (correct_chars / len(self.phrase)) * 100

    def on_typing_complete(self):
        """Handle the completion of the typing test."""
        self.end_time = time()
        wpm = self.calculate_wpm()
        accuracy = self.calculate_accuracy()
        save_typing_result(wpm, accuracy)
        show_wpm_chart(wpm)
        show_accuracy_chart(accuracy)

    def start(self):
        """Start the Typing Test GUI."""
        root = tk.Tk()
        root.title("Typing Test")

        # Styling
        theme = BaseTheme().get_styles()  # Initialize the theme
        root.configure(bg=theme["background"])

        # Instruction Label
        instruction = tk.Label(root, text="Type the phrase below:", bg=theme["background"], fg=theme["text"], font=theme["font"])
        instruction.pack(pady=10)

        # Display Phrase
        phrase_label = tk.Label(root, text=self.phrase, bg=theme["background"], fg=theme["accent"], font=theme["font"])
        phrase_label.pack(pady=10)

        # Typing Entry
        entry = tk.Entry(root, font=theme["font"], width=50)
        entry.pack(pady=10)
        entry.bind("<KeyPress>", lambda _: self.start_timer())
        entry.bind("<KeyRelease>", lambda _: setattr(self, "user_input", entry.get()))

        # Submit Button
        submit_button = tk.Button(root, text="Submit", bg=theme["accent"], command=lambda: [self.on_typing_complete(), root.destroy()])
        submit_button.pack(pady=20)

        root.mainloop()
