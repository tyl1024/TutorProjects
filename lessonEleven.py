#Hangman Game
'''
Created on Dec 23, 2019
@author: Tyler Major
'''
import winsound



def head():
    print("  ---  ")
    print(" -   - ")
    print("  ---  ")
    
def body():
    print("   !   ")
    print("   !   ")
    print("   !   ")
    print("   !   ")
    
    
    
import random

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#here we set the secret
wordList = ["Secret","Superman","Nemo","Yeet"]
word = random.choice(wordList)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in wordlist    
    for char in word:      

    # see if the character is in the players guess
        if char.lower() in guesses:    
    
        # print then out the character
            print (char)    
        else:
        # if not found, print a dash
            print ("_")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won\n")  
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 100 ms
        break              

    # ask the user go guess a character
    guess = input("Guess a character (a-z): ")
    print("")

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess.lower() not in word:  
     # turns counter decreases with 1 (now 9)
        turns -= 1        
        print ("The letter you guesses is not in the word")    
    # how many turns are left
        print ("You have", + turns, 'more guesses\n') 
        
        if (turns == 9):
            head()
        if(turns == 8):
            head()
            body()
 
    # if the turns are equal to zero
        if turns == 0:           
        # print "You Lose"
            print ("You have lost. You did not guess the word in 10 tries\n")
            
            
            
            
            
