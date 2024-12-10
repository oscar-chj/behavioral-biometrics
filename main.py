"""
Main entry point for the typing application.

This script initializes the Typing Test application, which allows
users to register, authenticate, and test their typing skills.
"""

from gui.typing_test import TypingTestGUI

if __name__ == "__main__":
    app = TypingTestGUI()
    app.start()
