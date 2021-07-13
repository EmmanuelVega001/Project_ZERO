from src.Sprite import Sprite

import pygame
class Enemy (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
        self.image = pygame.transform.scale(self.image, (400, 150))
        print("Enemy")