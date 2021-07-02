
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, src):
        pygame.image.load(src).convert()
