from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np

# Build an autoencoder model
def build_autoencoder(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(32, activation='relu'),
        Dense(64, activation='relu'),
        Dense(input_dim, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# Train the autoencoder
def train_autoencoder(model, data):
    model.fit(data, data, epochs=50, batch_size=16, shuffle=True, verbose=0)
    return model

# Compute reconstruction error
def compute_reconstruction_error(model, data):
    reconstructed = model.predict(data)
    return np.mean(np.square(data - reconstructed), axis=1)
