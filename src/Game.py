from src.Sprite import Sprite
from pygame import draw
from src.Player import Player
from src.Enemy import Enemy
import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        print("Game")
        self.player = Player()
        self.Vidas=3
        self.enemy=Enemy()
        self.x=0
        self.isJump=False
        self.contador=1
        self.RELOJ=pygame.time.Clock()
        self.tiempo=pygame.time.get_ticks()
        self.setBackgrounds()
        self.createWindow()

    def setBackgrounds(self):
        size = 1200, 500
        pygame.init()
        self.screen1 = pygame.display.set_mode(size)
        pygame.display.set_caption("Zero Demo")
        self.icon = pygame.image.load("./src/media/icono.png")
        pygame.display.set_icon(self.icon)
        self.setSprites()

    def createWindow(self):
        
        
        flag = True
        self.frame = 0
        
        while flag:
            
            self.drawSprites()
            self.recargarPantalla()
            pygame.time.delay(60)
            pygame.display.flip()
            pygame.key.set_repeat(60, 30)
            #para que aparezca un enemigo cada determinado tiempo
            
            print (self.tiempo)
            #self.drawEnemy()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                elif event.type == pygame.KEYDOWN:
                    self.moveControls(event)
                   
                elif event.type == pygame.KEYUP:
                    if (self.isJump==True):
                        self.downPlayer()
                    self.player.image = self.player.idleSprite[self.player.direction]
                    

    def setSprites(self):
        self.background = Sprite("./src/media/fondo-lejano.png")
        self.bg = Sprite("./src/media/fondo2.png")#fondo dos
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.arbol1=Sprite("./src/media/arbol1.png")
        self.background.draw(self.screen1, 0, 0)
        
        self.arbol1.draw(self.screen1,600,100)
        self.player.draw(self.screen1, 10, 310)
        
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1200,500))
        #self.highGrass.draw(self.screen1, 0, 0)

    def setSprites2(self):
        self.background = Sprite("./src/media/fondo2.png")
       # self.bg = Sprite("./src/media/fondo2.png")#fondo dos
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.background.draw(self.screen1, 0, 0)
        #self.player.draw(self.screen1, 790, 410)
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1200,450))
        #self.highGrass.draw(self.screen1, 0, 0)

    def recargarPantalla(self):
        #para hacer que el fondo se "mueva"
        x_relativa=self.x % self.highGrass.image.get_rect().width
        #self.screen1.blit(self.background.image,(x_relativa-self.background.image.get_rect().width,0))
        self.screen1.blit(self.highGrass.image,(x_relativa-self.highGrass.image.get_rect().width,0))
        if x_relativa-600:
         #   self.screen1.blit(self.background.image,(x_relativa,0))
            self.screen1.blit(self.highGrass.image,(x_relativa,0))
           
        self.x-=5
        pygame.display.update()
    
    def drawSprites(self):
        fuente = pygame.font.SysFont('Comic Sans MS', 40)
        rojo = 255, 0, 0


        self.background.draw(self.screen1, self.background.x, self.background.y)
        self.arbol1.draw(self.screen1, self.arbol1.x, self.arbol1.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        
        #self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)

        marcadorVidas = "Vidas: " + str(self.Vidas)
        mensaje = fuente.render(marcadorVidas, 0, rojo)
        self.screen1.blit(mensaje, (800,10))
        #self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
        
    def drawEnemy(self):
        self.enemy.draw(self.screen1,50,310)
        self.enemy.draw(self.screen1,self.enemy.x,self.enemy.y)


    def downPlayer(self):
        if self.player.x>=310:
            self.isJump=False
        else:
            self.isJump=True
            self.player.downing(self.screen1,self.frame)
            pygame.display.flip()


    def moveMap(self):
        if self.contador==1:
            self.setSprites()
            if (self.contador==2):
                self.player.draw(self.screen1,10,410)
            else:
                self.player.draw(self.screen1,790,410)
            print ("moveMapPrueba")
        else:
            self.setSprites2()
            self.player.draw(self.screen1,10,410)

    def moveControls(self, event):
        if event.key == pygame.K_d:
            self.frame = self.player.moveRight(self.screen1, self.frame)
            if (self.player.x > 800):
                self.contador+=1
                if (self.contador>2):
                    self.contador=1
                else:
                    self.contador+=1
                #self.moveMap()
                #self.player.movePlayer()
                #self.setSprites2()
               
                print("Contador: ",self.contador)
           
        elif event.key == pygame.K_a:
            self.frame = self.player.moveLeft(self.screen1, self.frame)
            if (self.player.x<5):
                self.contador-=1
                if (self.contador<=1):
                    self.contador=1
                else:
                    self.contador-=1
                #self.moveMap()
                #self.player.movePlayer2()
                #self.setSprites()
                
                print("Contador: ",self.contador)
        elif  event.key == pygame.K_UP or event.key == pygame.K_w:
            self.isJump=True
            self.frame = self.player.jump(self.screen1, self.frame)
            
            

