# Python Crash Course, p.60
# make list of first 10 cubes / cube of each int from 1 through 10, then print values with for loop
print('\n')
cubes_list = []
for value in range(1, 11):
	cube = value ** 3
	cubes_list.append(cube)

print(cubes_list)
print('\n')