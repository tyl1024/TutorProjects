'''
Created on Apr 13, 2020

@author: 1024t
'''
import time
import winsound
from playsound import playsound
import tkinter as tk
from tkinter import messagebox as mb


root=tk.Tk()
scrW = root.winfo_screenwidth()
scrH = root.winfo_screenheight()




print("What would you like to be reminded about:")
text = str(input(()))

print("How many seconds?")
localTime = float(input())
localTime = localTime * 5
time.sleep(localTime)
print(text)

mb.showinfo(text)
#winsound.Beep(5000, 10000)  # Beep at 1000 Hz for 100 ms
playsound('lol.mp3')
