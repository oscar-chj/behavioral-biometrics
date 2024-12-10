"""
Debug Script for Autoencoder and Evaluator Modules.

This script is designed to:
1. Test the autoencoder functionality (train, save, load, evaluate).
2. Test evaluator functions (metrics and anomaly detection).
3. Use sample data from `sample_data.json` for debugging.

Run this script to ensure `autoencoder.py` and `evaluator.py` work as intended.
"""

import json
import numpy as np
from autoencoder import train_autoencoder, load_autoencoder, evaluate_anomaly
from evaluator import calculate_cosine_similarity, calculate_reconstruction_error


# Load Sample Dataset
def load_sample_data(file_path="models/sample_data.json"):
    """
    Load sample dataset for testing.

    :param file_path: Path to the sample JSON file.
    :return: Normalized owner and test data as numpy arrays.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    owner_data = np.array(data["owner_data"])
    test_data = np.array(data["test_data"])
    return owner_data, test_data


# Debug Autoencoder
def debug_autoencoder(owner_data, test_data):
    """
    Test the autoencoder functionality.

    :param owner_data: Owner's normalized typing data.
    :param test_data: Test user's normalized typing data.
    """
    print("=== Autoencoder Debug ===")
    
    # Train the autoencoder
    print("Training the autoencoder...")
    model = train_autoencoder(owner_data)
    
    # Load the trained autoencoder
    print("Loading the autoencoder...")
    loaded_model = load_autoencoder()

    # Calculate reconstruction error for test data
    print("Calculating reconstruction error...")
    reconstruction_results = evaluate_anomaly(test_data, threshold=0.1)
    print(f"Reconstruction Errors: {reconstruction_results['errors']}")
    print(f"Anomaly Detected: {reconstruction_results['anomaly']}")


# Debug Evaluator
def debug_evaluator(owner_data, test_data):
    """
    Test the evaluator metrics and anomaly detection.

    :param owner_data: Owner's normalized typing data.
    :param test_data: Test user's normalized typing data.
    """
    print("\n=== Evaluator Debug ===")
    
    # Calculate cosine similarity
    print("Calculating cosine similarity...")
    cosine_sim = calculate_cosine_similarity(owner_data.mean(axis=0), test_data.mean(axis=0))
    print(f"Cosine Similarity: {cosine_sim}")

    # Calculate reconstruction error directly
    print("Calculating reconstruction error (direct)...")
    reconstruction_err = calculate_reconstruction_error(owner_data.mean(axis=0), test_data.mean(axis=0))
    print(f"Reconstruction Error: {reconstruction_err}")

if __name__ == "__main__":
    # Load sample data
    owner_data, test_data = load_sample_data()

    # Debug: Print loaded data shapes and types
    print(f"Owner data shape: {owner_data.shape}, dtype: {owner_data.dtype}")
    print(f"Test data shape: {test_data.shape}, dtype: {test_data.dtype}")

    # Ensure data is valid for TensorFlow
    if len(owner_data.shape) != 2 or len(test_data.shape) != 2:
        raise ValueError("Loaded data must be 2D (e.g., (n_samples, n_features)).")
    if owner_data.dtype != np.float32:
        owner_data = owner_data.astype(np.float32)
    if test_data.dtype != np.float32:
        test_data = test_data.astype(np.float32)

    # Debug autoencoder
    debug_autoencoder(owner_data, test_data)

    # Debug evaluator
    debug_evaluator(owner_data, test_data)

