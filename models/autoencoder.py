"""
Autoencoder for typing behavior anomaly detection.

This module uses an autoencoder to identify anomalies in typing patterns.
"""

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

def build_autoencoder(input_dim):
    """Build an autoencoder model."""
    model = Sequential([
        Dense(64, activation="relu", input_dim=input_dim),
        Dense(32, activation="relu"),
        Dense(64, activation="relu"),
        Dense(input_dim, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="mse")
    return model
