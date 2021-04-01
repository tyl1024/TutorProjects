'''
Created on Mar 1, 2020
@author: Tyler
'''

def main():
    intro()
    userInput()
    again = input("\n\nWould you like to convert something else? (y/n): ")
    num = 0
    while (num < 5):
        num = num + 1
        if (again == "yes") or (again == "y") or (again == "Yes"):
            userInput()
    else:
            print("Thank you for using the converter! Come again!")
    
def intro():
    print("This program is a converter for mph-km, farenheit-celsius, inch-centimeter\n\n")
    
def userInput():
    user = input("\nEnter what you would like to convert...(ex. mph, km, celsius, inch) ")
    if (user == "mph") or (user == "MPH") or (user == "m"):
        amount = eval(input("\nEnter the MPH you would like to convert: "))
        #1 mph = 1.609344 km/h
        mph = amount * 1.609344
        print(amount ,"MPH is", mph, "KM")
    if (user == "km") or (user == "KM") or (user == "k"):
        amount = eval(input("\nEnter the KM you would like to convert: "))
        #1 mph = 1.609344 km/h
        km = amount / 1.609344
        print(amount ,"KM is", km, "MPH")
    
    
    
    
    
    
main()