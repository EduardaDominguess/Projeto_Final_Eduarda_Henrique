import pygame as p


class Sapo(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH/2
        self.y = HEIGHT
        self.vel = 4
        self.width = 100
        self.height = 100

        # IMAGES

        self.sapo1 = p.image.load('SAPO1.1.png')
        self.sapo2 = p.image.load('SAPO1.3.png')
        self.sapo1 = p.transform.scale(self.sapo1, (self.width, self.height))
        self.sapo2 = p.transform.scale(self.sapo2, (self.width, self.height))

        self.image = self.sapo1
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -= self.vel

        elif keys[p.K_RIGHT]:
            self.x += self.vel

        if keys[p.K_UP]:
            self.y -= self.vel
            self.image = self.sapo1

        elif keys[p.K_DOWN]:
            self.y += self.vel
            self.image = self.sapo2
#Não sai da tela
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
            self.y = 150
            self.image = p.image.load('carro1.png')
            self.vel = 3
        elif number ==2:
            self.y = 250
            self.image = p.image.load('carro2.png')
            self.vel = 5
        elif number == 3:
            self.y = 350
            self.image = p.image.load('carro3.png')
            self.vel = 6
        elif number == 4:
            self.y = 450
            self.image = p.image.load('carro4.png')
            self.vel = 6.5
        else:
            self.y = 550
            self.image = p.image.load('carro5.png')
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

class Background(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = p.image.load('Background.png')
        #self.img2 = p.image.load('You Win.png')
        self.img3 = p.image.load('Telafinal.png')

        self.img1 = p.transform.scale(self.img1, (WIDTH, HEIGHT))
        #self.img2 = p.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = p.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)


WIDTH = 650
HEIGHT = 700

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Don't het hit!")
clock = p.time.Clock()

backgroung = Background()
backgroung_group = p.sprite.Group()
backgroung_group.add(backgroung)
 
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

    backgroung_group.draw(win)

    sapo_group.draw(win)
    car_group.draw(win)
    sapo_group.update()
    car_group.update()
    backgroung_group.update()

    p.display.update()

p.quit()