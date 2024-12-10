"""
Base Theme class for the Typing Test application.

This class provides the base color scheme, font settings, and other
styling properties for the GUI.
"""

class BaseTheme:
    def __init__(self):
        self.background_color = "#1E1E2F"
        self.text_color = "#FFFFFF"
        self.accent_color = "#FFC857"
        self.font_family = "Courier New"
        self.font_size = 16

    def get_styles(self):
        """
        Returns the styles as a dictionary for use in the GUI.

        :return: Dictionary of styles.
        """
        return {
            "background": self.background_color,
            "text": self.text_color,
            "accent": self.accent_color,
            "font": (self.font_family, self.font_size)
        }
