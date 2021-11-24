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
