import pygame
import random
import math
from pygame import mixer

pygame.init()

height = 800
width = 600
# create the screen
screen = pygame.display.set_mode((height, width))

# background
background = pygame.image.load('background.jpg')

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# playerImg = pygame.image.load('player.png')
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyImg.append(pygame.image.load("monster.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -1
bullet_state = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
game_over_font =  pygame.font.Font('freesansbold.ttf', 64)
textX = 10
textY = 10



def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score_value = font.render("score: " + str(score), True, (255,255,255))
    screen.blit(score_value, (x, y))

def game_over(x, y):
    game_is_over = game_over_font.render("GAMEOVER", True, (255, 255, 255))
    screen.blit(game_is_over, (x, y))




#Game loop
running = True
while running:
    # RGB - red, green, blue
    screen.fill((0, 0, 0))
    # background images
    # screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check whether its L or R
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            playerX_change = 0.3

        if keys[pygame.K_LEFT]:
            playerX_change = -0.3

        if keys[pygame.K_SPACE]:
            if bullet_state is "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
                bullet_sound = mixer.Sound("laser.wav")
                bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                if keys[pygame.K_RIGHT]:
                    playerX_change = 0.3

                if keys[pygame.K_LEFT]:
                    playerX_change = -0.3
        # return playerX_change

    # checking for boundaries so that spaceship stays in box
    playerX += playerX_change
    # boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement so that it stays in box
    for i in range(num_enemies):
        #game over
        if enemyY[i] > 440:
            for j in range(num_enemies):
                enemyY[j]= 2000
            game_over(200,400)
            break

        enemyX[i] += enemyX_change[i]
        # boundaries
        if enemyX[i] <= -80:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 814:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # collision
        iscollision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if iscollision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()

        enemy(enemyX[i], enemyY[i], i)

    # shoot bullet
    if bulletY <= -16:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
