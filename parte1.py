import os
import pygame
from pygame import mixer, sprite
from funcoes import checkCoin, checkColision, incrementCarsVelocity, isAlive, removeOneLife, showFinalScore, showScore
from random import randint
from classes import *



mixer.init()
mixer.music.load(os.path.join('soundtrack.mp3'))
mixer.music.set_volume(0.02)
mixer.music.play(-1)

pygame.init()
pygame.display.set_caption("Don't get hit!")
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

startScreen = StartScreen()
startScreenGroup = sprite.Group()
startScreenGroup.add(startScreen)

background = Background()
backgroundGroup = sprite.Group()
backgroundGroup.add(background)

isRunning = True
gameStarted = False
gameEnd = False
while isRunning:
    clock.tick(60)
    for event in pygame.event.get():
        startScreenGroup.draw(window)
        startScreenGroup.update()
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not gameEnd and not gameStarted:
                    font = pygame.font.SysFont('helvetica', 30)
                    gameStarted = True
                    startScreen.kill()
                    CURRENT_SCORE = 0
                    frog = Frog()
                    life1 = Life(1)
                    life2 = Life(2)
                    life3 = Life(3)
                    lifeList = [life1, life2, life3]
                    lifeGroup = sprite.Group()
                    lifeGroup.add(life1, life2, life3)
                    car1 = Car(1)
                    car2 = Car(2)
                    car3 = Car(3)
                    car4 = Car(4)
                    car5 = Car(5)
                    carGroup = sprite.Group()
                    carGroup.add(car1, car2, car3, car4, car5)
                    coin = Coin()
                    spriteGroup = sprite.Group()
                    spriteGroup.add(backgroundGroup, frog, carGroup, coin, lifeGroup)
                elif gameEnd and not gameStarted:
                    endScreen.kill()
                    startScreen = StartScreen()
                    startScreenGroup = sprite.Group()
                    startScreenGroup.add(startScreen)
                    startScreenGroup.draw(window)
                    startScreenGroup.update()
                    gameEnd = False
            if gameStarted:
                if event.key == pygame.K_UP:
                    frog.movement_up()
                    frog.image = frog.imageUp
                if event.key == pygame.K_DOWN:
                    frog.movement_down()  
                    frog.image = frog.imageDown              
                if event.key == pygame.K_RIGHT: 
                    frog.movement_right()
                    frog.image = frog.imageRight
                if event.key == pygame.K_LEFT:
                    frog.movement_left()
                    frog.image = frog.imageLeft
    
    if gameStarted:
        spriteGroup.draw(window)
        showScore(window, font, CURRENT_SCORE)
        spriteGroup.update()

        if checkColision(frog, carGroup):
            frog.reset_pos()
            removeOneLife(lifeList)
            if not isAlive(lifeList):
                gameStarted = False
                gameEnd = True
                endScreen = EndScreen()
                endScreenGroup = sprite.Group()
                endScreenGroup.add(endScreen)
                endScreenGroup.draw(window)
                endScreenGroup.update()
                font = pygame.font.SysFont('helvetica', 40, True)
                showFinalScore(window, font, CURRENT_SCORE)
        
        if checkCoin(frog, coin):
            CURRENT_SCORE += 1
            coin.reappear()
            incrementCarsVelocity(carGroup)
    
    pygame.display.update()

pygame.quit()
