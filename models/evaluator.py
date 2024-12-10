"""
Evaluator for typing performance and similarity metrics.

This module calculates a variety of metrics, including:
- Typing performance: WPM, accuracy, error rate, key latency, backspace rate.
- Similarity metrics: Cosine similarity, Euclidean distance, reconstruction error, and more.

These metrics are useful for performance tracking and anomaly detection.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean


def calculate_wpm(word_count, elapsed_time):
    """
    Calculate Words Per Minute (WPM).

    :param word_count: Number of words typed.
    :param elapsed_time: Time taken in seconds.
    :return: Words per minute.
    """
    return (word_count / elapsed_time) * 60


def calculate_cpm(char_count, elapsed_time):
    """
    Calculate Characters Per Minute (CPM).

    :param char_count: Number of characters typed.
    :param elapsed_time: Time taken in seconds.
    :return: Characters per minute.
    """
    return (char_count / elapsed_time) * 60


def calculate_accuracy(typed, expected):
    """
    Calculate typing accuracy as a percentage.

    :param typed: The string typed by the user.
    :param expected: The reference string.
    :return: Accuracy percentage.
    """
    correct_chars = sum(1 for a, b in zip(typed, expected) if a == b)
    return (correct_chars / len(expected)) * 100


def calculate_error_rate(typed, expected):
    """
    Calculate the typing error rate as a percentage.

    :param typed: The string typed by the user.
    :param expected: The reference string.
    :return: Error rate percentage.
    """
    incorrect_chars = sum(1 for a, b in zip(typed, expected) if a != b)
    return (incorrect_chars / len(expected)) * 100


def calculate_key_latency(key_times):
    """
    Calculate the average inter-key latency (time between consecutive keypresses).

    :param key_times: List of timestamps for keypress events.
    :return: Average latency between keypresses in seconds.
    """
    if len(key_times) < 2:
        return 0
    latencies = [key_times[i] - key_times[i - 1] for i in range(1, len(key_times))]
    return np.mean(latencies)


def calculate_backspace_rate(typed):
    """
    Calculate the percentage of backspace key usage during typing.

    :param typed: String representing the sequence of keys typed (including backspaces).
    :return: Percentage of backspaces used.
    """
    backspaces = typed.count('\b')
    total_keys = len(typed)
    return (backspaces / total_keys) * 100 if total_keys > 0 else 0


def calculate_cosine_similarity(profile_a, profile_b):
    """
    Calculate the cosine similarity between two typing profiles.

    :param profile_a: List or vector of typing data (e.g., key latencies, heatmap frequencies).
    :param profile_b: List or vector of typing data.
    :return: Cosine similarity (value between -1 and 1).
    """
    profile_a = np.array(profile_a).reshape(1, -1)
    profile_b = np.array(profile_b).reshape(1, -1)
    return cosine_similarity(profile_a, profile_b)[0][0]


def calculate_euclidean_distance(profile_a, profile_b):
    """
    Calculate the Euclidean distance between two typing profiles.

    :param profile_a: List or vector of typing data.
    :param profile_b: List or vector of typing data.
    :return: Euclidean distance (value >= 0).
    """
    return euclidean(profile_a, profile_b)


def calculate_reconstruction_error(original, reconstructed):
    """
    Calculate the reconstruction error (mean squared error) between two datasets.

    :param original: Original dataset (e.g., typing data).
    :param reconstructed: Reconstructed dataset from an autoencoder.
    :return: Reconstruction error (MSE).
    """
    original = np.array(original)
    reconstructed = np.array(reconstructed)
    return np.mean((original - reconstructed) ** 2)


def calculate_typing_consistency(key_times):
    """
    Calculate typing consistency as the standard deviation of inter-key latencies.

    :param key_times: List of timestamps for keypress events.
    :return: Standard deviation of latencies in seconds.
    """
    if len(key_times) < 2:
        return 0
    latencies = [key_times[i] - key_times[i - 1] for i in range(1, len(key_times))]
    return np.std(latencies)


def calculate_heatmap_similarity(heatmap_a, heatmap_b):
    """
    Calculate the similarity between two keyboard heatmaps using cosine similarity.

    :param heatmap_a: Dictionary of key frequencies for profile A.
    :param heatmap_b: Dictionary of key frequencies for profile B.
    :return: Cosine similarity score (value between -1 and 1).
    """
    keys = set(heatmap_a.keys()).union(set(heatmap_b.keys()))
    vector_a = [heatmap_a.get(key, 0) for key in keys]
    vector_b = [heatmap_b.get(key, 0) for key in keys]
    return calculate_cosine_similarity(vector_a, vector_b)


def calculate_typing_fatigue(latencies):
    """
    Measure typing fatigue by identifying increasing trends in inter-key latencies.

    :param latencies: List of inter-key latencies.
    :return: Fatigue score (percentage of increasing latency events).
    """
    if len(latencies) < 2:
        return 0
    fatigue_events = sum(1 for i in range(1, len(latencies)) if latencies[i] > latencies[i - 1])
    return (fatigue_events / len(latencies)) * 100
