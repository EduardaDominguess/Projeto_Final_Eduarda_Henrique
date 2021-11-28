
import pygame
from pygame.locals import *
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import os
import numpy as np
import random
import math
import sys
from classes import Rua1, Rua2, Rua3, Rua4, Rua5, Sapo, Vidas

pygame.init()

#nome
pygame.display.set_caption("Don't get hit!")

#tela
window = pygame.display.set_mode((largura, altura))

#placar
score = 0
life = 0

#Carregar imagens 

#Imagens das telas
telainicial1 = pygame.image.load(os.path.join("Imagens", "Telainicio.png"))
telafinal = pygame.image.load(os.path.join("Imagens", "Telafinal.png"))

#Imagem do cenário
cenario = pygame.image.load(os.path.join("Imagens", "Background.png")).convert()

#Imagens da sapo 
sapo1 = pygame.image.load(os.path.join('Imagens','SAPO1.1.png')).convert_alpha()
sapo2 = pygame.image.load(os.path.join('Imagens','SAPO1.2.png')).convert_alpha()
sapo3 = pygame.image.load(os.path.join('Imagens','SAPO1.3.png')).convert_alpha()
sapo4 = pygame.image.load(os.path.join('Imagens','SAPO1.4.png')).convert_alpha()

#Imagem da moeda
moeda = pygame.image.load(os.path.join('Imagens','moeda.png')).convert_alpha()

#Icone das vidas
vida = pygame.image.load(os.path.join('Imagens','heart.png')).convert_alpha()

pygame.init()

#Váriavies

altura = 480
largura = 560
x = largura/2
y = altura/2
x1 = largura/2
y1 = altura/2


'''LISTAS'''
#Lista velocidade
velocidade = [2,3]
v = 4

#lista vidas
lista_vidasx = np.arange(50,650,50)
lista_vidasy = np.arange(34,650,50)
lista_vidas_inicial = []

for i in lista_vidasx:
    for d in lista_vidasy:
        lista_vidas_inicial.append([i,d])

#apagando vidas
lista_vidas = []
vida = True
for i in range (len(lista_vidas_inicial)):
    if lista_vidas_inicial[i][1] == 34:
        if lista_vidas_inicial[i][0] == 50 or lista_vidas_inicial[i][0] == 208 or lista_vidas_inicial[i][0] == 464 or lista_vidas_inicial[i][0]:
            pass
        else:
            lista_vidas.append(lista_vidas_inicial[i])
    elif lista_vidas_inicial[i][1] == 275:
        if lista_vidas_inicial[i][0] == 336 or lista_vidas_inicial[i][0] == 592 or lista_vidas_inicial[i][0] == 976:
            pass
        else:
            lista_vidas.append(lista_vidas_inicial[i])
    else:
        lista_vidas.append(lista_vidas_inicial[i])


#lista moedas
lista_moedax = np.arange(50,650,50)
lista_moeday = np.arange(34,650,50)
lista_moeda_inicial = []

for i in lista_moedax:
    for d in lista_moeday:
        lista_moeda_inicial.append([i,d])

#apagando moedas
lista_moeda = []
moeda = True
for i in range (len(lista_moeda_inicial)):
    if lista_moeda_inicial[i][1] == 34:
        if lista_moeda_inicial[i][0] == 50 or lista_moeda_inicial[i][0] == 208 or lista_moeda_inicial[i][0] == 464 or lista_moeda_inicial[i][0]:
            pass
        else:
            lista_moeda.append(lista_moeda_inicial[i])
    elif lista_moeda_inicial[i][1] == 275:
        if lista_moeda_inicial[i][0] == 336 or lista_moeda_inicial[i][0] == 592 or lista_moeda_inicial[i][0] == 976:
            pass
        else:
            lista_moeda.append(lista_moeda_inicial[i])
    else:
        lista_moeda.append(lista_moeda_inicial[i])
        
     
'''OBJETOS'''
#ARRUMAR NOME CLASSES
#sapo
sapo_obj = Sapo([1072,258])

#vida
vida_obj = Vidas(random.choice(lista_vidas))

#moedas
#coin_obj = Moedas(random.choice(lista_vidas))

#Carros
obj1 = Rua1(random.choice(velocidade))
a1 = obj1.carro
obj2 = Rua2(random.choice(velocidade))
a2 = obj2.carro
obj3 = Rua3(random.choice(velocidade))
a3 = obj3.carro  
obj4 = Rua4(random.choice(velocidade))
a4 = obj4.carro  
obj5 = Rua5(random.choice(velocidade))
a5 = obj5.carro  

#Criando o relógio do pygame
relogio = pygame.time.Clock()

canario = False

'''Game loop'''
#geral
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
    
    #carro 1
    if x1 >= largura:
        x1 = 0
    x1 += 1

    #carro 2
    if x2 >= largura:
        x2 = 0
    x2 += 1

    #carro 3
    if x3 >= largura:
        x3 = 0
    x3 += 1

    if y >= largura:
        y = 0
    #y += 5 - Oq faz ele ficar se movimentando sem comando


    if personagem.colliderect(carro1):
        y = 0
        x = 0
    if personagem.colliderect(carro2):
        y = 0
        x = 0
    if personagem.colliderect(carro3):
        y = 0
        x = 0 

    pygame.display.flip()

pygame.quit()  
