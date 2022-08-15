import pygame

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

# Fire1
fire1_image = pygame.image.load('fire.png')
fire1X = 70
fire1Y = 100
fire1X_change = 3
fire1Y_change = 3

# Fire2
fire2_image = pygame.image.load('fire2.png')
fire2X = 200
fire2Y = 400
fire2X_change = -3
fire2Y_change = 3

# Fire3
fire3_image = pygame.image.load('fire2.png')
fire3X = 400
fire3Y = 200
fire3X_change = -3
fire3Y_change = -3

# Fire4
fire4_image = pygame.image.load('fire2.png')
fire4X = 600
fire4Y = 300
fire4X_change = -3
fire4Y_change = 3


def player(x, y):
    screen.blit(player_image, (x, y))

def fire1(x, y):
    screen.blit(fire1_image, (x, y))

def fire2(x, y):
    screen.blit(fire2_image, (x, y))

def fire3(x, y):
    screen.blit(fire3_image, (x, y))

def fire4(x, y):
    screen.blit(fire4_image, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Colour
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

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
        fire3X_change = 3
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


    # keystrokes and boundaries(player)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3.0
        if event.key == pygame.K_RIGHT:
            playerX_change = 3.0
        if event.key == pygame.K_UP:
            playerY_change = -3.0
        if event.key == pygame.K_DOWN:
            playerY_change = 3.0
        if playerX <= 0:
            playerX = 0
        elif playerX >= 720:
            playerX = 720
        if playerY <= 0:
            playerY = 0
        elif playerY >= 500:
            playerY = 500
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
    fire1(fire1X, fire1Y)
    fire2(fire2X, fire2Y)
    fire3(fire3X, fire3Y)
    fire4(fire4X, fire4Y)

    pygame.display.update()

