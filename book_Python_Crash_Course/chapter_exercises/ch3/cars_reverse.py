# Python Crash Course, p.45
# reverse() method changes the order of the list (not alphabetically) permanently, p.45
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the orginal list:")
print(cars)

print("\nHere is the list in reverse order:")
cars.reverse()
print(cars)

# revert to the orginal order anytime by applying reverse() to same list a second time, p.45
print("\nHere is the list reverted back to original order:")
cars.reverse()
print(cars)

print('\n')
