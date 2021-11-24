
import pygame
from pygame.locals import *
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import os


pygame.init()

#Váriavies

altura = 400
largura = 500
x = largura/2
y = altura/2
x1 = largura/2
y1 = altura/2


Image = pygame.sprite.Group()
Sapo1 = Sapos1()
Image.add(Sapo1)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Donkey Kong')
time = pygame.time.Clock()


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
    
    Image.draw(window)
    Image.update()
    personagem = pygame.draw.rect(window,(255,182,193),(x,y,30,30))
    barril = pygame.draw.rect(window,(255,182,193),(x1,y1,20,50))
    if y >= altura:
        y = 0
    #y += 5 - Oq faz ele ficar se movimentando sem comando

    pygame.display.update() 

pygame.quit()  
