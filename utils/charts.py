"""
Charts Generator.

Creates visualizations for typing performance metrics.
"""

import matplotlib.pyplot as plt

def show_wpm_chart(wpm):
    """Show a WPM bar chart."""
    plt.bar(["WPM"], [wpm], color="skyblue")
    plt.title("Words Per Minute")
    plt.ylabel("WPM")
    plt.show()

def show_accuracy_chart(accuracy):
    """Show an Accuracy bar chart."""
    plt.bar(["Accuracy"], [accuracy], color="green")
    plt.title("Typing Accuracy")
    plt.ylabel("Percentage")
    plt.show()

def show_error_rate_chart(error_rate):
    """Show an Error Rate bar chart."""
    plt.bar(["Error Rate"], [error_rate], color="red")
    plt.title("Error Rate")
    plt.ylabel("Percentage")
    plt.show()

def show_latency_trend(latencies):
    """Show a line chart of inter-key latencies."""
    plt.plot(latencies, marker="o", color="orange")
    plt.title("Key Latency Trends")
    plt.xlabel("Key Index")
    plt.ylabel("Latency (seconds)")
    plt.grid()
    plt.show()

def show_fatigue_chart(fatigue):
    """Show a bar chart for typing fatigue."""
    plt.bar(["Fatigue"], [fatigue], color="purple")
    plt.title("Typing Fatigue")
    plt.ylabel("Percentage")
    plt.show()
