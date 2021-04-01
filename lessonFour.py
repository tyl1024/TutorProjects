'''
#        Write a function called fizz_buzz that takes a number.
#        If the number is divisible by 3, show Fizz.
#        If it is divisible by 5, show Buzz.
#        If it is divisible by both 3 and 5, show FizzBuzz.
#        Otherwise, blah
'''

'''
def fizz_buzz(x):
    if (x % 15 == 0):
        return "fizzBuzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0: 
        return "buzz" 
    else:
        return "Blah"
    
#print(fizz_buzz(-7))
'''



'''
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print Ok.
Otherwise, for every 5mph above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: Points: 2.
If the driver gets more than 12 points, the function should print: License suspended
'''
'''
def speed_checker(speed):
    if speed <= 70:
        print("Ok")
    elif speed > 70:
        newSpeed = speed - 70
        print(newSpeed , " over the speed limit")
        points = float(newSpeed / 5) 
        meritPoints = round(points,5)
        print("you received " , meritPoints , "merit Points")
        if meritPoints > 12:
            print("License suspeneded for getting 12 points or more")
        
speed_checker(135)
'''

'''
#number of rows
for i in range(0, 5): 
      
        # inner loop to handle number of columns 
        for j in range(0, 2): 
          
            # printing stars 
            print("*",end="") 
       
        # ending line after each row 
        print("") 
'''
        




'''
def rightTriangle(num): 
      
    # outer loop to handle number of rows 
    # n in this case 
    for i in range(0, num): 
      
        # inner loop to handle number of columns 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("") 
  
rightTriangle(5)
'''
    

        
        
        
        