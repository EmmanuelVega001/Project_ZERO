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
        
        size = 1200, 600

        self.screen1 = pygame.display.set_mode(size)

        pygame.display.set_caption("Zero Demo")
        self.icon = pygame.image.load("./src/media/icono.png")

        pygame.display.set_icon(self.icon)
        flag = True
        self.setSprites()
        self.frame = 0
        while flag:
            self.drawSprites()
            self.collision()
            self.recargarPantalla()
            self.movimientoEnemy()
            pygame.time.delay(10)
            pygame.display.flip()
            pygame.key.set_repeat(60, 30)
            self.collision()
            if(self.player.isJumping and self.player.y >= 330):
                self.player.y -= 25
                self.frame = self.player.jump(self.screen1, self.frame)
            elif(self.player.y<410 and not self.player.isJumping):
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
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.arbol1=Sprite("./src/media/arbol1.png")
        self.background.draw(self.screen1, 0, 0)
        self.arbol1.draw(self.screen1,180,50)
        self.enemy.draw(self.screen1, 800, 410)
        self.player.draw(self.screen1, 180, 410)
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1600,600))
        #self.highGrass.draw(self.screen1, 0, 0)

    def movimientoEnemy(self):
        Sprite.__init__(self, "./src/media/movimientosEnemigos/enemigo.png")
        self.rect = self.image.get_rect()
        self.enemy.move(self.screen1)
        self.speedx=10
        
        
    def collision(self):
        x = 5
        y = 5
        self.persona=self.player.image.get_rect()
        self.persona.top=self.player.y
        self.persona.left=self.player.x
        self.enemigo=self.enemy.image.get_rect()
<<<<<<< HEAD
        self.enemigo.top=y
        self.enemigo.left=x
        colision=pygame.sprite.spritecollide(self.enemy,self.player,False)
        if colision:
            print("colisionsota")
=======
        self.enemigo.top=self.enemy.y
        self.enemigo.left=self.enemy.x
>>>>>>> c8846ecad9c585a4f3b8120c5a7f60b989fa8bd1
        if self.persona.colliderect(self.enemigo):
            print("Colision")
        else:
            print("No colision")

    
        
        

    def recargarPantalla(self):
        #para hacer que el fondo se "mueva"
        
        x_relativa=self.x % self.highGrass.image.get_rect().width
        #self.screen1.blit(self.background.image,(x_relativa-self.background.image.get_rect().width,0))
        self.screen1.blit(self.highGrass.image,(x_relativa-self.highGrass.image.get_rect().width,0))
        

        if x_relativa-600:
         #   self.screen1.blit(self.background.image,(x_relativa,0))
            self.screen1.blit(self.highGrass.image,(x_relativa,0))
        self.x-=3
        pygame.display.update()
    
    def drawSprites(self):
        self.background.draw(self.screen1, self.background.x, self.background.y)
        self.arbol1.draw(self.screen1, self.arbol1.x, self.arbol1.y)
        self.enemy.draw(self.screen1, self.enemy.x, self.enemy.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
        #self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
    def moveControls(self, event):
        if event.key == pygame.K_d:

            self.frame = self.player.moveRight(self.screen1, self.frame)
            
            if (self.player.x > 1200):
                self.player.movePlayer(180, 410)
           
        elif event.key == pygame.K_a:
            self.frame = self.player.moveLeft(self.screen1, self.frame)
            if (self.player.x<5):
                self.player.movePlayer2()
        elif  event.key == pygame.K_UP or event.key == pygame.K_w:
            if(self.player.y == 410):
                self.player.isJumping = True
            

