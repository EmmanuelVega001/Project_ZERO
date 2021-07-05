from src.Sprite import Sprite
from pygame import draw
from src.Player import Player
import pygame
from pygame.locals import *


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
        self.icon = pygame.image.load("./src/media/icono.png")
        pygame.display.set_icon(self.icon)
        flag = True
        self.setSprites()
        self.frame = 0
        while flag:
            self.drawSprites()
            pygame.display.update()
            pygame.time.delay(60)
            pygame.display.flip()
            pygame.key.set_repeat(50, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                elif event.type == pygame.KEYDOWN:
                    self.moveControls(event)
                elif event.type == pygame.KEYUP:
                    self.player.image = self.player.idleSprite[self.player.direction]

    def setSprites(self):
        self.background = Sprite("./src/media/fondo-lejano.png")
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.arbol1=Sprite("./src/media/arbol1.png")
        self.background.draw(self.screen1, 0, 0)
        self.arbol1.draw(self.screen1,180,50)
        self.player.draw(self.screen1, 180, 410)
        self.highGrass.draw(self.screen1, 0, 0)
        
    def drawSprites(self):
        self.background.draw(self.screen1, self.background.x, self.background.y)
        self.arbol1.draw(self.screen1, self.arbol1.x, self.arbol1.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
        
    def moveControls(self, event):
        if event.key == K_d:
            self.frame = self.player.moveRight(self.screen1, self.frame)
        elif event.key == K_a:
            self.frame = self.player.moveLeft(self.screen1, self.frame)

