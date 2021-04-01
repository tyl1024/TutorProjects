'''
Created on Feb 15, 2020

@author: 1024t
'''

from collections import Counter
num = Counter("777")  #input
print(num)

#input = enter a num:    ex('1776')
#amount = Counter(str(input))
#print(amount)   dictionary output
#find key ID for our lucky num and print that out 

#____________________________
#luck numbers are 6 and 8
#ex... 65 is lucky, 81 is lucky, 66 is lucky, and 88 is lucky,  46 is lucky and 98 is lucky but 68 and 1668 are unlucky
# two lucky numbers and if the number contains both lucky numbers, it is unlucky

num = input("Enter a num:")
amount = Counter((num))
print(amount)





