
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from Configurações import *
from classes import *
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')


window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Donkey Kong')
time = pygame.time.Clock()
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, donkey)).convert_alpha() #conserva png

class donkey(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)








game = True
while game:
    time.tick(10)
    window.fill((0,0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if pygame.key.get_pressed()[K_LEFT]: #esquerda
        x -= 20
    if pygame.key.get_pressed()[K_RIGHT]: #direita
        x += 20
    if pygame.key.get_pressed()[K_UP]: #cima
        y -= 20
    if pygame.key.get_pressed()[K_DOWN]: #baixo
        y += 20


    window.fill((255, 255, 255)) 
    #window.blit(kong(x,y))

    pygame.draw.rect(window,(rosa),(x,y,30,30))
    if y >= altura:
        y = 0
    #y += 5
 
    pygame.display.update() 

pygame.quit()  