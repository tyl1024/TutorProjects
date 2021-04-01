'''
Created on Jan 24, 2020

@author: 1024t
'''
import random


terms = {}
menu = None
while menu != "5":
    print("""

    DIGITAL FLASHCARDS!

    1 - List Terms
    2 - Add Term
    3 - Guess Random Definition
    4 - View Term-Definition Pairs
    5 - Exit

    """)
    menu = input("\t\t\tEnter Menu option: ")
    if menu == "1":  # List Terms
        print("\n")
        for term in terms:
            print("\t\t\t", term)
        input("\n\tPress 'Enter' to return to Main Menu.\n")

    elif menu == "2":  # Add Term
        term = input("\n\tEnter the new term: ")
        if term not in terms:  #if it already exist
            definition = input("\tWhat is the definition? ")
            terms[term] = definition
            print("\n\t" + term, "has been added.")
        else:
            print("\n\tThat term already exists!")
            input("\n\tPress 'Enter' to return to Main Menu.\n")

    elif menu == "3": # Guess Random Definition. Once correct, choose new random definition
        def generate_question():
            term, definition = random.choice(list(terms.items()))
            print("\n\t" + definition + "\n")
            return term
        term = generate_question()
        guess = None
        while guess != "EXIT":
            guess = input("\tWhat is the term? ")
            if guess == term:
                print("Correct!")
                if input("\tAnother definition?(y/n)") in ["y", "Yes", "Y", "YES"]:
                    term = generate_question()
                else:
                    break
    elif menu == "4": # Random display a term-definition pair.
        print("\n\t\t\tType 'Exit' to return to Menu\n")
        exit = None
        while exit != "EXIT":
            print("Type EXIT if want to stop seeing pairs")
            term, definition = random.choice(list(terms.items()))
            print(term + ":", definition)
            exit = input("")  # Press enter to continue.
 
 
