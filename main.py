import pygame
import math

# initialising the game
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))


#bg
background = pygame.image.load('bg.png')

# Title and icon
pygame.display.set_caption("Fireball")
icon = pygame.image.load('maze.png')
pygame.display.set_icon(icon)



# Player
player_image = pygame.image.load('player.png')
playerX = 360
playerY = 10
playerX_change = 0
playerY_change = 0

#Bombs
Bomb1_image = pygame.image.load('Bomb.png')
Bomb2_image = pygame.image.load('Bomb.png')
Bomb3_image = pygame.image.load('Bomb.png')
Bomb4_image = pygame.image.load('Bomb.png')

Bomb1X = 70
Bomb1Y = 100

Bomb2X = 200
Bomb2Y = 400

Bomb3X = 400
Bomb3Y = 200

Bomb4X = 600
Bomb4Y = 300

# fires
fire_images = []
fireX = []
fireY = []
fireX_change = []
fireY_change = []

# Fire1
fire1_image = pygame.image.load('fire.png')
fire1X = 70
fire1Y = 100
fire1X_change = 3
fire1Y_change = 3
fireX.append(fire1X)
fireY.append(fire1Y)
fireX_change.append(fire1X_change)
fireY_change.append(fire1Y_change)

# Fire2
fire2_image = pygame.image.load('fire2.png')
fire2X = 200
fire2Y = 400
fire2X_change = -3
fire2Y_change = 3
fireX.append(fire2X)
fireY.append(fire2Y)
fireX_change.append(fire2X_change)
fireY_change.append(fire2Y_change)

# Fire3
fire3_image = pygame.image.load('fire2.png')
fire3X = 400
fire3Y = 200
fire3X_change = -3
fire3Y_change = -3
fireX.append(fire3X)
fireY.append(fire3Y)
fireX_change.append(fire3X_change)
fireY_change.append(fire3Y_change)

# Fire4
fire4_image = pygame.image.load('fire2.png')
fire4X = 600
fire4Y = 300
fire4X_change = -3
fire4Y_change = 3
fireX.append(fire4X)
fireY.append(fire4Y)
fireX_change.append(fire4X_change)
fireY_change.append(fire4Y_change)

# Fire5
fire5_image = pygame.image.load('fire2.png')
fire5X = 600
fire5Y = 300
fire5X_change = -3
fire5Y_change = 3
fireX.append(fire5X)
fireY.append(fire5Y)
fireX_change.append(fire5X_change)
fireY_change.append(fire5Y_change)


# Fire6
fire6_image = pygame.image.load('fire2.png')
fire6X = 400
fire6Y = 200
fire6X_change = -3
fire6Y_change = -3
fireX.append(fire6X)
fireY.append(fire6Y)
fireX_change.append(fire6X_change)
fireY_change.append(fire6Y_change)

# Fire7
fire7_image = pygame.image.load('fire2.png')
fire7X = 200
fire7Y = 400
fire7X_change = -3
fire7Y_change = 3
fireX.append(fire7X)
fireY.append(fire7Y)
fireX_change.append(fire7X_change)
fireY_change.append(fire7Y_change)

# Fire8
fire8_image = pygame.image.load('fire2.png')
fire8X = 70
fire8Y = 100
fire8X_change = 3
fire8Y_change = 3
fireX.append(fire8X)
fireY.append(fire8Y)
fireX_change.append(fire8X_change)
fireY_change.append(fire8Y_change)

# Fire9
fire9_image = pygame.image.load('fire2.png')
fire9X = 70
fire9Y = 100
fire9X_change = 3
fire9Y_change = 3
fireX.append(fire9X)
fireY.append(fire9Y)
fireX_change.append(fire9X_change)
fireY_change.append(fire9Y_change)

# Fire10
fire10_image = pygame.image.load('fire2.png')
fire10X = 200
fire10Y = 400
fire10X_change = -3
fire10Y_change = 3
fireX.append(fire10X)
fireY.append(fire10Y)
fireX_change.append(fire10X_change)
fireY_change.append(fire10Y_change)

# Fire11
fire11_image = pygame.image.load('fire2.png')
fire11X = 400
fire11Y = 200
fire11X_change = -3
fire11Y_change = -3
fireX.append(fire11X)
fireY.append(fire11Y)
fireX_change.append(fire11X_change)
fireY_change.append(fire11Y_change)

# Fire12
fire12_image = pygame.image.load('fire2.png')
fire12X = 600
fire12Y = 300
fire12X_change = -3
fire12Y_change = 3
fireX.append(fire12X)
fireY.append(fire12Y)
fireX_change.append(fire12X_change)
fireY_change.append(fire12Y_change)


font = pygame.font.Font('freesansbold.ttf',32)

seconds = 0

textX = 10
textY = 10

# Game over
Gameover_font = pygame.font.Font('freesansbold.ttf', 30)


def show_time(x, y):
    time = font.render("Time :" + str(seconds), True, (255, 255, 255))
    screen.blit(time, (x, y))


def win():
    winning = font.render("YOU WON!!", True, (255, 255, 255))
    screen.fill('Black')
    screen.blit(winning, (250, 250))

