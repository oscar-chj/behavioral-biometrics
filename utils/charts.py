"""
Charts Generator.

Creates charts for typing performance metrics.
"""

import matplotlib.pyplot as plt

def show_wpm_chart(wpm):
    """Show a WPM bar chart."""
    plt.bar(["WPM"], [wpm])
    plt.title("Words Per Minute")
    plt.show()

def show_accuracy_chart(accuracy):
    """Show an Accuracy bar chart."""
    plt.bar(["Accuracy"], [accuracy])
    plt.title("Typing Accuracy")
    plt.show()
