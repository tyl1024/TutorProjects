'''
Created on Nov 10, 2019

@author: Tyler Major
'''

'''
while True:
    try:
        n = input("Please enter an float: ")
        n = int(n)
        break
    except ValueError:
        print("Not a valid integer! Please try again ...")
print("Great, you successfully entered an integer!")\
'''


'''
#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except NameError:
  print("Define x as a variable")
finally:
  print("The 'try except' is finished")
  '''

'''
    from graphics import *
    def main():
    winHeight = 540
    winWidth = 540
    win = GraphWin("Tyler",winWidth,winHeight)
    win.setBackground("black")
    
    moon = Circle(Point(245,243),120)
    moon.setFill(color_rgb(248,209,50))
    moon.setOutline(color_rgb(248, 209, 50))
    moon.draw(win)
    
    main()
'''






'''
homework = rock,paper,scissors
import random
Have random array contain rock,paper and scissors
randomly choose spot in array
compare user input to random option that computer chose
if user == rock and random == scissors...
    #do stuff

import random as r
data = ["rock","paper","scissors"]
action = r.choice(data)
print(action)    #the computer chose this random choice

user = Enter your choice(rock,paper or scissors)

if action == rock and user == rock
    print tie
.
.
.
'''
    
    

    
    

'''
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]    
player = False
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    '''
