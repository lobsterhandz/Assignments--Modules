class TextUtils:
    """
    A class that provides text utility functions for string manipulation.
    """

    @staticmethod
    def reverse_string(s):
        """
        Function to reverse a given string.
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s[::-1]

    @staticmethod
    def capitalize_string(s):
        """
        Function to capitalize a given string.
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s.capitalize()

    @staticmethod
    def remove_whitespace(s):
        """
        Function to remove whitespace from a given string.
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s.replace(" ", "")
