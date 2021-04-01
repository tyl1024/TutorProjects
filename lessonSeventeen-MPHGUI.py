'''
Created on Apr 19, 2020

@author: 1024t
'''

#graphics.py
#animations
#game development


'''
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb

root = Tk()
root.title("Converter")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 300, padx = 300)

# Create a Tkinter variable
tkvar = StringVar(root)
tkvar2 = StringVar(root)

# Dictionary with options
choices = { 'MPH','KMPH','Euros','US Dollars'}
choices2 = { 'MPH','KMPH','Euros','US Dollars'}
tkvar.set('MPH') # set the default option
tkvar2.set('KMPH') # set the default option


popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose one:").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column = 1)

popupMenu2 = OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text="Choose another:").grid(row = 1, column = 3)
popupMenu2.grid(row = 2, column = 3)


tk.Label(mainframe, text="Enter Data:").grid(row=3)

e1 = tk.Entry(mainframe)
e2 = tk.Entry(mainframe)

e1.grid(row=3, column=3)
e2.grid(row=3, column=1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get())
    
def change_dropdown(*args):
    print( tkvar2.get())

# link function to change dropdown
tkvar.trace('w', change_dropdown)
tkvar2.trace('w', change_dropdown)


root.mainloop()
'''


'''
#add rlabel to call_convert function
#in if statement, add conversion
#go to line 140 and add rlabel
#add word to dropdown list
#add label to line 153 in call_convert variable



import sys
import tkinter as tk
from functools import partial
 
# global variable
tempVal = "Celsius"                 #flag variable...if dropdown menu is celsius, do that
 
 
# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp
 
 
# the main conversion
def call_convert(rlabel1, rlabe12,rlabel3, inputn):   #add new rlabels for each conversion we add
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        yeet = float((float(tem) + 9))
        rlabel1.config(text="%f Fahrenheit" % f)    #this is where conversions and print statements are done
        rlabe12.config(text="%f Kelvin" % k)  
        rlabel3.config(text="%f Yeet" % yeet)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
    return

def exit():
    sys.exit()
 
 
# app window configuration and UI
root = tk.Tk()                                     #creating the GUI that pops up
root.geometry('600x150+100+100')                    #width and height     100 100 is where it shows up on computer
root.title('Temperature Converter')         #title in top left of gui
root.configure(background='#09A3BA')        #background
root.resizable(width=False, height=False)    #makes it impossible to resize
root.grid_columnconfigure(1, weight=1)   
root.grid_rowconfigure(0, weight=1)
 
numberInput = tk.StringVar()            #number user enters variable
var = tk.StringVar()
 
# label and entry field
input_label = tk.Label(root, text="Enter temperature", background='#09A3BA', foreground="#FFFFFF")  #label prints enter temprature
input_entry = tk.Entry(root, textvariable=numberInput)    #input box that shows up
input_label.grid(row=1)      #places label and entry box in rows and column
input_entry.grid(row=1, column=1)   #places label and entry box in rows and column
 
# result label's for showing the other two temperatures
result_label1 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")     #print statement on GUI
result_label1.grid(row=3, columnspan=4)

result_label2 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)

result_label3 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label3.grid(row=5, columnspan=4)

 
# drop down initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin","YEET"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)    #creates drop down menu
var.set(dropDownList[0])                                                  #celsius as first value in drop down
dropdown.grid(row=1, column=3)   #placing in spot on gui
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")   #unneed but its the way to change background
 
# button click
call_convert = partial(call_convert, result_label1, result_label2,result_label3, numberInput)   #calling our convert function up top
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")   #create convert button
result_button.grid(row=2, columnspan=4)         #place button


root.mainloop()
'''
























import tkinter as tk
from functools import partial
 
# global variable
tempVal = "Celsius"
 
 
# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp
 
 
# the main conversion
def call_convert(rlabel1, rlabe12,rlabel3,rlabel4, inputn):
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        MPH = float((float(tem) * 1.609344))
        KMPH = float((float(tem) / 1.609344))
        rlabel1.config(text="%f Fahrenheit" % f)
        rlabe12.config(text="%f Kelvin" % k)
        #rlabel3.config(text="%f MPH" % MPH)
        #rlabel4.config(text="%f KMPH" % KMPH)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        MPH = float((float(tem) * 1.609344))
        KMPH = float((float(tem) / 1.609344))
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Kelvin" % k)
        rlabel3.config(text="%f MPH" % MPH)
        rlabel4.config(text="%f KMPH" % KMPH)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        MPH = float((float(tem) * 1.609344))
        KMPH = float((float(tem) / 1.609344))
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
        rlabel3.config(text="%f MPH" % MPH)
        rlabel4.config(text="%f KMPH" % KMPH)
    if tempVal == 'MPH':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        MPH = float((float(tem) * 1.609344))
        KMPH = float((float(tem) / 1.609344))
        k = c + 273
        #rlabel1.config(text="%f Celsius" % c)
        #rlabe12.config(text="%f Fahrenheit" % f)
        rlabel4.config(text="%f KMPH" % KMPH)
        #rlabel3.config(text="%f Kelvin" % k)
    if tempVal == 'KMPH':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        k = c + 273
        MPH = float((float(tem) * 1.609344))
        KMPH = float((float(tem) / 1.609344))
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
        rlabel4.config(text="%f MPH" % MPH)
        rlabel3.config(text="%f Kelvin" % k)

    return
 
 
# app window configuration and UI
root = tk.Tk()
root.geometry('400x200')
root.title('Unit Converter')
root.resizable(width=False, height=False)

 
numberInput = tk.StringVar()
var = tk.StringVar()
 
# label and entry field
input_label = tk.Label(root, text="Enter Unit you want converted")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)
 
# result label's for showing the other two temperatures
result_label1 = tk.Label(root)
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root)
result_label2.grid(row=4, columnspan=4)
result_label3 = tk.Label(root)
result_label3.grid(row=5, columnspan=4)
result_label4 = tk.Label(root)
result_label4.grid(row=6, columnspan=4)
 
# drop down initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin","MPH","KMPH"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)

 
# button click
call_convert = partial(call_convert, result_label1, result_label2, result_label3, result_label4, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)
 
root.mainloop()



