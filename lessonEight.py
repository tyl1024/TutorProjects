'''
Created on Nov 15, 2019

@author: Tyler Major
'''
from turtle import *
import turtle

'''
# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels
bob.forward(100)

# Step 4: We're done!
turtle.done()
'''


'''
silly = turtle.Turtle()

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()
'''


'''
smart = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    smart.forward(50)
    smart.right(90)
    
# This isn't indented, so we aren't repeating it.
turtle.done()
'''



'''
star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(145)
    
turtle.done()
'''


'''
spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 100)
    spiral.right(144)
    
turtle.done()
'''


'''
polygon = turtle.Turtle()

polygon.pencolor("red")
polygon.fillcolor("blue")
polygon.shapesize(5, 5, 5)
#polygon.color("black", "red")

num_sides = 9
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
'''


'''
t = turtle.Turtle()
t.fillcolor('orange')
t.begin_fill()
for i in range(6):
  t.forward(150)
  t.right(60)
t.end_fill()
turtle.done()
'''


'''
alex = turtle.Turtle()
alex.shape("turtle")
alex.speed(1)
alex.goto(15, 250)
turtle.done()
'''




'''
screen = Screen()
screen.bgcolor('SkyBlue')    #sets background color

shape = Shape('compound')     #just set as standard


turtle = Turtle(visible=False)  #gets rid of drawing line
turtle.speed(1)
turtle.penup()                   #gets rid of drawing lines


turtle.begin_poly()            #make shape
turtle.circle(15)
turtle.end_poly()              #end shape
shape.addcomponent(turtle.get_poly(), 'red')   #color shape


screen.register_shape('circle', shape)   #store shape and name it house so now we can move circle anywhere

turtle.goto(-200, -200)            #starting positions

# Now we can move our house in any manner that we move a turtle:
turtle.shape('circle')


turtle.forward(100)   #pixels to the right

screen.mainloop()
'''


'''
import turtle

screen = turtle.Screen()
screen.bgcolor('SkyBlue')    #sets background color

shape = Shape('compound')     #just set as standard

alpha = turtle.Turtle()
beta = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()



alpha.left(180)
beta.right(0)

alpha.speed(1)
beta.speed(2)

alpha.forward(100)
beta.forward(100)


turtle1.begin_fill()
turtle1.begin_poly()            #make shape
turtle1.circle(15)
turtle1.end_poly()              #end shape
turtle1.end_fill()
shape.addcomponent(turtle1.get_poly(), 'green')   #color shape


screen.register_shape('circle', shape)   #store shape and name it house so now we can move circle anywhere
turtle2.shape("circle")
turtle2.forward(100)


turtle.done()
'''



'''
#turtle game

playGround = Screen()

playGround.screensize(250, 250)
playGround.title("Turtle Keys")

run = Turtle("turtle")
run.color("blue")
run.penup()
run.setposition(250, 250)
run.speed(5)

follow = Turtle("turtle")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

def k1():
    run.forward(45)

def k2():
    run.left(45)

def k3():
    run.right(45)

def k4():
    run.backward(45)

def quitThis():
    playGround.bye()

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

def follow_runner():
    follow.setheading(follow.towards(run))
    follow.forward(min(follow.distance(run), 8))

    if is_collided_with(follow, run):
        print('Collision!')
        quitThis()
    else:
        playGround.ontimer(follow_runner, 10)

playGround.onkey(k1, "Up")  # the up arrow key
playGround.onkey(k2, "Left")  # the left arrow key
playGround.onkey(k3, "Right")  # you get it!
playGround.onkey(k4, "Down")

playGround.listen()

follow_runner()

playGround.mainloop() 
'''  




'''
#Pratice GUI
from tkinter import *
 
window = Tk()
 
window.title("YEEEEET")
 
window.mainloop()
'''


'''
from tkinter import *
window = Tk()
 
window.title("Welcome Vikram")
 
label = Label(window, text="Yeeet!")
 
label.grid(column=0, row=0)
 
window.mainloop()
'''


'''
from tkinter import *
window = Tk()
 
window.title("Welcome Tyler")
lbl = Label(window, text="Hello", font=("Arial Bold", 100))
lbl.grid(column=0, row=0)
 
window.mainloop()
'''


'''
from tkinter import *
 
window = Tk()
 
window.title("Welcome!! :)")
 
window.geometry('500x500')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=1, row=5)
 
btn = Button(window, text="Don't touch this button")
 
btn.grid(column=0, row=5)
 
window.mainloop()
'''



'''
from tkinter import *
 
window = Tk()
 
window.title("Welcome!!")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
def clicked():
    lbl.configure(text="Button was clicked !!")
 
btn = Button(window, text="Click Me", bg="orange", fg="red",command = clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()
'''




'''
from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("Welcome!!")
 
window.geometry('350x200')
 
def clicked():
    messagebox.showinfo('Logout Screen', 'You have succesffully logged out')
 
btn = Button(window,text='logout', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()
'''


'''
from tkinter import *
 
from tkinter.ttk import Progressbar
 
from tkinter import ttk
 
window = Tk()
 
window.title("Welcome!!")
 
window.geometry('350x200')
 
style = ttk.Style()
 
style.theme_use('default')
 
style.configure("black.Horizontal.TProgressbar", background='green')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 99
 
bar.grid(column=0, row=0)

 
window.mainloop()
'''




from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import mp3play

window = Tk()
 
window.title("Welcome!!")
 
window.geometry('650x600')


style = ttk.Style()
style.configure("black.Horizontal.TProgressbar", background='red')
 
bar = Progressbar(window, length=300, style='black.Horizontal.TProgressbar')
bar['value'] = 10
bar.grid(column=0, row=0)
 
def clicked():
    bar['value'] = bar['value'] + 10
    if bar['value'] > 100:
       messagebox.showinfo('Data Successful', 'The bar has reached 100%')
       
def decrease():
    bar['value'] = bar['value'] -10
    if bar['value'] < 0:
       messagebox.showinfo('Data Successfully deleted', 'The bar has reached 0%')

def playMusic():
    print()
       

     
btn = Button(window, text="Click Here To Increase Bar", bg="blue", fg="white",command = clicked)
btn.grid(column=1, row=0)
 
 
btn2 = Button(window, text="Click Here To Decrease Bar", bg="blue", fg="white",command = decrease)
btn2.grid(column=2, row=0)

lbl = Label(window, text="YEEEEET", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

window.mainloop()













