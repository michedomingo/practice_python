# Python Crash Course, p.60
"""
# use 3rd arg of range() to print list of odd numbers 1 to 20
# incorrect output not expected
print('\n')

odd_numbers = list(range(1, 21, 3))
print(odd_numbers)

"""
print('\n')

# Python program to print odd Numbers in a List using modulo
  
# list of odd numbers 
odd_numbers = list(range(1, 21))
  
# iterating each number in list 
for num in odd_numbers:
      
    # checking condition 
    if num % 2 != 0: 
       print(num) 

print('\n')
# Python program to print odd Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num % 2 != 0: 
       print(num, end = " ") 
print('\n')
