#Configurações do jogo 
altura = 480
largura = 640
x = largura/2
y = altura/2
nome_jogo = 'Donkey Kong'
donkey = "donkey-kong-2.gif"
fonte = "arial"

#Cores 
rosa = (255,182,193)
branco = (255,255,255)

#Donkey configurações
""" aceleracao= 0.5
atrito = -0.12
gravidade = 0.8 """
pulo = 22 


#Plataforma
plataformas = [(0, altura-60), (175, 100),
(largura / 2 - 50, altura * 3 /4),
(350, 200), (125, altura - 350)] 

#Posições iniciais
donkey_incio = 2
plataforma_inicio = 1
