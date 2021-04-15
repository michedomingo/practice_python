# Python Crash Course, p.68
# store five simple foods in tuple
print('\n')

foods = ('pizza', 'fries', 'salad', 'bagels', 'coffee')
print("Original menu:")
for food in foods:
	print(f"\t{food.title()}")

# foods[0] = 'junk' - TypeError: 'tuple' boject doe not support item assigment

foods = ('gelato', 'waffles', 'salad', 'bagels', 'coffee')
print("\nRevised menu")
for food in foods:
	print(f"\t{food.title()}")

print('\n')
