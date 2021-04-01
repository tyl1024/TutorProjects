'''
Created on Apr 26, 2020

@author: 1024t
'''
'''
#creating the pop up box and then disappearing. We want it to stay up as long as game is not over
import pygame                                   #import pygame
pygame.init()                                   #create the box that pops up
dis=pygame.display.set_mode((400,300))          #geometry thing like when making GUIs... this sets how big the game is
pygame.display.update()                         #update game
pygame.quit()                                   #be able to exit game
quit()   
'''                                       #quit


'''
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game')
game_over=False   #flag variable to false
while not game_over:   #while game is not over
    for event in pygame.event.get():   #this loops through mouse and keyboard movements and prints what we are doing
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()
'''

'''
#It will not print out mouse events but it will let us quit now
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game')
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True      #if quit is clicked..quit
 
pygame.quit()
quit()
'''



'''
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
 
pygame.display.set_caption('Snake game')
 
blue=(0,0,255)
red=(255,0,0)
 
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,blue,[200,150,10,10])    #this creates blue square and puts it at the coordinates we want it at
    pygame.display.update()
pygame.quit()
quit()
'''


'''
import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)  #RGB

 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')
 
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0      #these variables are used for moving    
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:    #if key is pressed...this is built in function in pygame
            if event.key == pygame.K_LEFT:     #lrft arrow is pressed
                x1_change = -10      #sending block to the left -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change    #the block at 300,300...adding the up value to it over and over again
    y1 += y1_change
    dis.fill(white)     #changing the blackgroung color of the display
    pygame.draw.rect(dis, black, [x1, y1, 20, 20])      #place block at 300,300  ...making it 10 pixels long and 10 pixels high
 
    pygame.display.update()   #update
 
    clock.tick(30)    #this is the speed up of the snake
 
pygame.quit()
quit()
'''



#YOU LOST SCREEN
'''
import pygame
import time
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))   #GUI width and height
pygame.display.set_caption('Snake Game')
 
game_over = False
 
x1 = dis_width/2      #This is placing the snake block in the center of the screen
y1 = dis_height/2
 
snake_block=10
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=30
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:    #if the snake leaves the screen. set gameover to true and quit game
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])   #drawing the snake. x1,y1 is movement and snake block is the size of the snake
 
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost",red)   #pygame built in the types a message
pygame.display.update()
time.sleep(2)    #show you lost screen for 2 seconds and thens quit game
 
pygame.quit()
quit()
'''


'''
#Eat food and print yummy. Check to see if it is colliding. Loop to play again or quit

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30)      #This is to change the font of you lost
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])       #color changing funtion
 
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2    #centering the snake
 
    x1_change = 0    
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0     #creates food in random spot
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #food is same size as snake
 
    while not game_over:
        while game_close == True:   #We lost so
            dis.fill(white)    #background color to white and print you lost message
            message("You Lost! Press Q-Quit or C-Play Again", red)  #press c or q to play again or quit
            pygame.display.update()  #call update to close game or play again
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:    #if q is pressed, quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:   #restart game using recursion
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0                              #snakes movements
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:     #you lost if reached out of bounds
            game_close = True
 
        x1 += x1_change      #incrememnting snake left and right
        y1 += y1_change      #up and down
        dis.fill(white)    #background color
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])   #draws the food in a random spot
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])        #draws the snake in the center
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
'''



import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2   #center the snake
    y1 = dis_height / 2
 
    x1_change = 0   #snakes movement
    y1_change = 0
 
    snake_List = []   #empty list
    Length_of_snake = 1   #
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0     #places food in random spot
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)    #game over screen
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:   #if q, quit..if c, play again
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:    #snake moves up,left, down and right
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True            #making sure snake doesn't leave the boundary
            
        x1 += x1_change
        y1 += y1_change        #moves snake
        dis.fill(blue)   #backgrund color
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])   #draws the food
        snake_Head = []             
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)    #adding another rectangle to our snake
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:  #if the head hits the tail
            if x == snake_Head:    #set game over
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:   #instead of print yummy.... we add 1 rectangle to the lenght of snake
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
