# Python Crash Course, p.61 - 62
# to output first three elements in a list, request indices 0 through 3 to return elements 0, 1, and 2
print('\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# to output 2nd, 3rd, and 4th items in a list, start slice at index 1 and end at index 4
print(players[1:4])

# if you omit fist index in a slice, Python automatically starts slice at beginning of list
print(players[:4])

# if you want a slice that includes end of list, omit 2nd index, p. 62
print(players[2:])

# negative index returns an element a certain distance from the end of list
# to output last three players on roster:
print(players[-3:])

# include a third value in the brackets, tells python how many items to skip between items in specified range
print(players[0:5:2])
print('\n')

# loop through first three players and print names as a simple roster
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print('\n')