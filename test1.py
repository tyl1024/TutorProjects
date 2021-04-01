'''
Created on Jan 25, 2020

@author: 1024t
'''
import sys


def main():
    menu()
    
    while(choice != '5'):  
    
        if (choice=='1'):
            print()
    
        elif (choice == '2'):
            words = []  #terms
            answers = [] #definitions
            term = input('What is the term:')
            define = input ('What is the definition: ')
            print(term,'has been added')
            for i in words:
                words.append(term)
                print("hi: ",words)
            for j in answers:
                answers.append(define)
                print("Bye",answers)
            rtrn = input("\n\tPress 'Enter' to return to Main Menu.\n")  
            if (rtrn == ("")):
                menu()
    

def menu():
    global mscreem,choice
    mscrem = print("""

    DIGITAL FLASHCARDS!

    1 - List Terms
    2 - Add Term
    3 - Guess Random Definition
    4 - View Term-Definition Pairs
    5 - Exit

    """)
    choice = input("\t\t\tEnter Menu option: ")
    

main()



