from src.Sprite import Sprite

import pygame
class Enemy (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
        self.speedy = 0
        self.speedx = 15
        self.image = pygame.transform.scale(self.image, (208, 152))
    def move(self, window):
        self.draw(window, self.x - self.speedx, self.y)

