import pygame as p
from pygame import mixer
import os


class Sapo(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH/2
        self.y = HEIGHT
        self.vel = 4
        self.width = 100
        self.height = 100

        # IMAGES

        self.sapo1 = p.image.load('Imagens', 'SAPO1.1.png') #FRENTE
        self.sapo2 = p.image.load('Imagens', 'SAPO1.3.png') #TRAS
        self.sapo3 = p.image.load('Imagens', 'SAPO1.2.png') #DIREITA
        self.sapo4 = p.image.load('Imagens', 'SAPO1.4.png') #ESQUERDA
        self.sapo1 = p.transform.scale(self.sapo1, (self.width, self.height))
        self.sapo2 = p.transform.scale(self.sapo2, (self.width, self.height))
        self.sapo3 = p.transform.scale(self.sapo3, (self.width, self.height))
        self.sapo4 = p.transform.scale(self.sapo4, (self.width, self.height))

        self.image = self.sapo1
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)

    def movement(self):
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    self.x -= 85
                    self.image = self.sapo4
                if event.key == p.K_RIGHT:
                    self.x += 85
                    self.image = self.sapo3
                if event.key == p.K_UP:
                    self.y -= 86
                    self.image = self.sapo1
                if event.key == p.K_DOWN:
                    self.y += 86
                    self.image = self.sapo2
#Limites tela
    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

class Car(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.y = 130
            self.image = p.image.load('Imagens', 'carro1.png')
            self.vel = 3
        elif number ==2:
            self.y = 220
            self.image = p.image.load('Imagens', 'carro2.png')
            self.vel = 5
        elif number == 3:
            self.y = 307
            self.image = p.image.load('Imagens', 'carro3.png')
            self.vel = 6
        elif number == 4:
            self.y = 395
            self.image = p.image.load('Imagens', 'carro4.png')
            self.vel = 6.5
        else:
            self.y = 570
            self.image = p.image.load('Imagens', 'carro5.png')
            self.vel = 4


        self.x = WIDTH / 2
        self.width = 80
        self.height = 80
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.x += self.vel

        if self.x - self.width / 2 < 0:
            self.x = self.width / 2
            self.vel *= -1

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2
            self.vel *= -1


WIDTH = 650
HEIGHT = 700

p.init()

mixer.init()
mixer.music.load(os.path.join('music', 'Musiquinha.mp3'))
mixer.music.set_volume(0.2)
mixer.music.play(-1)


window = p.display.set_mode((WIDTH, HEIGHT))
cenario = pygame.image.load(os.path.join('Imagens', "Background.png")).convert()
p.display.set_caption("Don't het hit!")
clock = p.time.Clock()

 
sapo = Sapo()
sapo_group = p.sprite.Group()
sapo_group.add(sapo)

carro1 = Car(1)
carro2 = Car(2)
carro3 = Car(3)
carro4 = Car(4)
carro5 = Car(5)
car_group = p.sprite.Group()
car_group.add(carro1,carro2,carro3,carro4,carro5)


run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
            
    window.fill((0, 255, 0))
    window.blit(cenario, (0,0))


    sapo_group.draw(window)
    car_group.draw(window)
    sapo_group.update()
    car_group.update()

    p.display.update()

p.quit()
