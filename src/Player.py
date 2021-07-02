from src.Sprite import Sprite

import pygame

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/player.png")
        print("Player")
        self.speedx = 0
        self.frames = [pygame.Rect((0,  0, 60,  90)), pygame.Rect((90, 0, 90, 90)), pygame.Rect((0, 90, 60, 90)), pygame.Rect((90, 90,  90 , 90 ))]
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
    def jump(self):
        pass