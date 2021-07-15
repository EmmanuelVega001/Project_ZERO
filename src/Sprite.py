<<<<<<< HEAD
import pygame

#Conjunto inicial de sprites cargados
class Sprite(pygame.sprite.Sprite):
    def __init__(self, src):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(src)
        #print("Sprite cargado: " + src)

    #Actualizar * Ticks
    def draw(self, window, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        window.blit(self.image, (self.x, self.y))
       
=======
import pygame

#Conjunto inicial de sprites cargados
class Sprite(pygame.sprite.Sprite):
    def __init__(self, src):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(src)
        #print("Sprite cargado: " + src)
        
    #Actualizar * Ticks
    def draw(self, window, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        window.blit(self.image, (self.x, self.y))
       
>>>>>>> 9f00c1f1823bf45479e6d28640061f2395ebb224
