from src.Sprite import Sprite

import pygame


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/movimientosJugador/reposoDerecha.png")
        self.image = pygame.transform.scale(self.image, (85, 132))
        #print("Player")
        self.speedy = 0
        self.speedx = 5
        self.isJumping = 10
        self.idleSprite = [
            pygame.transform.scale(
                pygame.image.load("./src/media/movimientosJugador/reposoDerecha.png"),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load("./src/media/movimientosJugador/reposoIzquierda.png"),
                (85, 132),
            ),
        ]

        self.walkRightSprite = [
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoDerecha1.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoDerecha2.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoDerecha3.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoDerecha4.png"
                ),
                (85, 132),
            ),
        ]

        self.walkLeftSprite = [
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoIzuierda1.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoIzquierda2.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoIzquierda3.png"
                ),
                (85, 132),
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "./src/media/movimientosJugador/corriendoIzquierda4.png"
                ),
                (85, 132),
            ),
        ]
        self.jumpSprites = [
            [
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoDerecha1.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoDerecha2.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoDerecha3.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoDerecha4.png"
                    ),
                    (85, 132),
                ),
            ],
            [
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoIzquierda1.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoIzquierda2.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoIzquierda3.png"
                    ),
                    (85, 132),
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        "./src/media/movimientosJugador/saltoIzquierda4.png"
                    ),
                    (85, 132),
                ),
            ],
        ]
        self.direction = 0
        # self.frames = [
        #     [
        #         pygame.Rect((0,  0, 60,  90)),
        #         pygame.Rect((90, 0, 90, 90)),
        #         pygame.Rect((0, 90, 60, 90)),
        #         pygame.Rect((90, 90,  90 , 90 ))
        #     ]
        # ]

    def moveLeft(self, window, frame):
        self.image = self.idleSprite[1]
        self.draw(window, self.x - self.speedx, self.y)
        self.image = self.walkLeftSprite[frame]
        #print("Izquierda frame: " + str(frame))
        frame += 1
        self.direction = 1
        if frame == 4:
            frame = 0
        return frame

    def moveRight(self, window, frame):
        self.image = self.idleSprite[0]
        self.draw(window, self.x + self.speedx, self.y)
        self.image = self.walkRightSprite[frame]
        #print("Derecha frame: " + str(frame))
        frame += 1
        self.direction = 0
        if frame == 4:
            frame = 0
            
        return frame

    def jump(self, window, frame):
        self.image = self.idleSprite[self.direction]
        self.draw(window, self.x, self.y -self.isJumping)
        self.image = self.jumpSprites[self.direction][frame]
        #print("Salto frame: " + str(frame))
        frame += 1
        if frame == 4:
            frame = 0
            self.isJumping+=1
            if (self.y<=200):
                self.isJumping=0


        #if (self.up()==True or self.down()==False):
        #    self.x+=5
        #    self.y+=5
        #else:
         #   self.x+=5
          #  self.y-=25
        #print (self.y)
        return frame
    def downing(self, window, frame):
        self.image = self.idleSprite[self.direction]
        self.draw(window, self.x, self.y +self.isJumping)
        #self.image = self.jumpSprites[self.direction][frame]
        #print("Salto frame: " + str(frame))
        if(self.y>=310):
            self.isJumping=0
        else:
            self.isJumping+=1
           
    def up(self):
        bandera=False
        if (self.y<=200):
            bandera=True
        return bandera
    
    def down(self):
        bandera=False
        if (self.y>=305):
            bandera=True
        return bandera

    def movePlayer(self):
        self.x = 5
        self.y = 410
        
    def movePlayer2(self):
        self.x=700
        self.y=410


