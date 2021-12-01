import pygame
import random import randint
import os 

WIDTH = 650
HEIGHT = 700

'''CLASSES'''
class Frog(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH/2
        self.y = HEIGHT
        self.width = 100
        self.height = 100

        self.imageUp = pygame.image.load('frog-up.png')
        self.imageDown = pygame.image.load('frog-down.png')
        self.imageRight = pygame.image.load('frog-right.png')
        self.imageLeft = pygame.image.load('frog-left.png')
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
            self.image = pygame.image.load('car-1.png')
            self.velocity = 5.1
        elif number == 2:
            self.y = 220
            self.image = pygame.image.load('car-2.png')
            self.velocity = -3.5
        elif number == 3:
            self.y = 307
            self.image = pygame.image.load('car-3.png')
            self.velocity = 3
        elif number == 4:
            self.y = 395
            self.image = pygame.image.load('car-4.png')
            self.velocity = -4
        else:
            self.y = 570
            self.image = pygame.image.load('car-6.png')
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

        self.image = pygame.image.load('coin.png')
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

        self.image = pygame.image.load('heart.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)


class Background(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('background.png')
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
        self.background = pygame.image.load('start-screen.png')
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
        self.background = pygame.image.load('end-screen.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.image = self.background
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)
