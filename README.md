# Behavioral Biometric Typing Analysis System

This project demonstrates a concept for a security system that uses typing biometrics to determine if the current user is the owner of the device. The system leverages AI to analyze typing speed, accuracy, and patterns to compute the probability of a different user operating the system.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Implementation Details](#implementation-details)
- [Future Work](#future-work)
- [License](#license)

## Introduction

The system captures and analyzes user typing behavior in real-time, comparing it to a pre-recorded owner's typing data. If the typing style deviates significantly beyond a set threshold, the system alerts that the current user may not be the owner.

## Features

1. Collects typing data such as speed, key press duration, and heatmap.
2. Preprocesses the data for analysis.
3. Uses a pre-trained AI model to compare the current user's typing behavior with the owner's profile.
4. Outputs a probability score indicating the likelihood of a different user.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/oscar-chj/behavioral-biometrics.git
    cd behavioral-biometrics
    ```

2. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python main.py
    ```

## Usage

1. Run the `main.py` script to launch the GUI.
2. Choose to **Register** or **Authenticate**:
    - **Register**: Record the owner's typing behavior by typing a given phrase multiple times.
    - **Authenticate**: The system compares the current typing data with the owner's stored profile.
3. View the result, which shows a probability score and whether the user is identified as the owner or a different person.

## File Structure

```
behavioral-biometric-typing/
│
├── main.py              # Main script to run the application
├── gui.py               # GUI implementation using Tkinter
├── ai_model.py          # AI model for comparison
├── data/
│   ├── owner_profile.json  # Pre-recorded owner's typing profile
│   └── current_data.json   # Current user's typing data
├── utils.py             # Utility functions for data preprocessing
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Implementation Details

- **Typing Data Collection**: Records typing speed, key press durations, and key release intervals.
- **Data Preprocessing**: Normalizes and cleans the data for AI analysis.
- **AI Model**: A lightweight machine learning model is used to compare typing behaviors and compute a probability score.
- **Threshold**: A configurable threshold determines the probability score above which a user is flagged as different.

## Future Work

- Expand biometric features to include mouse movements and scrolling patterns.
- Integrate with OS-level APIs for seamless operation.
- Train the AI model with a larger dataset for higher accuracy.
- Develop a mobile version for Android and iOS.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
