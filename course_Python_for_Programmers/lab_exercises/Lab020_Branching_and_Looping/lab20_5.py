#!/usr/bin/env python3
"""
5. (Optional) Write a script
that produces this pattern:
         *          01
        ***         03
       *****        05
      *******       07
     *********      09
    ***********     11
   *************    13 
  ***************   15
 *****************  17
******************* 19
Can you find an easier way?
Hint: Remember lab10_2 where you 
learned to multiply and concatonate strings.
"""
asterisk = '*'
blanks = 9

for num in range(1, 20, 2):
    print(blanks * ' ', asterisk * num)
    blanks -= 1
