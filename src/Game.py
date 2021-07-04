from pygame import draw
from src.Player import Player
import pygame

class Game:
    def __init__(self):
        print("Game")
        self.player = Player()
        
        self.createWindow()
    def createWindow(self):
        pygame.init()

        size = 800, 600

        self.screen1 = pygame.display.set_mode(size)

        pygame.display.set_caption("Zero Demo")
        self.drawSprites()
        flag = True
        
        while flag:
            pygame.time.delay(50)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
    def drawSprites(self):
        self.player.setInWindow(self.screen1, 0, 0, 3)
