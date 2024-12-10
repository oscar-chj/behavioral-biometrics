"""
Data Manager.

Handles saving and loading user profiles and typing results.
"""

import json
from datetime import datetime


def save_typing_result(wpm, accuracy, error_rate, avg_latency, backspace_rate, consistency, fatigue):
    """
    Save typing test results to the results.json file.

    :param wpm: Words per minute.
    :param accuracy: Accuracy percentage.
    :param error_rate: Error rate percentage.
    :param avg_latency: Average key latency (seconds).
    :param backspace_rate: Backspace usage rate percentage.
    :param consistency: Typing consistency (standard deviation of latencies).
    :param fatigue: Typing fatigue percentage.
    """
    result = {
        "timestamp": datetime.now().isoformat(),
        "wpm": wpm,
        "accuracy": accuracy,
        "error_rate": error_rate,
        "avg_latency": avg_latency,
        "backspace_rate": backspace_rate,
        "consistency": consistency,
        "fatigue": fatigue,
    }

    try:
        # Load existing results
        with open("data/results.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is invalid, initialize an empty list
        data = {"tests": []}

    # Append the new result
    data["tests"].append(result)

    # Save updated results back to the file
    with open("data/results.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Typing result saved successfully!")
