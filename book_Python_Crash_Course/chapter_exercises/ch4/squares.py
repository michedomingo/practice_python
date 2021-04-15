# Python Crash Course, p.58 - 60
# make list of first 10 square numbers / square of each integer from 1 through 10
# two asterisks (**) represent exponents
print('\n')

# p. 58
squares = []
for value in range(1, 11):
	square = value ** 2 # more concisely: omit temporary variable square, append each new value directly to list (as below)
	squares.append(square)
print(squares)
print('\n')

# p. 59
squares = []
for value in range(1, 5):
	squares.append(value**2) # sometimes using a temporary variable makes code easier to read
print(squares)
print('\n')

# List Comprehensions, p. 60
# combines for loop and creation of new elements into one line, automatically appends each new element
squares = [value**2 for value in range(1, 11)] # Notice: NO Colon is used at end of for statement
print(squares)
print('\n')
