# Python Crash Course, p.63 - 65
# to copy a list, make a slice that includes entire original list by omitting first and second indices ([:])
# this tells python to make a slice that starts at first item and ends with last item
print('\n')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # must use a slice to produce two seperate lists, or it will associate amother variable to point to same list

print("My favorite foods are:")
print(f"\t{my_foods}")
print("\nMy friend's favorite foods are:")
print(f"\t{friend_foods}")
print('\n')

# add new food to each list with append(), p.64
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(f"\t{my_foods}")
print("\nMy friend's favorite foods are:")
print(f"\t{friend_foods}")
print('\n')
