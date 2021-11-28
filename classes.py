import pygame
import random
import os 

'''CLASSES'''
#classe sapo
class Sapo:
    def __init__(self, posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]
        self.retangulo = pygame.Rect((self.posicaox, self.posicaoy), (128,128))
    def sapo_sobe(self):
        self.posicaoy -= 128
        self.retangulo.top = self.posicaoy     
    def sapo_desce(self):
        self.posicaoy += 128
        self.retangulo.top = self.posicaoy 
    def sapo_direita(self):
        self.posicaox += 128
        self.retangulo.left = self.posicaox 
    def sapo_esquerda(self):
        self.posicaox -= 128
        self.retangulo.left = self.posicaox 
#vida      
class Vidas:
    def __init__(self,posicao):
        self.posicaox = posicao[0]
        self.posicaoy = posicao[y]

#lista carros
carros_left = ['carro1', 'carro2','carro3']
carros_right = ['carro4', 'carro5','carro6']

#listas ruas
#COMPLETAR COM O TAMANHO
r1 = [275.5, 217]
r2 = [-285, 42.7]
r3 = [406.3, -44.5]
r4 = [-285, -138.3]
r5 = [283.4, -219.2]

class Carros:
    def __init__(self,rua, velocidade):
        self.velocidade = velocidade
        self.rua = rua
        if  self.rua == 1:
            self.posicaox = r1[0]
            self.posicaoy = r1[1]
    
        elif self.rua == 2:
            self.posicaox = r2[0]
            self.posicaoy = r2[1]
            
        elif self.rua == 3:
            self.posicaox = r3[0]
            self.posicaoy = r3[1]
                
        elif self.rua == 4:
            self.posicaox = r4[0]
            self.posicaoy = r4[1]
                
        elif self.rua == 5:
            self.posicaox = r5[0]
            self.posicaoy = r5[1]

        if self.rua == 1 or self.rua == 3 or self.rua == 5:
            sprite = random.choice(carros_right)
            if sprite == 'carro1':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro1')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 170)) #VER POSICAOOO
            if sprite == 'carro2':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro2')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 212)) #VER POSICAOOO
            if sprite == 'carro3':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro3')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 212)) #VER POSICAOOO
            
        if self.rua == 2 or self.rua == 4:
            if sprite == 'carro4':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro4')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 212)) #VER POSICAOOO
            if sprite == 'carro5':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro5')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 212)) #VER POSICAOOO
            if sprite == 'carro6':
                self.imagem = pygame.image.load(os.path.join('Imagens','carro6')).convert_alpha()
                self.rectangle = pygame.Rect((self.posicaox, self.posicaoy), (128, 212)) #VER POSICAOOO
    
    #movimentaçao
    def movimento(self):
        if self.rua == 1 or self.rua == 3 or self.rua == 5: 
            self.posicaoy -= self.velocidade
            self.retangulo.top = self.posicaoy 
        elif self.rua == 2 or self.rua == 4 or self.rua == 6: 
            self.posicaoy += self.velocidade
            self.retangulo.top = self.posicaoy 
       
'''RUAS'''
#RUA1
class Rua1:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Carros(1, velocidade)
        self.carro.movimento()

class Rua2:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Carros(1, velocidade)
        self.carro.movimento()

class Rua3:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Carros(1, velocidade)
        self.carro.movimento()

class Rua4:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Carros(1, velocidade)
        self.carro.movimento()

class Rua5:
    def __init__(self,velocidade):
        self.velocidade = velocidade
        self.carro = Carros(1, velocidade)
        self.carro.movimento()



                













""" #classe sapo
class Sapos1 (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Sapo1 = []
        self.Sapo1.append(pygame.image.load('Sapo1/SAPO1.1.png'))
        self.Sapo1.append(pygame.image.load('Sapo1/SAPO1.2.png'))
        self.Sapo1.append(pygame.image.load('Sapo1/SAPO1.3.png'))
        self.Sapo1.append(pygame.image.load('Sapo1/SAPO1.4.png'))
        self.atual = 0
        self.image = self.Sapo1[self.atual]
        self.image = pygame.transform.scale(self.image, (540/10, 540/10))
        self.rect = self.image.get_rect() 
        self.rect.topleft = 100, 100
    
    def update(self):
        if pygame.key.get_pressed()[K_LEFT]: #esquerda
            self.image = self.Sapo1[3]
            self.image = pygame.transform.scale(self.image, (540/10, 540/10))
        if pygame.key.get_pressed()[K_RIGHT]: #direita
            self.image = self.Sapo1[1]
            self.image = pygame.transform.scale(self.image, (540/10, 540/10))
        if pygame.key.get_pressed()[K_UP]: #cima
            self.image = self.Sapo1[0]
            self.image = pygame.transform.scale(self.image, (540/10, 540/10))
        if pygame.key.get_pressed()[K_DOWN]: #baixo
            self.image = self.Sapo1[2]
            self.image = pygame.transform.scale(self.image, (540/10, 540/10))
    
    def move(self, movement):
        def __init__(self,movement):
            self.movementx = movement[0]
            self.movementy = movement[1]
            self.Sapo1 = pygame.Rect((self.movementx, self.movementy), (128,128))
        def sobe_raposa(self):
            self.movementy -= 128
            self.Sapo1.top = self.movementy     
        def desce_raposa(self):
            self.movementy += 128
            self.Sapo1.top = self.movementy 
        def direita(self):
            self.movementx += 128
            self.Sapo1.left = self.movementx 
        def esquerda(self):
            self.movementx -= 128
            self.Sapo1.left = self.movementx 

#lista carros
carros_left = [carro1, carro2, carro3]
carros_right = [carro4, carro5, carro6]    

#carros
class Carros:
    def __init__(self,rua,velocidade):
        self.velocidade = velocidade 
        self.rua = rua
        if self.rua = 1:
            
        pass """
