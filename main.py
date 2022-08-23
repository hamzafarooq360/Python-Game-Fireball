import pygame
import math

def game():

    end_time = pygame.time.get_ticks() / 1000

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
    class player:

        def __init__(self, playerX, playerY, playerX_change, playerY_change):
            self.playerX = playerX
            self.playerY = playerY
            self.playerX_change = playerX_change
            self.playerY_change = playerY_change

    p = player(360, 10, 0, 0)

    #Bombs
    Bomb_image = pygame.image.load('Bomb.png')


    class Bomb:
        def __init__(self, BombX, BombY):
            self.BombX = BombX
            self.BombY = BombY

    Bomb1 = Bomb(70, 100)
    Bomb2 = Bomb(200, 400)
    Bomb3 = Bomb(400, 200)
    Bomb4 = Bomb(600, 300)


    # Fires
    fire1_image = pygame.image.load('fire.png')

    class Fire:
        def __init__(self, FireX, FireY, FireX_change, FireY_Change):
            self.FireX = FireX
            self.FireY = FireY
            self.FireX_change = FireX_change
            self.FireY_change = FireY_Change


    # Fire1
    Fire1 = Fire(70, 100, 3, 3)

    # Fire2
    Fire2 = Fire(200, 400, -3, 3)

    # Fire3
    Fire3 = Fire(400, 200, -3, -3)

    # Fire4
    Fire4 = Fire(600, 300, -3, 3)

    # Fire5
    Fire5 = Fire(600, 300, -3, 3)

    # Fire6
    Fire6 = Fire(400, 200, -3, -3)


    # Fire7
    Fire7 = Fire(200, 400, -3, 3)

    # Fire8
    Fire8 = Fire(70, 100, 3, 3)

    # Fire9
    Fire9 = Fire(70, 100, 3, 3)

    # Fire10
    Fire10 = Fire(200, 400, -3, 3)

    # Fire11
    Fire11 = Fire(400, 200, -3, -3)

    # Fire12
    Fire12 = Fire(600, 300, -3, 3)

    font = pygame.font.Font('freesansbold.ttf',32)


    textX = 10
    textY = 10

    # Game over
    Gameover_font = pygame.font.Font('freesansbold.ttf', 30)
    survival_font = pygame.font.Font('freesansbold.ttf', 30)


    def show_time(x, y):
        time = font.render("Time:" + str(int(start_time-end_time)) + " Seconds", True, (255, 255, 255))
        screen.blit(time, (x, y))


    def win():
        screen.fill('Black')
        winning = font.render("YOU WON!! Press P to play again or Q to quit", True, (255, 255, 255))
        screen.blit(winning, (50, 250))

        p.playerX = 360
        p.playerY = 10
        p.playerX_change = 0
        p.playerY_change = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    elif event.key == pygame.K_p:
                        gameover = False
                        start_time = 0
                        game()

    def playerr(x, y):
        screen.blit(player_image, (x, y))

    def bomb(x,y):
        screen.blit(Bomb_image, (x, y))

    def fire(x, y):
        screen.blit(fire1_image, (x, y))


    def isCollision(enemyX, enemyY, playerX, playerY):
        distance = math.sqrt(math.pow(enemyX-playerX,2)+math.pow(enemyY-playerY,2))
        return distance < 32


    # Game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        start_time = pygame.time.get_ticks() / 1000

        # Colour
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))


        if Fire1.FireX <= 0:
            Fire1.FireX_change = 3
            Fire1.FireY_change = 3
        elif Fire1.FireX >= 750:
            Fire1.FireX_change = -3
            Fire1.FireY_change = 0
        if Fire1.FireY <= 0:
            Fire1.FireX_change = 0
            Fire1.FireY_change = 2
        elif Fire1.FireY >= 550:
            Fire1.FireX_change = 3
            Fire1.FireY_change = -3

        if Fire2.FireX <= 0:
            Fire2.FireX_change = 3
            Fire2.FireY_change = 3
        elif Fire2.FireX >= 750:
            Fire2.FireX_change = -3
            Fire2.FireY_change = 3
        if Fire2.FireY <= 0:
            Fire2.FireX_change = -3
            Fire2.FireY_change = 3
        elif Fire2.FireY >= 550:
            Fire2.FireX_change = 0
            Fire2.FireY_change = -3

        if Fire3.FireX <= 0:
            Fire3.FireX_change = 5
            Fire3.FireY_change = 3
        elif Fire3.FireX >= 750:
            Fire3.FireX_change = -3
            Fire3.FireY_change = 3
        if Fire3.FireY <= 0:
            Fire3.FireX_change = -3
            Fire3.FireY_change = 3
        elif Fire3.FireY >= 550:
            Fire3.FireX_change = 0
            Fire3.FireY_change = -3

        if Fire4.FireX <= 0:
            Fire4.FireX_change = 3
            Fire4.FireY_change = 3
        elif Fire4.FireX >= 750:
            Fire4.FireX_change = -3
            Fire4.FireY_change = 3
        if Fire4.FireY <= 0:
            Fire4.FireX_change = -3
            Fire4.FireY_change = 3
        elif Fire4.FireY >= 550:
            Fire4.FireX_change = 0
            Fire4.FireY_change = -3

            # break
        if Fire8.FireX <= 0:
            Fire8.FireX_change = 3
            Fire8.FireY_change = 3
        elif Fire8.FireX >= 750:
            Fire8.FireX_change = -3
            Fire8.FireY_change = 0
        if Fire8.FireY <= 0:
            Fire8.FireX_change = 0
            Fire8.FireY_change = 2
        elif Fire8.FireY >= 550:
            Fire8.FireX_change = 3
            Fire8.FireY_change = -3

        if Fire7.FireX <= 0:
            Fire7.FireX_change = 3
            Fire7.FireY_change = 3
        elif Fire7.FireX >= 750:
            Fire7.FireX_change = -3
            Fire7.FireY_change = 3
        if Fire7.FireY <= 0:
            Fire7.FireX_change = -3
            Fire7.FireY_change = 3
        elif Fire7.FireY >= 550:
            Fire7.FireX_change = 0
            Fire7.FireY_change = -3

        if Fire6.FireX <= 0:
            Fire6.FireX_change = 5
            Fire6.FireY_change = 3
        elif Fire6.FireX >= 750:
            Fire6.FireX_change = -3
            Fire6.FireY_change = 3
        if Fire6.FireY <= 0:
            Fire6.FireX_change = -3
            Fire6.FireY_change = 3
        elif Fire6.FireY >= 550:
            Fire6.FireX_change = 0
            Fire6.FireY_change = -3

        if Fire5.FireX <= 0:
            Fire5.FireX_change = 3
            Fire5.FireY_change = 3
        elif Fire5.FireX >= 750:
            Fire5.FireX_change = -3
            Fire5.FireY_change = 3
        if Fire5.FireY <= 0:
            Fire5.FireX_change = -3
            Fire5.FireY_change = 3
        elif Fire5.FireY >= 550:
            Fire5.FireX_change = 0
            Fire5.FireY_change = -3

        if Fire9.FireX <= 0:
            Fire9.FireX_change = 3
            Fire9.FireY_change = 3
        elif Fire9.FireX >= 750:
            Fire9.FireX_change = -3
            Fire9.FireY_change = 0
        if Fire9.FireY <= 0:
            Fire9.FireX_change = 0
            Fire9.FireY_change = 2
        elif Fire9.FireY >= 550:
            Fire9.FireX_change = 3
            Fire9.FireY_change = -3

        if Fire10.FireX <= 0:
            Fire10.FireX_change = 3
            Fire10.FireY_change = 3
        elif Fire10.FireX >= 750:
            Fire10.FireX_change = -3
            Fire10.FireY_change = 3
        if Fire10.FireY <= 0:
            Fire10.FireX_change = -3
            Fire10.FireY_change = 3
        elif Fire10.FireY >= 550:
            Fire10.FireX_change = 0
            Fire2.FireY_change = -3

        if Fire11.FireX <= 0:
            Fire11.FireX_change = 5
            Fire11.FireY_change = 3
        elif Fire11.FireX >= 750:
            Fire11.FireX_change = -3
            Fire11.FireY_change = 3
        if Fire11.FireY <= 0:
            Fire11.FireX_change = -3
            Fire11.FireY_change = 3
        elif Fire11.FireY >= 550:
            Fire11.FireX_change = 0
            Fire11.FireY_change = -3

        if Fire12.FireX <= 0:
            Fire12.FireX_change = 3
            Fire12.FireY_change = 3
        elif Fire12.FireX >= 750:
            Fire12.FireX_change = -3
            Fire12.FireY_change = 3
        if Fire12.FireY <= 0:
            Fire12.FireX_change = -3
            Fire12.FireY_change = 3
        elif Fire12.FireY >= 550:
            Fire12.FireX_change = 0
            Fire12.FireY_change = -3

        # keystrokes and boundaries(player)
        if event.type == pygame.KEYDOWN:
            if p.playerX <= 0:
                p.playerX = 0
            elif p.playerX >= 726:
                p.playerX = 726
            elif p.playerY <= 0:
                p.playerY = 0
            elif p.playerY >= 550:
                p.playerY = 550
            if event.key == pygame.K_LEFT:
                p.playerX_change = -3.0
            if event.key == pygame.K_RIGHT:
                p.playerX_change = 3.0
            if event.key == pygame.K_UP:
                p.playerY_change = -3.0
            if event.key == pygame.K_DOWN:
                p.playerY_change = 3.0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p.playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p.playerY_change = 0


        p.playerX += p.playerX_change
        p.playerY += p.playerY_change
        Fire1.FireX += Fire1.FireX_change
        Fire1.FireY += Fire1.FireY_change
        Fire2.FireX += Fire2.FireX_change
        Fire2.FireY += Fire2.FireY_change
        Fire3.FireX += Fire3.FireX_change
        Fire3.FireY += Fire3.FireY_change
        Fire4.FireX += Fire4.FireX_change
        Fire4.FireY += Fire4.FireY_change

        playerr(p.playerX, p.playerY)
        bomb(Bomb1.BombX,Bomb1.BombY)
        bomb(Bomb2.BombX,Bomb2.BombY)
        bomb(Bomb3.BombX,Bomb3.BombY)
        bomb(Bomb4.BombX,Bomb4.BombY)

        fire(Fire1.FireX, Fire1.FireY)
        fire(Fire2.FireX, Fire2.FireY)
        fire(Fire3.FireX, Fire3.FireY)
        fire(Fire4.FireX, Fire4.FireY)

        if start_time - end_time > 10:
            fire(Fire5.FireX, Fire5.FireY)
            Fire5.FireX += Fire5.FireX_change
            Fire5.FireY += Fire5.FireY_change

        if start_time - end_time > 20:
            fire(Fire6.FireX, Fire6.FireY)
            Fire6.FireX += Fire6.FireX_change
            Fire6.FireY += Fire6.FireY_change

        if start_time - end_time > 30:
            fire(Fire7.FireX, Fire7.FireY)
            Fire7.FireX += Fire7.FireX_change
            Fire7.FireY += Fire7.FireY_change

        if start_time - end_time > 40:
            fire(Fire8.FireX, Fire8.FireY)
            Fire8.FireX += Fire8.FireX_change
            Fire8.FireY += Fire8.FireY_change

        if start_time - end_time > 50:
            fire(Fire9.FireX, Fire9.FireY)
            Fire9.FireX += Fire9.FireX_change
            Fire9.FireY += Fire9.FireY_change

        if start_time - end_time > 60:
            fire(Fire10.FireX, Fire10.FireY)
            Fire10.FireX += Fire10.FireX_change
            Fire10.FireY += Fire10.FireY_change

        if start_time - end_time > 70:
            fire(Fire11.FireX, Fire11.FireY)
            Fire11.FireX += Fire11.FireX_change
            Fire11.FireY += Fire11.FireY_change

        if start_time - end_time > 80:
            fire(Fire12.FireX, Fire12.FireY)
            Fire12.FireX += Fire12.FireX_change
            Fire12.FireY += Fire12.FireY_change

        if start_time - end_time > 90:
            win()

        collisions = []
        collisions.append(isCollision(Fire1.FireX, Fire1.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire2.FireX, Fire2.FireY, p.playerX,p.playerY))
        collisions.append(isCollision(Fire3.FireX, Fire3.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire4.FireX, Fire4.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire5.FireX, Fire5.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire6.FireX, Fire6.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire7.FireX, Fire7.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire8.FireX, Fire8.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire9.FireX, Fire9.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire10.FireX, Fire10.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire11.FireX, Fire11.FireY, p.playerX, p.playerY))
        collisions.append(isCollision(Fire12.FireX, Fire12.FireY, p.playerX, p.playerY))


        for i in range(len(collisions)):
            if collisions[i]:
                gameover = True
                screen.fill('Black')
                over = Gameover_font.render("GAME OVER! Press P to Play Again and Q to Quit.", True,
                                            (255, 255, 255))

                screen.blit(over, (50, 250))
                p.playerX = 200
                p.playerY = 400
                p.playerX_change = 0
                p.playerY_change = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    elif event.key == pygame.K_p:
                        gameover = False
                        game()

        show_time(20, 20)
        pygame.display.update()

game()

