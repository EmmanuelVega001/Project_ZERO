from src.Sprite import Sprite

import pygame
class Enemy (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
<<<<<<< HEAD
        self.image = pygame.transform.scale(self.image, (400, 150))
        print("Enemy")

        
=======
        self.speedy = 0
        self.speedx = 5
        self.image = pygame.transform.scale(self.image, (400, 150))
    
    def move(self, window):
        
        self.draw(window, self.x - self.speedx, self.y)

>>>>>>> 9f00c1f1823bf45479e6d28640061f2395ebb224
