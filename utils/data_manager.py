"""
Data Manager.

Handles saving and loading user profiles and typing results.
"""

import json

def save_typing_result(wpm, accuracy):
    """Save typing test results."""
    result = {"wpm": wpm, "accuracy": accuracy}
    with open("data/results.json", "r+") as f:
        data = json.load(f)
        data["tests"].append(result)
        f.seek(0)
        json.dump(data, f)
