'''
Created on Oct 28, 2019
@author: Tyler Major
'''
from array import array


def main():
    header()         #this calls the header function that just prints out the title of the program
    userInput()      #this calls userInput which is where you enter all the players stats and it sends code into a textfile
    askQuestion()    #this calls askQuestion which runs userInput if user enters "yes" and searches players stats if users types "no"


def userInput():
    global answer     #this variable is made global so the askQuestion function can use it
    playerName = input("Enter the player's name: ")                         #prompts user
    yards = input("Enter the number of yards: ")                            #prompts user
    touchdown = input("Enter how many touchdowns occurred: ")               #prompts user
    fumble = input("Enter how many times a fumble occured: ")               #prompts user
    
    myArray = [playerName,yards,touchdown,fumble]                           #puts all user input into an array

    print("\nThe current array holds: " ,myArray, "and it has been saved to a textfile")  #prints out the data inside the array we just created
    a = open('lessonFive.txt', 'a')                                         #makes textfile and parameter set to 'a' so you add to texfile database with stats
    a.write(str(myArray))                                                   #writes the array data into the textfile so players stats exist
    a.write("\n")                                                           #writes new line to textfile for spacing 
    answer = input("\nWould you like to enter data for another player: ")   #prompts user to enter data for another player 
    while (answer != "no"):                                                 #if answer does not equal 'no', run askQuestion function again to add new data
        askQuestion()                                                       #calls askQuestion function again
        if (answer == "no"):                                                #if answer is 'no' to enter another player, program is done
            print("Program finished")


def askQuestion():
    if (answer == "yes"):                                                    #if answer == yes, call user input function again
        userInput()
    elif (answer == "no"):                                                   #if answer is no, search player in textfile
        searchPlayer = input("\nEnter a player's name that exists:")         #prompt user to enter a name that exist in textfile
        searchfile = open("lessonFive.txt", "r")                             #open textfile and read it
        for line in searchfile:                                              #loop through textfile
            if searchPlayer in line:                                         #if user input is in textfile
                #print(line) 
                myarray = list(line.split(","))                              #makes myarray variable and converts it to a list and splits the list at "," so number is alone
                touchdowns = myarray[2].strip("' '")                         #touchdown variable is equal to the 2nd spot in the array we made and we strip the ' ' off of it. For example, '2' is now just 2
                #print(touchdowns)
                calcPoints = int(touchdowns) * 6                             #convert 2 to an integer and than multiply it by 6 to get points
                print("The player you searched scored",touchdowns,"touchdowns which equals", calcPoints , "points")   #print out how many touchdowns player scored and convert it to points
            
        
def header():
    print("*****************************************************")
    print("**** This is a program to calculate NFL Fantasy ****")
    print("****      Written October 28th,2019             ****")
    print("*****************************************************")

main()


        
        

    
    
