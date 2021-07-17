from src.Sprite import Sprite

import pygame
class Enemy (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
        self.enemigoDerecha=Sprite("./src/media/movimientosEnemigos/enemigoDerecha.png")
        self.speedy = 0
        self.speedx = 15
        self.image = pygame.transform.scale(self.image, (208, 152))
    
    def move(self, window,derecha):
        if self.x<=0:
            self.x=1800
        self.draw(window, self.x - self.speedx, self.y)


