from src.Enemy import Enemy
from src.Sprite import Sprite
from pygame import draw
from src.Player import Player
import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        print("Game")
        self.player = Player()
        self.enemy=Enemy()
        self.x=0
        self.RELOJ=pygame.time.Clock()
        self.createWindow()

    def createWindow(self):
        pygame.init()
        
        size = 1200, 500

        self.screen1 = pygame.display.set_mode(size)

        pygame.display.set_caption("Zero Demo")
        self.icon = pygame.image.load("./src/media/icono.png")

        pygame.display.set_icon(self.icon)
        flag = True
        self.setSprites()
        self.frame = 0
        while flag:
            self.collision()
            self.drawSprites()
            pygame.time.delay(10)
            pygame.display.flip()
            pygame.key.set_repeat(60, 30)
            self.enemy.move(self.screen1)
            if(self.player.isJumping and self.player.y >= 150):
                self.player.y -= 25
                self.frame = self.player.jump(self.screen1, self.frame)
            elif(self.player.y<310 and not self.player.isJumping):
                self.player.y += 25
            else:
                self.player.isJumping = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                elif event.type == pygame.KEYDOWN:
                    self.moveControls(event)
                elif event.type == pygame.KEYUP:
                    if event.key == K_w or K_UP:
                        self.player.isJumping = False
                    self.player.image = self.player.idleSprite[self.player.direction]

    def setSprites(self):
        self.background = Sprite("./src/media/fondo-lejano.png")
        self.arbol1=Sprite("./src/media/arbol1.png")
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.background.draw(self.screen1, 0, 0)
        #self.arbol1.draw(self.screen1,180,50)
        self.player.draw(self.screen1, 180, 310)
        self.enemy.draw(self.screen1, 800, 310)
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1600,500))
        # self.highGrass.draw(self.screen1, 0, 0)
        
    def collision(self):

        self.persona=self.player.image.get_rect()
        self.persona.top=self.player.y
        self.persona.left=self.player.x
        self.enemigo=self.enemy.image.get_rect()
        self.enemigo.top=self.enemy.y
        self.enemigo.left=self.enemy.x

        if self.persona.colliderect(self.enemigo):
            print("Colision")
        else:
            print("No colision")
        
    
    def drawSprites(self):
        x_relativa=self.x % self.highGrass.image.get_rect().width
        self.screen1.blit(self.background.image,(x_relativa-self.background.image.get_rect().width,0))
        self.screen1.blit(self.highGrass.image,(x_relativa-self.highGrass.image.get_rect().width,0))
        if x_relativa-600:
            self.screen1.blit(self.background.image,(x_relativa,0))
            self.screen1.blit(self.highGrass.image,(x_relativa,0))
        self.arbol1.draw(self.screen1, self.arbol1.x, self.arbol1.y)
        self.enemy.draw(self.screen1, self.enemy.x, self.enemy.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
    def moveControls(self, event):
        if event.key == pygame.K_d:

            self.frame = self.player.moveRight(self.screen1, self.frame)
            
            if (self.player.x > 1200):
                self.player.movePlayer(180, 310)
        elif (event.key == pygame.K_a and event.key==pygame.K_w):
            self.frame = self.player.moveLeft(self.screen1, self.frame)
            if(self.player.y == 310):
                self.player.isJumping = True
            print("izquierda salto")


        elif event.key == pygame.K_a:
            self.frame = self.player.moveLeft(self.screen1, self.frame)
            if (self.player.x<5):
                self.player.movePlayer2()

        elif  event.key == pygame.K_UP or event.key == pygame.K_w:
            if(self.player.y == 310):
                self.player.isJumping = True

        elif (event.key==pygame.K_w and event.key == pygame.K_d):
            if(self.player.y == 310):
                self.player.isJumping = True
            self.frame = self.player.moveRight(self.screen1, self.frame)
            print("a salto")
        
        elif (event.key == pygame.K_d and event.key==pygame.K_w):
            self.frame = self.player.moveRight(self.screen1, self.frame)
            if(self.player.y == 310):
                self.player.isJumping = True
            

        
        elif (event.key==pygame.K_w and event.key == pygame.K_a):
            if(self.player.y == 310):
                self.player.isJumping = True
            self.frame = self.player.moveLeft(self.screen1, self.frame)
        
       
            

        
            

