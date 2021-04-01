"""
TypeSpeed is a simple program that measures your typing speed
Type on!
"""

# Python imports
import random
from threading import Timer
import sys



ended = False


def main():
    """ Displays available menu options """

    print("\n")
    print("     1. Play")
    print("     2. Exit")           #main menu
    print("\n")

    choice = int(input())      #user input

    while choice not in range(1,3):  #checks to make sure input correct
        print("> Invalid input")
        choice = int(input())
    else:
        if choice == 1:
            start_game()    #if one, start game
        elif choice == 2:
            sys.exit()      # 2 = quit and close


def get_words():
    """ Returns an array of words extracted from words.txt """
    words = [] 
    with open('words.txt', 'r') as f:
        words = f.read().split("\n")
    return words


def check_word(reference_word, given_word):
    """
    Compares the word the user was supposed to type and the word user typed
    Returns true if both match, false otherwise
    Parameters:
        reference_word:
            Reference word
        given_word:
            Word to check
    """

    if reference_word == given_word:
        return True
    return False


def get_stats(correct, wrong, total):
    """
    Computes and returns the player's typing stats
    Parameters:
        correct:
            Number of correct words
        wrong:
            Number of wrong words
        total:
            Total number of words
    """

    accuracy = round(((correct / total) * 100), 2)
    speed = float(correct)/1 #min or 60 seconds

    stats = {
        "right": str(correct),
        "wrong": str(wrong),
        "accuracy": str(accuracy),
        "WPM": str(speed)
    
    }
    return stats


def end_game():
    """ Ends the game and prepares the results """

    global ended
    stats = get_stats(correct_words, wrong_words, total_words)
    print("\n")
    print(stats)
    ended = True


def start_game():
    """ Starts the game """

    global correct_words
    global wrong_words
    global total_words

    print("""
    Quick guide:
        A word will come up on the screen and you'll have to type the exact same word
        and hit enter. You'll have 60 seconds to type in as many words as you can.
        """)
    print("Hit enter to continue ('q' to exit_game)")

    response = input()

    if response == "q":
        exit()

    correct_words = 0
    wrong_words = 0
    total_words = 0
    word_list = get_words()
    # Call end_game() after 60 seconds
    t = Timer(60, end_game)
    t.start()

    while True:
        if ended:
            exit()
        random_word = random.choice(word_list)
        total_words += 1
        print("  ", random_word)
        typed_word = input("> ")

        if check_word(random_word, typed_word):
            correct_words += 1
        else:
            wrong_words += 1

main()

