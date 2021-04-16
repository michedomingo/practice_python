"""
Create instances of restaurants.
"""
from _10_restaurant import IceCreamStand


my_stand = IceCreamStand("salt & straw", "ice cream")
print(f"{my_stand.restaurant_name.title()} sells yummy {my_stand.cuisine_type.title()}.")
my_stand.display_flavors()
