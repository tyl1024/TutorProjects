'''
Created on Jun 8, 2020

@author: Tyler Major
'''
def main():
    intro()
    menu()
    userInput()
    deposit()
    
    
   
   
def intro():
    global menu
    print("\n\nWelcome to your personal bank! Follow the menu options to access your bank.")

def menu():
    print("\n\t\t1: TO VIEW BALANCE\n\t\t2: TO DEPOSIT\n\t\t3: TO WITHDRAW\n\t\t4: TRANSFER CHECKING TO SAVINGS\n\t\t5: TRANSFER SAVINGS TO CHECKING\n\t\t6: MAKE A FOLDER\n\t\t7: QUIT")
    
    
def userInput():
    user = eval(input("\nPlease enter an option based on the  menu above: "))
    if (user == 2):
        deposit = eval(input("How much do you want to deposit?: "))
        newDep = str(deposit)
        filename = "bank.txt"
        fd = open(filename,"a")
        fd.write(newDep)
        
    if (user == 3):
        withdraw()
        
        
def deposit():
    k = open("bank.txt",'r+')
    lines = k.readlines()     #i am reading lines here
    counter = 0          #counter update each time number is entered
    k.write("\n")
    for line in lines:            #taking each line
       conv_int = int(line)         #converting string to int
       counter = counter + conv_int      #update counter
    print(counter)
    
def withdraw():
    withdraw = eval(input("How much do you want to withdraw?: "))
    k = open("bank.txt",'r+')
    lines = k.readlines()     #i am reading lines here
    counter = 0          #counter update each time number is entered
    for line in lines:            #taking each line
       conv_int = int(line)         #converting string to int
       counter = counter + conv_int      #update counter
    total = counter - withdraw
    print(total)
    


        
main()