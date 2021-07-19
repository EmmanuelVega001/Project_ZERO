from src.Enemy import Enemy
from src.Sprite import Sprite
from pygame import draw
from src.Player import Player
from src.Apple import Apple


import pygame
import random
from pygame.locals import *

import os

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        print("Game")
        self.contador=0
        self.player = Player()
        self.enemy=Enemy()
        self.apple=Apple()
        print(os.getcwd())
        self.dolor1=pygame.mixer.Sound("./src/media/dolor.wav")
        self.yea=pygame.mixer.Sound("./src/media/yea.wav")
        self.yea2=pygame.mixer.Sound("./src/media/yea2.wav")
        self.dolor2=pygame.mixer.Sound("./src/media/dolor2.wav")
        self.x=0
        self.contador=1
        self.derecha=False
        self.RELOJ=pygame.time.Clock()
        self.persona=self.player.image.get_rect()
        self.enemigo=self.enemy.image.get_rect()
        self.manzana=self.apple.image.get_rect()
        self.createWindow()

    def createWindow(self):
        
        pygame.mixer.music.load("./src/media/Musica_Fondo.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
        size = 1200, 490

        self.screen1 = pygame.display.set_mode(size)

        pygame.display.set_caption("Zero Demo")
        self.icon = pygame.image.load("./src/media/icono.png")

        pygame.display.set_icon(self.icon)
        self.flag = True
        self.song = 1
        self.setSprites()
        self.frame = 0
        while self.flag:
            self.collision()
            self.drawSprites()
            pygame.time.delay(10)
            pygame.display.flip()
            pygame.key.set_repeat(60, 30)
            self.enemy.move(self.screen1,self.derecha)
            self.apple.move(self.screen1)
            if(self.player.isJumping and self.player.y >= 110):
                self.player.y -= 25
                self.frame = self.player.jump(self.screen1, self.frame)
            elif(self.player.y<310 and not self.player.isJumping):
                self.player.y += 25
            else:
                self.player.isJumping = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                elif event.type == pygame.KEYDOWN:
                    self.moveControls(event)
                elif event.type == pygame.KEYUP:
                    if event.key == K_w or K_UP:
                        self.player.isJumping = False
                    self.player.image = self.player.idleSprite[self.player.direction]

    def setSprites(self):
        numero_random=random.randrange(10,1100)
        self.background = Sprite("./src/media/fondo-lejano.png")
        self.arbol1=Sprite("./src/media/arbol1.png")
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.background.draw(self.screen1, 0, 0)
        #self.arbol1.draw(self.screen1,180,50)
        self.player.draw(self.screen1, 180, 310)
        self.enemy.draw(self.screen1, 800, 330)
        self.apple.draw(self.screen1,numero_random,-20)
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1300,490))
        #self.highGrass.draw(self.screen1, 1100, 490)
    
    def setManzana(self):
        numero_random=random.randrange(10,1100)
        self.apple.draw(self.screen1,numero_random,0)

    def setEnemyRight(self):
        self.enemy.draw(self.screen1, 100, 330)

    def setEnemyLeft(self):
        self.enemy.draw(self.screen1, 1600, 330)

        
    def collision(self):
       
        self.persona.top=self.player.y
        self.persona.left=self.player.x
        
        self.enemigo.top=self.enemy.y
        self.enemigo.left=self.enemy.x
        if self.persona.colliderect(self.enemigo):
            if self.derecha==False:
                if self.contador>=100:
                    self.player.puntosVida -= 1
                    if self.player.puntosVida<=0: self.flag = False
                    self.contador=0
                    self.dolor1.play()
                    self.setEnemyLeft()
                    self.derecha=True
                else:
                    self.contador+=10
            else:
                if self.contador>=100:
                    self.player.puntosVida   -= 1
                    if self.player.puntosVida<=0: self.flag = False
                    self.contador=0
                    self.dolor2.play()
                    self.setEnemyLeft()
                    self.derecha=False
                else:
                    self.contador+=10
        self.manzana.top=self.apple.y
        self.manzana.left=self.apple.x

        if self.persona.colliderect(self.manzana):
            if self.song==1:
                self.player.puntos += 1
                self.yea.play()
                self.setManzana()
                self.song=0
                print(self.song)
            else:
                self.player.puntos+= 1
                self.yea2.play()
                self.setManzana()
                self.song=1
                print(self.song)
    def drawSprites(self):
        rojo = 255, 0, 0
        self.background.draw(self.screen1,self.background.x,self.background.y)
        self.arbol1.draw(self.screen1, self.arbol1.x, self.arbol1.y)
        self.enemy.draw(self.screen1, self.enemy.x, self.enemy.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        self.apple.draw(self.screen1,self.apple.x,self.apple.y)

      
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)

        
        self.marcador = str(self.player.puntosVida)
        self.puntos = str(self.player.puntos)
        self.palabra="Puntos de vida: "+self.marcador
        self.fuente = pygame.font.Font(None, 40)
        self.mensaje = self.fuente.render(self.palabra, 1, rojo)

        self.palabra2="Puntos: "+self.puntos
        self.mensaje2= self.fuente.render(self.palabra2, 1, rojo)

        self.screen1.blit(self.mensaje, (800,30))
        self.screen1.blit(self.mensaje2, (800,60))
        



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
        
       
            

        
            

