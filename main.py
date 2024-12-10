from gui import TypingGUI
from utils import load_profile, normalize_data
from ai_model import build_autoencoder, train_autoencoder, compute_reconstruction_error
import numpy as np

def main():
    owner_profile_file = "data/owner_profile.json"
    current_profile_file = "data/current_data.json"

    print("1. Set Up Owner Profile")
    print("2. Authenticate as Owner")
    print("3. Use as Guest")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        print("Setting up owner profile...")
        gui = TypingGUI()
        gui.start(is_owner=True, filename=owner_profile_file)

    elif choice == "2":
        print("Authenticating as owner...")
        owner_profile = load_profile(owner_profile_file)
        if not owner_profile:
            print("No owner profile found. Please set up the owner profile first.")
            return

        gui = TypingGUI()
        gui.start(is_owner=False, filename=current_profile_file)
        current_profile = load_profile(current_profile_file)

        # Normalize data for the model
        owner_data = normalize_data(owner_profile["key_durations"])
        current_data = normalize_data(current_profile["key_durations"])

        # Train and test the autoencoder
        autoencoder = build_autoencoder(input_dim=len(owner_data))
        autoencoder = train_autoencoder(autoencoder, np.array([owner_data]))
        error = compute_reconstruction_error(autoencoder, np.array([current_data]))

        print(f"Reconstruction Error: {error[0]}")
        if error[0] > 0.1:  # Example threshold
            print("Warning: Typing does not match the owner's profile!")
        else:
            print("Typing matches the owner's profile.")

    elif choice == "3":
        print("Using as guest. No profile comparison will be performed.")
        gui = TypingGUI()
        gui.start(is_owner=False, filename=current_profile_file)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
