import pygame, random

displayWidth = 1280
displayHeight = 720
scale = 16
state = 0
score = 0
gridWidth = displayWidth / scale
gridHeight = displayHeight / scale
tick = 5

#0 = up
#1 = right
#2 = down
#3 = left
snakeD = 0
snakeX = [0]
snakeY = [0]
snakeL = 1

foodX = 0
foodY = 0

background = (0,0,0)
snakeC = (125,125,125)
foodC = (255,0,0)

#Shortcut version of random int
def rand(x, y):
    return random.randint(x, y)

#Food location randomizer
def foodR():
    global foodX, foodY, gridWidth, gridHeight
    foodX = rand(0, gridWidth - 1)
    foodY = rand(0, gridHeight - 1)

#Resetting game back to it's starting position
def gameStart():
    global score, state, snakeX, snakeY, foodX, foodY, gridWidth, gridHeight, snakeD, snakeL, snakeC, foodC
    #Resetting stats
    score = 0
    state = 0
    snakeX = [int(gridWidth/2)]
    snakeY = [int(gridHeight/2)]
    #foodX = rand(10, gridWidth - 10)
    #foodY = rand(10, gridHeight - 10)
    snakeD = 0
    snakeL = 1

    #Colour generation
    snakeC = (0,0,255)
    foodC = (255,0,0)

#Everything the game should do every tick
def gameTick():
    global snakeD, snakeY, snakeX, snakeL, state, gridHeight, gridWidth, score, scale
    #Moving the snake's head
    if snakeD == 0:
        snakeY[0] -= 1
    elif snakeD == 1:
        snakeX[0] += 1
    elif snakeD == 2:
        snakeY[0] += 1
    else:
        snakeX[0] -= 1
    snakeL = snakeL
    #Moving the rest of the snake's body
    for x in range(0, snakeL - 1):
        if x != snakeL:
            snakeY[snakeL - x - 1] = snakeY[snakeL - x - 2]
            snakeX[snakeL - x - 1] = snakeX[snakeL - x - 2]
    
    #Checking to see if the snake dies
    if snakeX[0] < 0 or  snakeY[0] < 0 or snakeX[0] > gridWidth - 1 or snakeY[0] > gridHeight - 1:
        state = 1
    for x in range(3,snakeL):
        if snakeX[0] == snakeX[x] and snakeY[0] == snakeY[x]:
            state = 1
    
    #Checking collision between the snake and the food
    if snakeX[0] == foodX and snakeY[0] == foodY:
        foodR()
        score += 1
        snakeL += 1
        snakeY.append(snakeY[-1])
        snakeX.append(snakeX[-1])

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snaky boi')
clock = pygame.time.Clock()
gameStart()
ticker = 0
while state == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snakeD != 2:
                snakeD = 0
            elif event.key == pygame.K_DOWN and snakeD != 0:
                snakeD = 2
            elif event.key == pygame.K_LEFT and snakeD != 1:
                snakeD = 3
            elif event.key == pygame.K_RIGHT and snakeD != 3:
                snakeD = 1
    if(ticker < 7):
        ticker += 1
        continue
    else:
        ticker = 0
    print(ticker)
    gameDisplay.fill(background)
    for x in range(0, snakeL):
        pygame.draw.rect(gameDisplay,snakeC,(snakeX[x] * scale, snakeY[x] * scale, scale, scale))
    if snakeX[0] == foodX and snakeY[0] == foodY:
        foodR()
    pygame.draw.rect(gameDisplay,foodC,(foodX * scale, foodY * scale, scale, scale))
    gameTick()
    pygame.display.update()