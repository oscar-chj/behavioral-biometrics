"""
Heatmap Generator.

This module generates a heatmap of keypress frequencies for typing tests.
"""

import matplotlib.pyplot as plt
import numpy as np

def generate_keyboard_heatmap(key_frequencies):
    """
    Generate a keyboard heatmap based on key frequencies.

    :param key_frequencies: Dictionary with keys as characters and values as frequencies.
    """
    # Define the keyboard layout
    keyboard = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["Z", "X", "C", "V", "B", "N", "M"]
    ]

    # Create a matrix to store frequencies
    frequency_matrix = []
    for row in keyboard:
        row_frequencies = [key_frequencies.get(key.lower(), 0) for key in row]
        frequency_matrix.append(row_frequencies)

    # Convert to numpy array for plotting
    frequency_matrix = np.array(frequency_matrix)

    # Plot the heatmap
    plt.figure(figsize=(10, 5))
    plt.imshow(frequency_matrix, cmap="YlOrRd", interpolation="nearest")
    plt.colorbar(label="Frequency")
    plt.title("Keyboard Heatmap")
    
    # Add key labels
    for i, row in enumerate(keyboard):
        for j, key in enumerate(row):
            plt.text(j, i, key, ha="center", va="center", color="black")

    plt.xticks(range(len(keyboard[0])), [""] * len(keyboard[0]))  # Hide tick marks
    plt.yticks(range(len(keyboard)), [""] * len(keyboard))       # Hide tick marks

    plt.tight_layout()
    plt.show()
