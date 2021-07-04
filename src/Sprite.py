
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, src):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.transform.scale(pygame.image.load(src), (180, 180))
        self.frames = []
        print("Sprite: " + src)
    def setInWindow(self, window, x, y, frame):
        print(self.frames[0])
        self.x = x
        self.y = y
        self.rect = self.image.subsurface(self.frames[frame]).get_rect()
        window.blit(self.image.subsurface(self.frames[frame]), (self.x, self.y))