def game_over():
    over = Gameover_font.render("GAME OVER! YOU SURVIVED " + str(final_times[0]) + " SECONDS", True, (255, 255, 255))
    screen.blit(over, (50, 250))

def player(x, y):
    screen.blit(player_image, (x, y))

def bomb1(x,y):
    screen.blit(Bomb1_image, (x, y))

def bomb2(x,y):
    screen.blit(Bomb2_image, (x, y))

def bomb3(x,y):
    screen.blit(Bomb3_image, (x, y))

def bomb4(x,y):
    screen.blit(Bomb4_image, (x, y))

def fire1(x, y):
    screen.blit(fire1_image, (x, y))

def fire2(x, y):
    screen.blit(fire2_image, (x, y))

def fire3(x, y):
    screen.blit(fire3_image, (x, y))

def fire4(x, y):
    screen.blit(fire4_image, (x, y))

def fire5(x, y):
    screen.blit(fire5_image, (x, y))

def fire6(x, y):
    screen.blit(fire6_image, (x, y))

def fire7(x, y):
    screen.blit(fire7_image, (x, y))

def fire8(x, y):
    screen.blit(fire8_image, (x, y))

def fire9(x, y):
    screen.blit(fire9_image, (x, y))

def fire10(x, y):
    screen.blit(fire10_image, (x, y))

def fire11(x, y):
    screen.blit(fire11_image, (x, y))

def fire12(x, y):
    screen.blit(fire12_image, (x, y))

def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX-playerX,2)+math.pow(enemyY-playerY,2))
    return distance < 32


