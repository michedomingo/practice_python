"""
A set of classes that can be used to represent restaurants.
"""


class Restaurant:
    """Defines a type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant info"""
        print(
            f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints message indicating restaurant is open."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, customer_amount):
        """Set the number of customers who've been served."""
        if customer_amount >= self.number_served:
            self.number_served = customer_amount
        else:
            print("You can't roll back the customer amount!")

    def increment_number_served(self, increment):
        """Increment the number of customers who've been served."""
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't roll back the customer amount!")


class IceCreamStand(Restaurant):
    """Represents aspects of a Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Ice Cream Stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "strawberry", "vanilla"]

    def display_flavors(self):
        """Print a statement about type of flavors sold."""
        print(f"Choose from the following flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")
