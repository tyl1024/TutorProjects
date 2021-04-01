'''
Created on Dec 9, 2019

@author: 1024t
'''

def main ():
    intro()
    uinput()
    work()
   
def intro():
    print('Welcome to my calculator.')
    print('0 is to add.')
    print('1 is to subtract.')    
    print('2 is to multiply.')
    print('3 is to divide.')

def uinput():
    global choice
    choice = eval(input('Enter the operation you would like to use: '))
    if (choice >= 4):
        error()
    
def error():
    print("You have entered an invalid number. Please try again")
    uinput()
    
def add():
    print(fnum + snum)
    
def sub():
    print(fnum - snum)

def multiply():
    print(fnum * snum)    

def divide():
    print(fnum / snum)

def work():
    global fnum,snum
    fnum =  eval(input('Enter the first number: '))
    snum =  eval(input('Enter the second number: '))
    if (choice == 0):
        add()
    elif (choice == 1):
        sub()
    elif(choice == 2):
        multiply()
    elif(choice == 3):
        divide()
                
main()
