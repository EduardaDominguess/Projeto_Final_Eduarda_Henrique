
import pygame
from pygame.constants import KEYDOWN, K_a, K_d, K_s, K_w


pygame.init()

altura = 400
largura = 500
x = largura/2
y = altura/2

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

    pygame.draw.rect(window,(255,0,0),(x,y,40,100))
    if y >= altura:
        y = 0
    y += 5

    pygame.display.update() 

pygame.quit()  
