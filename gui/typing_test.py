"""
Typing Test GUI.

This module creates the interface for users to complete a typing test.
It includes sentence selection, typing input, a timer, and live stats.
"""

import tkinter as tk
from time import time
from gui.base_theme import BaseTheme  # Import BaseTheme
from models.evaluator import (
    calculate_wpm,
    calculate_accuracy,
    calculate_error_rate,
    calculate_key_latency,
    calculate_backspace_rate,
    calculate_typing_consistency,
    calculate_typing_fatigue
)
from utils.heatmap import generate_keyboard_heatmap
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
        elapsed_time = self.end_time - self.start_time
        user_input = self.user_input
        phrase = self.phrase

        # Performance Metrics
        wpm = calculate_wpm(len(user_input.split()), elapsed_time)
        accuracy = calculate_accuracy(user_input, phrase)
        error_rate = calculate_error_rate(user_input, phrase)
        latencies = [self.typing_data[i]["time"] - self.typing_data[i - 1]["time"] for i in range(1, len(self.typing_data))]
        avg_latency = calculate_key_latency(latencies)
        backspace_rate = calculate_backspace_rate(user_input)
        consistency = calculate_typing_consistency(latencies)
        fatigue = calculate_typing_fatigue(latencies)

        # Save results and visualize
        save_typing_result(wpm, accuracy, error_rate, avg_latency, backspace_rate, consistency, fatigue)

        # Generate Heatmap
        key_frequencies = {}
        for char in user_input:
            key_frequencies[char.lower()] = key_frequencies.get(char.lower(), 0) + 1
        generate_keyboard_heatmap(key_frequencies)

        # Print metrics for debugging
        print(f"WPM: {wpm}")
        print(f"Accuracy: {accuracy}%")
        print(f"Error Rate: {error_rate}%")
        print(f"Average Latency: {avg_latency}s")
        print(f"Backspace Rate: {backspace_rate}%")
        print(f"Consistency (Latency Std Dev): {consistency}s")
        print(f"Fatigue: {fatigue}%")

        # Visualize results
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
