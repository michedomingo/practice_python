"""
A set of classes that can be used to represent users.
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


class Privileges:
    """Represents privileges granted to an Administrator."""

    def __init__(self):
        """
        Initialize the admin privileges.
        """
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print a statement that lists admin privileges."""
        print(f"As an admin, you have the following privileges:")
        for p in self.privileges:
            print(f"\t{p.title()}")


class Admin(User):
    """Represents aspects of an Administrator."""

    def __init__(self, first_name, last_name, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes of the Admin class.
        """
        super().__init__(first_name, last_name, location)
        self.admin_privilege = Privileges()
