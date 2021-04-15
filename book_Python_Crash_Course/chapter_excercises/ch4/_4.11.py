# Python Crash Course, p.65
# add onto program from ex.4-1
print('\n')
pizzas = ['pepperoni', 'sausage', 'mushroom']
friend_pizzas = pizzas[:]

pizzas.append('hawaiian')
friend_pizzas.append('italian')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())
print('\n')	

print("My friend's favorite pizzas are:")
for other in friend_pizzas:
	print(f"\t{other.title()}")

print('\n')
