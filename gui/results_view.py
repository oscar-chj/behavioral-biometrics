"""
Results View.

This module generates the results view, including WPM and Accuracy charts.
"""

import tkinter as tk
from utils.charts import show_wpm_chart, show_accuracy_chart

class ResultsView:
    def __init__(self, wpm, accuracy):
        self.wpm = wpm
        self.accuracy = accuracy

    def display_results(self):
        """Display WPM and Accuracy charts."""
        show_wpm_chart(self.wpm)
        show_accuracy_chart(self.accuracy)
