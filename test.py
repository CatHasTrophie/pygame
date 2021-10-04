import pygame
import random
pygame.init()
playerX = 360
playerY = 464
enemyX = random.randint(0, 732)
enemyY = random.randint(0, 200)
playerXChange = 0
enemyXChange = 0
leftCorner = True
rightCorner = False
gameScreen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Bhramand ki Sair")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

class animations():

    def player(animationImage,playerX,playerY):
        animationIMG = pygame.image.load(animationImage)
        gameScreen.blit(animationIMG, (playerX, playerY))

    def enemy(animationImage, enemyX, enemyY):
        animationIMG = pygame.image.load(animationImage)
        gameScreen.blit(animationIMG, (enemyX,enemyY))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange -= 0.5
            if event.key == pygame.K_RIGHT:
                playerXChange += 0.5
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerXChange = 0

    playerX += playerXChange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if  enemyX <= 0:
         leftCorner = True
         rightCorner = False 
    elif enemyX >= 736:
         rightCorner = True
         leftCorner = False
    while leftCorner == True:
        enemyXChange += 0.3
    while rightCorner == True:
        enemyXChange -= 0.3
    enemyX += enemyXChange
    gameScreen.fill((255,255,255))
    animations.player("spaceship.png", playerX,playerY)
    animations.enemy("alien.png", enemyX, enemyY)

    pygame.display.update()
    