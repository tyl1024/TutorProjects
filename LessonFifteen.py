'''
Created on Feb 17, 2020

@author: Tyler Major
'''

#easy questions.. 1-3     $100
#medium questions..4-6    $500
#hard questions..  7-10   $1000

#easyQ1,medQ2,hardQ3 = whatever the question is
#["what is the first letter in the alphabet, "what is animal that barks?]....random question from array
# total amount won
#if wrong, we lose and program stops and money is lost..
#questions...
'''
["what is the first letter in the alphabet, "what is animal that barks?, "What 5 * 5?"]
["What is the square root of 144?", "What is 5^2","Which president is on the 20 dollar bill?" 
["Fill in the blank... force = _____ * acceleration", "What is group of mammals that lay eggs classified as?"
'''
import random
import sys
import time

def main():
    intro()
    registerPlayer()
    question1()
    
def intro():
    print("\n************************************************************")
    print("** Welcome to who wants to be a millionaire!              **")
    print("** This is a 10 question game and the questions           **")
    print("** will get significantly harder as you get more correct. **")
    print("************************************************************\n")
    
def registerPlayer():
    name = input("Enter your name: ")
    print("Welcome," , name, "... Let's get ready for who wants to be a millionaire!\n")
    print("Your first question will be below...\n\n")
    print("IF YOU TAKE LONGER THAN 5 SECONDS")
    
def question1():
        #start = time.time()
        #while (time.time() - start < 5):   #runs for 5 seconds
            easyQ = ["What is the first letter in the alphabet?" ,"What is animal that barks?", "What 5 * 5?"]
            randomEasy = random.choice(easyQ)   #gets random question
            firstQ = input(randomEasy)          
            if randomEasy == easyQ[0]:
                answer = "a"
            elif randomEasy == easyQ[1]:
                answer = "dog"
            elif randomEasy == easyQ[2]:
                answer = "25"
           # if (time.time() - start > 5):
            #    print("Sorry you ran out of time! Try again next time! You lose!\n")
             #   sys.exit()
            if firstQ == answer:
                print("Correct! You won 100 dollars!\n")
            else:
                print("Sorry! that's the wrong answer!\n")

main()

    