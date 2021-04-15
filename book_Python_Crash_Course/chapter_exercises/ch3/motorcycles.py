# Python Crash Course, p.37 - 42
print('\n')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Appending Elements to the End of a List, p.37
motorcycles.append('ducati123')
#Inserting Elements into a List, p.38
motorcycles.insert(0, 'ducati321')
print(motorcycles)

# Removing an Item Using the del Statement, p.39
del motorcycles[2]
print(motorcycles)
print('\n')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print('\n')

# The pop() method removes the last item in a list, but lets you work with item after removal, p.39
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")

# Use pop() to remove an item from any position by including the index, p.40
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print('\n')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Use the remove() method, if you only know the value (not the position) of item you want to remove, p.41
motorcycles.remove('ducati')
print(motorcycles)
print('\n')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Can also use remove() method to work with a value that's being removed from a list, p.41
affordable = 'ducati'
motorcycles.remove(affordable)
print(motorcycles)
print(f"\nA {affordable.title()} is affordable for me.")
