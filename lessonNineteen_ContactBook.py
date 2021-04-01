'''
Created on Apr 26, 2020

@author: 1024t
'''
import sys
import os

def main():
    menu()
    user = input("Please enter an option based on the menu above: ")
    if(user == "A" or user == "a"):
        text = "ADD a contact."
        print("\nYou have chosen to "+ text)
        add()
    if(user == "S" or user == "s"):
        text = "Search for a contact."
        print("\nYou have chosen to "+ text)
        search()
        
    if(user == "D" or user == "d"):
        text = "DELETE a contact."
        print("\nYou have chosen to "+ text)
        delete()
        
    if(user == "V" or user == "v"):
        text = "VIEW ALL contacts"
        print("\nYou have chosen to "+ text)
        view()
    if(user == "Q" or user == "q"):
        text = "QUIT the program."
        print("\nYou have chosen to "+ text)
        quit()
    if(user == "R" or user == "r"):
        text = "RETURN to menu."
        print("\nYou have chosen to "+ text)
        menu()
    
def add():
    name = input("Enter contacts full name: ")
    tele = input("Enter contacts number: ")
    address = input("Enter contacts address:")
    print("\n",name,"has been added as a contact.")
    filename = "contacts.txt"
    fd = open(filename,"a")
    import random
    for x in range(1):
        id = (random.randint(1,2000000))
        newID = str(id)
    print("The contact " + name+ " has been given the unique ID of ", newID)
    fd.write(name + "\t\t\t\t" + tele + "\t\t\t\t" + address + "\t\t\t\t" + newID + "\t\t\t\n")
    print("\n\n\tQ to QUIT program\n\n")
    print("\tR to RETURN to main menu...\n\n")
    user = input("Please choose to return to the main menu or quit program: ")
    if(user == "R" or user == "r"):
        text = "RETURN to menu."
        print("\nYou have chosen to "+ text)
        main()
    if(user == "Q" or user == "q"):
        text = "QUIT program."
        print("\nYou have chosen to "+ text)
        quit()

def view():
    f = open('contacts.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
   
def delete():
    with open("contacts.txt","r+") as f:                                           #opening text file
        new_f = f.readlines()                                                      #reading every line in the text file
        deletedName = input("Enter the name of the contact you wish to delete: ")  #user input of what we want delete
        f.seek(0)                                                                  #read from beginning of file
        for line in new_f:                                                         #for line in every line in the text file
            if deletedName not in line:                                            #if user input is not in the line, we write line
                f.write(line)                                                      #if user input found, don't write that line
        f.truncate()                                                               #updates what you did
        print("\n", deletedName, "has been removed from the contact book.")
        
   
def search():
    with open("contacts.txt","r+") as f:
        new_f = f.readlines()
        deletedName = input("Enter the name of the contact you wish to search for: ")
        f.seek(0)
        for line in new_f:
            if deletedName in line:
                print("\n" ,line)
        print("\n This is the data for", deletedName, "that you searched for.")
    
    
def quit():
    sys.exit()

def menu():
    print("\n\tA to ADD a contact..\n"+
          "\tS to SEARCH for a contact..\n"+    
          "\tD to DELETE a contact...\n"+
          "\tV to VIEW ALL contacts...\n"+
          "\tR to RETURN to main menu...\n"+
          "\tQ to QUIT program.\n\n")
  
main()
