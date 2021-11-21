from Configurações import *
from random import randrange, choice
import pygame


class moviemnto:
    def inicio(self, filename):
        self.spritesheet = pygame.image.load(filename).convert() #convertendo a imagem do arquivo para o jogo

    def image(self, x, y, altura, largura):
        imagem = pygame.Surface((largura, altura))
        imagem.blit(self.spritesheet, (0, 0), (x, y, largura, altura))
        imagem = pygame.transform.scale(imagem, (largura // 3, altura // 3)) # tamanho do Macaco
        return imagem

class Jogador(pygame.sprite.Sprite):
    def incio(self, game):
        self._layer= donkey_incio # configurando a camada em que o jogador está 
        #self.groups= game.all_sprites # adicionando na função o grupo de sprites
        #pygame.sprite.Sprite.__init__(self, self.groups)
        self.game= game
        self.andando= False    #sem movimento
        self.pulando= False    #sem movimento
        self.frame_atual= 0    
        self.ultimo_update= 0 
        self.carrega_imagens()  #adicionando a função carregando_imagens
        self.image= self.jogador_parado[0] # imagem do jogador parado 
        self.rect= self.image.get_rect()   # configurando as dimensões da imagem como retângulo
        self.rect.center= (40, altura - 100) #p/ ele começar no canto inferior esquerdo da tela
        self.pos= vet(40, altura - 100) #posição
        self.vel= vet(0, 0)  #velocidade
        self.acc= vet(0, 0)  #aceleração

    def carrega_imagens(self):
        #Dando as cordenadas das imagens do jogador parado
        self.jogador_parado= [self.game.spritesheet.get_image(260, 1032, 128, 256), self.game.spritesheet.get_image(260, 774, 128, 256)] 
        for frame in self.jogador_parado:
            frame.set_colorkey(rosa)   #Definindo o fundo da imagem preto
        #Dando as cordenadas das imagens do jogador andando
        self.andando_direita = [self.game.spritesheet.get_image(130, 1290, 128, 256),
                            self.game.spritesheet.get_image(130, 1032, 128, 256) ]
        self.andando_esquerda = []
        for frame in self.jogador_andando_d: #rotacionando as imagens para a esquerda
            frame.set_colorkey(rosa)   #Definindo o fundo da imagem preto
            self.jogador_andando_e.append(pygame.transform.flip(frame, True, False)) #rotaciona horizontalmente, não verticalmente
        #Dando as cordenadas da imagem do jogador pulando
        self.jogador_pulando= self.game.spritesheet.get_image(260, 516, 128, 256)
        self.jogador_pulando.set_colorkey(rosa)  #Definindo o fundo da imagem preto

    def pular_cut(self):
        #Arrumando o pulo
        if self.pulando:
            if self.vel.y < -3:
                self.vel.y = -3

    def pular(self):  #!!!!!!!!!!
        #só pula se tiver em alguma plataforma
        self.rect.x += 2
        colisao = pygame.sprite.spritecollide(self, self.game.platforms, False)  #declarando colisão
        self.rect.x -= 2 #não é visível isso, mas necessário
        # Se houver colisão e o E.T não estiver pulando
        if colisao and not self.pulando:
            self.game.jump_sound.play() #só faz esse som quando ele pula p/ outra plataforma
            self.pulando = True
            self.vel.y = -pulo
    


        

        
        



 