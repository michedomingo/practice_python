# Python Crash Course, p.65
# choose a version of foods.py and write 2 for loops to print lists
print('\n')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for mine in my_foods:
	print(f"\t{mine.title()}")

print("\nMy friend's favorite foods are:")
for other in friend_foods:
	print(f"\t{other.title()}")

print('\n')
