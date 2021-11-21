#Import bibliotecas
import pygame
from classes import *  
from jogo import *  
from Configurações import *  
 
pygame.init()

g = Game()
g.tela_inicio()
#Estado do jogo
while g.running:
    g.novo_jogo()
    g.game_over()
 
pygame.quit()
