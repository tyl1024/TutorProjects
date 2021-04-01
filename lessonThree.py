'''
Created on Oct 8, 2019

@author: 1024t
'''
from test.test_wsgiref import hello_app
'''
x = int(1)  
print(x)
y = int(2.8) 
print(y)
x = float(1)
print(x)    
y = float(2.8)  
print(y) 
'''

'''
counter = 0
for i in range(10):
    counter += 1
    print(counter)
    '''
    


i = 0
while i <= 6:
  print(i)
  i += 1

    
    
'''   
i = 0
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  '''


'''
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
'''
    
'''  
thislist = ["apple", "banana", "cherry"]
thislist[1] = "watermelon"
print(thislist)
'''

'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, your fruit is not there")
    '''
    
'''   
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
'''
    
    
fileName = open("testFile.txt", "r")
print(fileName.read())
print(fileName.read(5))
fileName.close()

'''
f = open("testFile.txt", "a")   #append
f.write("\nHi")
f.close()
'''



'''
lessonEight = input("Enter your file: ")
print("You entered: " ,lessonEight)
fileOpener = open(lessonEight,"r")
print(fileOpener.read())
'''





'''
fileName = input("Enter the name of your file to count: ")

inFile = open(fileName, "r")
vowels = ("AEIOUaeiou")
cons = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

countV = 0
countC = 0
for text in inFile.read():
    if text in vowels:
        countV += 1
    elif text in cons:
        countC += 1

print("There are " , countV , " vowels in textfile and" , countC , " consonants.")

'''
    
