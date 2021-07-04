from src.Sprite import Sprite

import pygame


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/sprites.png")

        print("Player")
        self.speedx = 10
        idleSprite=[pygame.image.load("./src/media/movimientosJugador/reposoDerecha.png"),
               pygame.image.load("./src/media/movimientosJugador/reposoIzquierda.png")]

        walkRightSprite=[pygame.image.load("./src/media/movimientosJugador/corriendoDerecha1.png"),
                       pygame.image.load("./src/media/movimientosJugador/corriendoDerecha2.png"),
                       pygame.image.load("./src/media/movimientosJugador/corriendoDerecha3.png"),
                       pygame.image.load("./src/media/movimientosJugador/corriendoDerecha4.png")]

        walkLeftSprite=[pygame.image.load("./src/media/movimientosJugador/corriendoIzuierda1.png"),
                         pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda2.png"),
                         pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda3.png"),
                         pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda4.png")]

        jumpRightSprite=[pygame.image.load("./src/media/movimientosJugador/saltoDerecha1.png"),
                     pygame.image.load("./src/media/movimientosJugador/saltoDerecha2.png"),
                     pygame.image.load("./src/media/movimientosJugador/saltoDerecha3.png"),
                     pygame.image.load("./src/media/movimientosJugador/saltoDerecha4.png")]

        jumpLeftSprite=[pygame.image.load("./src/media/movimientosJugador/saltoIzquierda1.png"),
                       pygame.image.load("./src/media/movimientosJugador/saltoIzquierda2.png"),
                       pygame.image.load("./src/media/movimientosJugador/saltoIzquierda3.png"),
                       pygame.image.load("./src/media/movimientosJugador/saltoIzquierda4.png")]
        self.frames = [
            [
                pygame.Rect((0,  0, 60,  90)), 
                pygame.Rect((90, 0, 90, 90)), 
                pygame.Rect((0, 90, 60, 90)), 
                pygame.Rect((90, 90,  90 , 90 ))
            ]
        ]
    def moveLeft(self):
        self.setInWindow(self.x, self.y, 2)
    def moveRight(self):
        self.setInWindow(self.x, self.y, 0)
    def jump(self):
        pass
