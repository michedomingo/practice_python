# Python Crash Course, p.73
# loops through list of car names, print 'bmw' in uppercase, otherwise title case
print('\n')

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())	

print('\n')
