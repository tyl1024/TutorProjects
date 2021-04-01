'''
Created on Nov 24, 2019

@author: Tyler Major
'''


'''
#What will this print?
x = 4 
x = "Sally"
print(x)
'''


'''
#Will this work?
x, y, z = "Orange", "Banana", "Cherry"
a,b= "apple","banana"
print(x)
print(y)
print(z)
print(a)
print(b)
'''

'''
a,b = ["hi","bye"]
print(a[0:2])
print(b[0:3])
'''


'''
#What should be used here. Commma or plus sign?
x = "hello"
print("The number is: " ,       x )
'''


'''
#Code a for loop that prints your name 5 times?



for i in range(5):
    print("Vikram")
'''


'''
#How can you find out the data type of a variable?
x = 1
y = ['hello']
z = "Goodbye"




print(type(x), "\n",     type(y) , "\n",     type(z), "\n")
'''
 
 
 
    
'''  
#How can I turn an integer into a float?



x = 5
print(float(x))
'''



'''
#How can I print out a random number between 1-15?


import random

print(random.randrange(1,15))
'''


'''
#What will this print?
a = "Hello, World!"
print(a[7])
'''



'''
#What will this print?
a = ["Hello", "World"]
print(a[0])
'''
'''
a = "This is a sentence"
print(len(a))
'''

'''
array = ["hi", "bye"]
print(len(array))
'''

'''
#How can I find the length of a string or array?




a = ['a','b','c']
print(len(a))
b = "This is a sentence"
print(len(b))
'''

x = "I have a dog"
print(x[7:13])

y = "cat dog fish"
print(y[4:7])
'''
#How can I print out the range between a string. Example: How can I print "a dog" in the string "I have a dog"
x = "I have a dog"
print(x[7:12])
y = "cat dog fish"  #print just cat



print(y[0:3])
'''


'''
#What will this do?
a = " Hello, World! "
print(a.split(" ")) 
'''



'''
#What will this do?
a = "       Hello, World!    "   #begin/end
print(a.strip()) 
print(a)
'''



'''
#How can you make text lower case?
x = "TYLER AAHHHH"
y = "tYlEr"
'''

    






#Text based adventure game
def main():
    intro()
    userInput()
    firstQuestion()
    
    

def intro():
    print("Welcome to Tyler's Text Adventure Game. \n")
    print("Plot:\n\n\t It is a dark stormy night. A loud thunder bang crackles throughout the sky shakes the entire house.\n"
          + "You wake up with your heart beating fast because of how bad it scared you. You reach over to turn the light on\n"
          + "but the light won't turn on. The power must have went out. So you reach around your dark room to find your\n"
          + "cell phone. You forgot to charge it the night before so your phone battery is on 5 percent. You yell out for\n"
          + "your parents but no one answers. MOM! DAD!.....no response. So you try again. MOM!! DAD!!!...nothing but silence\n" 
          + "You start to get worried so you get up out of bed with your phone in your hand. You put your phone on battery saver\n" 
          + "mode and it says it will last for 10 minutes. What will you do next.....\n\n")
    
def userInput():
    name = input("What is your name: ")
    print("Hello",name,", every action you make from now on will change the result of the story. Choose carefully...")
    
def firstQuestion():
    q1 = eval(input("Choose an option: \n" +
               "\t1: You open the door to enter your dark hallway to try to find your parents\n"+
               "\t2: You go back to your bed and scream and yell for help\n"+
               "\t3: You try to call your parents with your cell phone that has 10 minutes left of power\n\n"))
    if (q1 == 1):
        print("\nYou slowly open the door and turn on your phone flashlight. You have 9 minutes left of battery.\n"+
              "You start to head slowly to your parents bedroom to see where they are... \n")
        parentsRoom()
    elif (q1 == 2):
        yourRoom()
    elif (q1 == 3):
        print("You go to your contacts and try to call your Mom first. It rings and no one answers. You then\n" +
              "dial your Dad's number and you hear the phone ring from in his room. Someone answers and says: SHHHH\n")
        phoneCall()
        

def parentsRoom():
    print("You yell Mom! Dad! Still no answer... You are walking down the hallway when suddenly you hear a bang in your bathroom\n") 
    x = eval(input("Choose an option: \n "+
               "\t1: You run passed the door and slam open your parents door.\n"+
               "\t2: You turn around and run back into your room.\n"+
               "\t3: You investigate the bathroom noise before going into your parents room.\n\n"))  
    
def yourRoom():
    print("You jump back in bed and frantically scream and yell for help. No one is answer but you look out your window\n" +
          "and see your neighbor pulling into her driveway...")
    x = eval(input("Choose an option: \n "+
               "\t1: You open the window and yell your neighbors name and beg for help.\n"+
               "\t2: You leave your room again and try to make it to your neighbors house.\n"+
               "\t3: You continue to scream and yell and ignore your neighbor.\n\n"))
    
def phoneCall():
    print("You are shocked to hear someone shush you and you are unsure if it is your Dad's voice or not. ")
    x = eval(input("Choose an option: \n "+
               "\t1: You say nothing and listen to see if anything else is said.\n"+
               "\t2: You say: Dad? Is that you?.\n"+
               "\t3: You hang up the phone.\n\n"))
        
main()








