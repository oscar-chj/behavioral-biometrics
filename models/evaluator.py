"""
Evaluator for typing performance metrics.

This module calculates Words Per Minute (WPM) and accuracy.
"""

def calculate_wpm(word_count, elapsed_time):
    """Calculate Words Per Minute."""
    return (word_count / elapsed_time) * 60

def calculate_accuracy(typed, expected):
    """Calculate typing accuracy."""
    correct_chars = sum(1 for a, b in zip(typed, expected) if a == b)
    return (correct_chars / len(expected)) * 100
