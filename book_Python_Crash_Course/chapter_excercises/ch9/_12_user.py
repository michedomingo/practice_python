"""
A class used to represent users.
"""


class User:
    """A model of a user profile"""

    def __init__(self, first_name, last_name, location):
        """Initialize attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Print user info"""
        print(f"{self.first_name} {self.last_name} from {self.location}")

    def greet_user(self):
        """Prints personalized greeting"""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment the the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0"""
        self.login_attempts = 0
