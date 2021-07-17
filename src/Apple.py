from src.Sprite import Sprite

import pygame
class Apple (Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/manzana.png")
        self.speedy = 1
        self.speedx = 0
        
    
    def move(self, window):
        
        self.draw(window, self.x , self.y+ self.speedy)
        if self.y>=500:
            self.y=-10

