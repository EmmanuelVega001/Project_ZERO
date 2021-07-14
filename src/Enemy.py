from src.Sprite import Sprite

import pygame
class Enemy (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
        self.speedy = 0
        self.speedx = 5
        self.image = pygame.transform.scale(self.image, (400, 150))
        self.rect= self.image.get_rect()
    
    def move(self, window):
        
        self.draw(window, self.x - self.speedx, self.y)

    
    

