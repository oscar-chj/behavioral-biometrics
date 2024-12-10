import json
import numpy as np

# Save typing profile to file
def save_profile(filename, profile):
    with open(filename, "w") as f:
        json.dump(profile, f)

# Load typing profile from file
def load_profile(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Preprocess typing data
def preprocess_data(raw_data):
    key_durations = [item["time"] for item in raw_data]
    return {
        "key_durations": key_durations,
        "heatmap": calculate_heatmap(raw_data)
    }

# Calculate heatmap data
def calculate_heatmap(raw_data):
    heatmap = {}
    for item in raw_data:
        key = item["key"]
        if key not in heatmap:
            heatmap[key] = 0
        heatmap[key] += 1
    return heatmap

# Normalize data for model input
def normalize_data(key_durations):
    key_durations = np.array(key_durations)
    return (key_durations - key_durations.mean()) / key_durations.std()
