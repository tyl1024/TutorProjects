'''
Created on Nov 3, 2019

@author: Tyler Major
'''

import random as r

'''
number = r.randint(0,5)
print(number)
'''

'''
myList = ['a','b','c']
print(r.choice(myList))
'''


headsCounter = 0
tailsCounter = 0
myList = ["heads", "tails"]
for i in range(100000):
    coin = r.choice(myList)
    if (coin == "heads"):
        headsCounter += 1
    if (coin == "tails"):
        tailsCounter += 1
    
        
print("Total Heads: ", headsCounter)
print("Total Tails: ", tailsCounter)


#random Password generator
#Ask user how long the password should be
#Ask how many letters
#Ask how many numbers
