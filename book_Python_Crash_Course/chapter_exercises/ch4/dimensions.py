# Python Crash Course, p.66
# tuple is an immutable list - values cannot change
# tuple looks like a list except use parenthesis instead of square brackets
print('\n')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print('\n')

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
print('\n')
