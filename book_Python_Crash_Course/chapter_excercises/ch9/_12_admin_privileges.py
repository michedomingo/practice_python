"""
A set of classes that can be used to represent admins.
"""
from _12_user import User


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
