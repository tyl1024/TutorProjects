'''
Created on Jun 21, 2020

@author: 1024t
'''

list = [-15,-26,-1,-23.5,7,2,10]
new_list = []  

while list:
    min = list[0]
    for x in list:
        if x < min:
            min = x
    new_list.append(min)
    list.remove(min)
print(new_list)




test = [-15,-26,-1,-23,7,2,10]
test.sort()
print(test)


