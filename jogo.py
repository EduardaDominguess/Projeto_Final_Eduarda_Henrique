import os
import pygame
from pygame import mixer, sprite
from funcoes import checkCoin, checkColision, incrementCarsVelocity, isAlive, removeOneLife, showFinalScore, showScore
from random import randint

class Frog(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH/2
        self.y = HEIGHT
        self.width = 100
        self.height = 100

        self.imageUp = pygame.image.load('imagens','frog-up.png')
        self.imageDown = pygame.image.load('imagens','frog-down.png')
        self.imageRight = pygame.image.load('imagens','frog-right.png')
        self.imageLeft = pygame.image.load('imagens','frog-left.png')
        self.imageUp = pygame.transform.scale(self.imageUp, (self.width, self.height))
        self.imageDown = pygame.transform.scale(self.imageDown, (self.width, self.height))
        self.imageRight = pygame.transform.scale(self.imageRight, (self.width, self.height))
        self.imageLeft = pygame.transform.scale(self.imageLeft, (self.width, self.height))

        self.image = self.imageUp
        self.rect = self.image.get_rect()

    def update(self):
        self.movement_up()
        self.movement_down()
        self.movement_left()
        self.movement_right()
        self.correction()
        self.rect.center = (self.x, self.y)

    def reset_pos(self):
        self.x = WIDTH/2
        self.y = HEIGHT

    def movement_left(self):
        self.x -= 85
        
    def movement_right(self):
        self.x += 85

    def movement_up(self):
        self.y -= 86

    def movement_down(self):
        self.y += 86 
       
    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2
        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

class Car(sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.y = 130
            self.image = pygame.image.load('imagens','car-1.png')
            self.velocity = 5.1
        elif number == 2:
            self.y = 220
            self.image = pygame.image.load('imagens','car-2.png')
            self.velocity = -3.5
        elif number == 3:
            self.y = 307
            self.image = pygame.image.load('imagens','car-3.png')
            self.velocity = 3
        elif number == 4:
            self.y = 395
            self.image = pygame.image.load('imagens','car-4.png')
            self.velocity = -4
        else:
            self.y = 570
            self.image = pygame.image.load('imagens','car-6.png')
            self.velocity = -3.2

        self.x = WIDTH / 2
        self.width = 80
        self.height = 80
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.x += self.velocity

        if self.x + self.width / 2 < 0:
            self.x = WIDTH + self.width / 2

        elif self.x - self.width / 2 > WIDTH:
            self.x = - self.width / 2

class Coin(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, WIDTH)
        self.y = randint(85, HEIGHT)
        self.width = 56
        self.height = 56

        self.image = pygame.image.load('imagens','coin.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def reappear(self):
        self.x = randint(0, WIDTH)
        self.y = randint(85, HEIGHT)

class Life(sprite.Sprite):
    def __init__(self, count):
        super().__init__()
        self.width = 56
        self.height = 56

        self.x = self.width * count * 1.1
        self.y = self.height - 10

        self.image = pygame.image.load('imagens','heart.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)


class Background(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('imagens','background.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.image = self.background
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)
    
class StartScreen(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('imagens','start-screen.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.image = self.background
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)

class EndScreen(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('imagens','end-screen.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.image = self.background
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)
        
WIDTH = 650
HEIGHT = 700


mixer.init()
mixer.music.load(os.path.join('musicas','soundtrack.mp3'))
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
