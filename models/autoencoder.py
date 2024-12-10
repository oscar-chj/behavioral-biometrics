"""
Autoencoder for typing behavior anomaly detection.

This module includes:
1. Training the autoencoder on owner's typing data.
2. Saving and loading the trained model.
3. Calculating reconstruction error for anomaly detection.
"""

from tensorflow.python.keras.models import Sequential, load_model
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.callbacks import EarlyStopping
import numpy as np
import os

MODEL_PATH = "models/owner_typing_model.h5"  # Path to save the trained model

def build_autoencoder(input_dim):
    """
    Build an autoencoder model for typing data.

    :param input_dim: The number of features in the input data.
    :return: Compiled autoencoder model.
    """
    model = Sequential([
        Dense(64, activation="relu", input_dim=input_dim),
        Dense(32, activation="relu"),
        Dense(64, activation="relu"),
        Dense(input_dim, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

def train_autoencoder(data, save_model=True):
    """
    Train the autoencoder on owner's typing data.

    :param data: Normalized typing data (e.g., latencies, heatmaps). Must be a 2D Numpy array.
    :param save_model: Whether to save the trained model to disk.
    :return: Trained autoencoder model.
    """
    # Ensure data is a valid Numpy array and 2D
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if len(data.shape) != 2:
        raise ValueError(f"Data must be a 2D array, but got shape {data.shape}")

    input_dim = data.shape[1]
    model = build_autoencoder(input_dim)

    # Debug: Confirm data shape and type
    print(f"Training data shape: {data.shape}, dtype: {data.dtype}")

    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor="loss", patience=5)

    # Train the model
    model.fit(data.astype(np.float32), data.astype(np.float32),  # Ensure dtype compatibility
              epochs=50, batch_size=16, shuffle=True, callbacks=[early_stopping])

    # Save the trained model
    if save_model:
        model.save(MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")
    return model

def load_autoencoder():
    """
    Load a pre-trained autoencoder model.

    :return: Loaded autoencoder model.
    """
    if os.path.exists(MODEL_PATH):
        return load_model(MODEL_PATH)
    else:
        raise FileNotFoundError(f"No saved model found at {MODEL_PATH}")


def calculate_reconstruction_error(data, model):
    """
    Calculate reconstruction error for typing data using the trained model.

    :param data: Normalized typing data to evaluate.
    :param model: Trained autoencoder model.
    :return: Mean reconstruction error for the input data.
    """
    reconstructed = model.predict(data)
    error = np.mean(np.square(data - reconstructed), axis=1)  # Per-sample error
    return error

def evaluate_anomaly(test_data, threshold=0.1):
    """
    Evaluate anomaly by calculating reconstruction error and comparing it to a threshold.

    :param test_data: Normalized typing data for authentication.
    :param threshold: Error threshold for anomaly detection.
    :return: Dictionary with reconstruction error and anomaly flag.
    """
    model = load_autoencoder()
    errors = calculate_reconstruction_error(test_data, model)
    anomaly_flag = errors > threshold
    return {"errors": errors.tolist(), "anomaly": anomaly_flag.any()}
