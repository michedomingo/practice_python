# Python Crash Course, p.60
# make a list of numbers 1 to 100, print min/max/sum of list
print('\n')

list = []
for value in range(1, 101):
	number = value
	list.append(number)

print(list)
print(min(list))
print(max(list))
print(sum(list))

print('\n')
