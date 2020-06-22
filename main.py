import pygame, random

displayWidth = 1280
displayHeight = 720
scale = 16
state = 0
score = 0
gridWidth = displayWidth / scale
gridHeight = displayHeight / scale
tick = 5
border = 2

#0 = up
#1 = right
#2 = down
#3 = left
snakeD = 0
snakeX = [0]
snakeY = [0]
snakeL = 1

fTick = 0
nextF = 6


foodX = 0
foodY = 0

background = (0,0,0)
snakeC = (125,125,125)
foodC = (128,0,0)
white = (255,255,255)
green = (0,128,0)
blue = (0,0,128)
lPink = (255,102,204)
lPurple = (170, 109, 209)

#Button function
def button(msg, x, y, w, h, ic, ac, pc, action=None):
    global gameDisplay
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
    text = font.render(msg, True, ic, ac)
    textRect = text.get_rect()  
    textRect.center = (int(x + w / 2) , int(y + h / 2))
    gameDisplay.blit(text, textRect)
    if x + w > mouse[0] > x and y + h  > mouse[1] > y:
        pygame.draw.rect(gameDisplay, pc, (x, y, w, h))
        text = font.render(msg, True, ic, pc)
        textRect = text.get_rect()  
        textRect.center = (int(x + w / 2) , int(y + h / 2))
        gameDisplay.blit(text, textRect)
        if click[0] == 1 and action is not None:
            action()

#Shortcut version of random int
def rand(x, y):
    if y < x:
        return random.randint(y, x)
    else:
        return random.randint(x, y)

#Food location randomizer
def foodR():
    global foodX, foodY, gridWidth, gridHeight, nextF, snakeX, snakeY
    staX = 1
    staY = 3
    midX = int(gridWidth / 2)
    midY = int(gridHeight / 2 + 2)
    endX = int(gridWidth - 2)
    endY = int(gridHeight - 2)

    X1 = 0
    X2 = 0
    Y1 = 0
    Y2 = 0

    if snakeX[0] >= midX:
        staX = int(gridWidth - 2)
        endX = 1
    if snakeY[0] >= midY:
        staY = int(gridHeight - 2)
        endY = 3

    tempR = rand(0, 8)
    done = 1
    if tempR <= 3:
        X1 = staX
        X2 = midX
        Y1 = staY
        Y2 = midY
    elif tempR <= 5:
        X1 = staX
        X2 = midX
        Y1 = midY
        Y2 = endY
    elif tempR <= 7:
        X1 = midX
        X2 = endX
        Y1 = staY
        Y2 = midY
    else:
        X1 = midX
        X2 = endX
        Y1 = midY
        Y2 = endY
    while done == 1:
        foodX = rand(X1, X2)
        foodY = rand(Y1, Y2)
        done = 0
        for x in range(snakeL):
            if snakeX[x] == foodX and snakeY[x] == foodY:
                done = 1
                print("Overlap")   
        print(tempR)
        print("foodX ", foodX)
        print("FoodY ", foodY)
        print(str(X1) + " " + str(X2))
        print(str(Y1) + " " + str(Y2))
    if nextF > 1: 
        nextF -= 1

#Resetting game back to it's starting position
def gameStart():
    global score, state, snakeX, snakeY, foodX, foodY, gridWidth, gridHeight, snakeD, snakeL, snakeC, foodC, nextF
    #Resetting stats
    score = 0
    state = 0
    snakeX = [int(gridWidth/2),int(gridWidth/2),int(gridWidth/2)]
    snakeY = [int(gridHeight/2),int(gridHeight/2),int(gridHeight/2)]
    snakeD = 0
    snakeL = 3
    done = 1
    while done == 1:
        foodX = rand(1, gridWidth - 2)
        foodY = rand(3, gridHeight - 2)
        done = 0
        for x in range(snakeL):
            if snakeX[x] == foodX and snakeY[x] == foodX:
                done = 1
    #Colour generation
    snakeC = (0,0,255)
    foodC = (255,0,0)
    nextF = 6

#Everything the game should do every tick
def gameTick():
    global snakeD, snakeY, snakeX, snakeL, state, gridHeight, gridWidth, score, scale
    #Moving the rest of the snake's body
    for x in range(0, snakeL - 1):
        if x != snakeL:
            snakeY[snakeL - x - 1] = snakeY[snakeL - x - 2]
            snakeX[snakeL - x - 1] = snakeX[snakeL - x - 2]

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

    
    #Checking to see if the snake dies
    if snakeX[0] < 1 or  snakeY[0] < 3 or snakeX[0] > gridWidth - 2 or snakeY[0] > gridHeight - 2:
        state = 1
    for x in range(3,snakeL):
        if snakeX[0] == snakeX[x] and snakeY[0] == snakeY[x]:
            state = 1
    
    #Checking collision between the snake and the food
    if snakeX[0] == foodX and snakeY[0] == foodY:
        score += 7 - nextF
        foodR()
        snakeL += 1
        snakeY.append(snakeY[-1])
        snakeX.append(snakeX[-1])

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snaky boi')
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score: ' + str(score), True, green, background)
textRect = text.get_rect()  
textRect.center = (int(displayWidth / 2) , scale)
gameStart()
ticker = 0
locked = 0
menu = 0

def cont():
    global menu
    menu = 1

while menu == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(background)
    button("Start", 525, 250, 300, 60, blue, lPink, lPurple, cont)
    pygame.display.update()
while state == 0 :
    clock.tick(60)

    #User input management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snakeD != 2 and locked == 0:
                snakeD = 0
                locked = 1
            elif event.key == pygame.K_DOWN and snakeD != 0 and locked == 0:
                snakeD = 2
                locked = 1
            elif event.key == pygame.K_LEFT and snakeD != 1 and locked == 0:
                snakeD = 3
                locked = 1
            elif event.key == pygame.K_RIGHT and snakeD != 3 and locked == 0:
                snakeD = 1
                locked = 1
    #Framerate control
    if(ticker < nextF):
        ticker += 1
        continue
    else:
        ticker = 0
        locked = 0 
    if nextF < 6:
        if fTick == 100:
            nextF += 1
            fTick = 0
        else:
            fTick += 1
    #The start of display management 
    gameDisplay.fill(background)
    for x in range(0, snakeL):
        pygame.draw.rect(gameDisplay,white,(snakeX[x] * scale, snakeY[x] * scale, scale, scale))
        pygame.draw.rect(gameDisplay,snakeC,(snakeX[x] * scale + 2, snakeY[x] * scale + 2, scale - 4, scale - 4))
    
    #Checking food collision
    if snakeX[0] == foodX and snakeY[0] == foodY:
        foodR()
    
    #Drawing the food
    pygame.draw.rect(gameDisplay,white,(foodX * scale, foodY * scale, scale, scale))
    pygame.draw.rect(gameDisplay,foodC,(foodX * scale + 2, foodY * scale + 2, scale - 4, scale - 4))

    #Drawing the playing field
    pygame.draw.line(gameDisplay, white, (scale, scale * 3), (displayWidth - scale, scale * 3))
    pygame.draw.line(gameDisplay, white, (displayWidth - scale, scale * 3), (displayWidth - scale, displayHeight - scale))
    pygame.draw.line(gameDisplay, white, (displayWidth - scale, displayHeight - scale), (scale, displayHeight - scale))
    pygame.draw.line(gameDisplay, white, (scale, displayHeight - scale), (scale, scale * 3))

    #Drawing the score
    text = font.render('Score: ' + str(score), True, green, background)
    gameDisplay.blit(text, textRect) 
    gameTick()
    #Updating the display
    pygame.display.update()