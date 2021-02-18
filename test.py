import pygame

pygame.init()

height = 800
width = 600
#create the screen
screen = pygame.display.set_mode((height, width))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#playerImg = pygame.image.load('player.png')
playerImg = pygame.image.load('spaceship.png')
#playerX = height/2 - 32
#playerY = 450
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


class ship():
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

#Game loop
running = True
while running:
    #RGB - red, green, blue
    screen.fill((0,0,0))



    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()