import pygame, random

displayWidth = 1280
displayHeight = 720
scale = 20
state = 0
score = 0
gridWidth = displayWidth / scale
gridHeight = displayHeight / scale

#0 = up
#1 = right
#2 = down
#3 = left
snakeD = 0
snakeX = 0
snakeY = 0
snakeL = 1

foodX = 0
foodY = 0

background = (0,0,0)
snakeC = (125,125,125)
foodC = (255,255,255)

#Shortcut version of random int
def rand(x, y):
    return random.randint(x, y)

#Resetting game back to it's starting position
def gameStart():
    #Resetting stats
    score = 0
    state = 0
    snakeX = int(gridWidth/2)
    snakeY = int(gridHeight/2)
    foodX = rand(10, gridWidth - 10)
    foodY = rand(10, gridHeight - 10)
    snakeD = 0

    #Colour generation
    snakeC = (0,0,255)
    foodC = (255,0,0)