#starter tick
start_ticks = pygame.time.get_ticks()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Colour
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))


    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds




    if fire1X <= 0:
        fire1X_change = 3
        fire1Y_change = 3
    elif fire1X >= 750:
        fire1X_change = -3
        fire1Y_change = 0
    if fire1Y <= 0:
        fire1X_change = 0
        fire1Y_change = 2
    elif fire1Y >= 550:
        fire1X_change = 3
        fire1Y_change = -3

    if fire2X <= 0:
        fire2X_change = 3
        fire2Y_change = 3
    elif fire2X >= 750:
        fire2X_change = -3
        fire2Y_change = 3
    if fire2Y <= 0:
        fire2X_change = -3
        fire2Y_change = 3
    elif fire2Y >= 550:
        fire2X_change = 0
        fire2Y_change = -3

    if fire3X <= 0:
        fire3X_change = 5
        fire3Y_change = 3
    elif fire3X >= 750:
        fire3X_change = -3
        fire3Y_change = 3
    if fire3Y <= 0:
        fire3X_change = -3
        fire3Y_change = 3
    elif fire3Y >= 550:
        fire3X_change = 0
        fire3Y_change = -3

    if fire4X <= 0:
        fire4X_change = 3
        fire4Y_change = 3
    elif fire4X >= 750:
        fire4X_change = -3
        fire4Y_change = 3
    if fire4Y <= 0:
        fire4X_change = -3
        fire4Y_change = 3
    elif fire4Y >= 550:
        fire4X_change = 0
        fire4Y_change = -3

        # break
    if fire8X <= 0:
        fire8X_change = 3
        fire8Y_change = 3
    elif fire8X >= 750:
        fire8X_change = -3
        fire8Y_change = 0
    if fire8Y <= 0:
        fire8X_change = 0
        fire8Y_change = 2
    elif fire8Y >= 550:
        fire8X_change = 3
        fire8Y_change = -3

    if fire7X <= 0:
        fire7X_change = 3
        fire7Y_change = 3
    elif fire7X >= 750:
        fire7X_change = -3
        fire7Y_change = 3
    if fire7Y <= 0:
        fire7X_change = -3
        fire7Y_change = 3
    elif fire7Y >= 550:
        fire7X_change = 0
        fire7Y_change = -3

    if fire6X <= 0:
        fire6X_change = 5
        fire6Y_change = 3
    elif fire6X >= 750:
        fire6X_change = -3
        fire6Y_change = 3
    if fire6Y <= 0:
        fire6X_change = -3
        fire6Y_change = 3
    elif fire6Y >= 550:
        fire6X_change = 0
        fire6Y_change = -3

    if fire5X <= 0:
        fire5X_change = 3
        fire5Y_change = 3
    elif fire5X >= 750:
        fire5X_change = -3
        fire5Y_change = 3
    if fire5Y <= 0:
        fire5X_change = -3
        fire5Y_change = 3
    elif fire5Y >= 550:
        fire5X_change = 0
        fire5Y_change = -3
        # break

    if fire9X <= 0:
        fire9X_change = 3
        fire9Y_change = 3
    elif fire9X >= 750:
        fire9X_change = -3
        fire9Y_change = 0
    if fire9Y <= 0:
        fire9X_change = 0
        fire9Y_change = 2
    elif fire9Y >= 550:
        fire9X_change = 3
        fire9Y_change = -3

    if fire10X <= 0:
        fire10X_change = 3
        fire10Y_change = 3
    elif fire10X >= 750:
        fire10X_change = -3
        fire10Y_change = 3
    if fire10Y <= 0:
        fire10X_change = -3
        fire10Y_change = 3
    elif fire10Y >= 550:
        fire10X_change = 0
        fire10Y_change = -3

    if fire11X <= 0:
        fire11X_change = 5
        fire11Y_change = 3
    elif fire11X >= 750:
        fire11X_change = -3
        fire11Y_change = 3
    if fire11Y <= 0:
        fire11X_change = -3
        fire11Y_change = 3
    elif fire11Y >= 550:
        fire11X_change = 0
        fire11Y_change = -3

    if fire12X <= 0:
        fire12X_change = 3
        fire12Y_change = 3
    elif fire12X >= 750:
        fire12X_change = -3
        fire12Y_change = 3
    if fire12Y <= 0:
        fire12X_change = -3
        fire12Y_change = 3
    elif fire12Y >= 550:
        fire12X_change = 0
        fire12Y_change = -3

    # keystrokes and boundaries(player)
    if event.type == pygame.KEYDOWN:
        if playerX <= 0:
            playerX = 0
        elif playerX >= 726:
            playerX = 726
        elif playerY <= 0:
            playerY = 0
        elif playerY >= 550:
            playerY = 550
        if event.key == pygame.K_LEFT:
            playerX_change = -3.0
        if event.key == pygame.K_RIGHT:
            playerX_change = 3.0
        if event.key == pygame.K_UP:
            playerY_change = -3.0
        if event.key == pygame.K_DOWN:
            playerY_change = 3.0

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    

    playerX += playerX_change
    playerY += playerY_change
    fire1X += fire1X_change
    fire1Y += fire1Y_change
    fire2X += fire2X_change
    fire2Y += fire2Y_change
    fire3X += fire3X_change
    fire3Y += fire3Y_change
    fire4X += fire4X_change
    fire4Y += fire4Y_change



    player(playerX, playerY)
    bomb1(Bomb1X,Bomb1Y)
    bomb2(Bomb2X, Bomb2Y)
    bomb3(Bomb3X, Bomb3Y)
    bomb4(Bomb4X, Bomb4Y)

    fire1(fire1X, fire1Y)
    fire2(fire2X, fire2Y)
    fire3(fire3X, fire3Y)
    fire4(fire4X, fire4Y)


    if seconds > 10:
        fire5(fire5X, fire5Y)
        fire5X += fire5X_change
        fire5Y += fire5Y_change
    if seconds > 20:
        fire6(fire6X, fire6Y)
        fire6X += fire6X_change
        fire6Y += fire6Y_change
    if seconds > 30:
        fire7(fire7X, fire7Y)
        fire7X += fire7X_change
        fire7Y += fire7Y_change
    if seconds > 40:
        fire8(fire8X, fire8Y)
        fire8X += fire8X_change
        fire8Y += fire8Y_change
    if seconds > 50:
        fire9(fire9X, fire9Y)
        fire9X += fire9X_change
        fire9Y += fire9Y_change
    if seconds > 60:
        fire10(fire10X, fire10Y)
        fire10X += fire10X_change
        fire10Y += fire10Y_change

    if seconds > 70:
        fire11(fire11X, fire11Y)
        fire11X += fire11X_change
        fire11Y += fire11Y_change

    if seconds > 80:
        fire12(fire12X, fire12Y)
        fire12X += fire12X_change
        fire12Y += fire12Y_change

    if seconds > 90:
        win()

    collisions = []
    collisions.append(isCollision(fire1X, fire1Y, playerX, playerY))
    collisions.append(isCollision(fire2X, fire2Y, playerX, playerY))
    collisions.append(isCollision(fire3X, fire3Y, playerX, playerY))
    collisions.append(isCollision(fire4X, fire4Y, playerX, playerY))
    collisions.append(isCollision(fire5X, fire5Y, playerX, playerY))
    collisions.append(isCollision(fire6X, fire6Y, playerX, playerY))
    collisions.append(isCollision(fire7X, fire7Y, playerX, playerY))
    collisions.append(isCollision(fire8X, fire8Y, playerX, playerY))
    collisions.append(isCollision(fire9X, fire9Y, playerX, playerY))
    collisions.append(isCollision(fire10X, fire10Y, playerX, playerY))
    collisions.append(isCollision(fire11X, fire11Y, playerX, playerY))
    collisions.append(isCollision(fire12X, fire12Y, playerX, playerY))

    for i in range(len(collisions)):
        if collisions[i]:
            end_time = pygame.time.get_ticks()
            playerX = 200
            playerY = 400
            playerX_change = 0
            playerY_change = 0
            screen.fill('Black')
            seconds_survived = (end_time - start_ticks) // 1000
            final_times = []
            final_times.append(seconds_survived)
            over = Gameover_font.render("GAME OVER! YOU SURVIVED " + str(final_times[0]) + " SECONDS", True,
                                        (255, 255, 255))
            screen.blit(over, (50, 250))

    show_time(textX, textY)
    pygame.display.update()
