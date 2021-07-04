from src.Sprite import Sprite

import pygame



# reposo=[pygame.image.load("./src/media/movimientosJugador/reposoDerecha.png"),
#        pygame.image.load("./src/media/movimientosJugador/reposoIzquierda.png")]

# caminarDerecha=[pygame.image.load("./src/media/movimientosJugador/corriendoDerecha1.png"),
#                pygame.image.load("./src/media/movimientosJugador/corriendoDerecha2.png"),
#                pygame.image.load("./src/media/movimientosJugador/corriendoDerecha3.png"),
#                pygame.image.load("./src/media/movimientosJugador/corriendoDerecha4.png")]

# caminaIzquierda=[pygame.image.load("./src/media/movimientosJugador/corriendoIzuierda1.png"),
#                  pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda2.png"),
#                  pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda3.png"),
#                  pygame.image.load("./src/media/movimientosJugador/corriendoIzquierda4.png")]

# saltoDerecha=[pygame.image.load("./src/media/movimientosJugador/saltoDerecha1.png"),
#              pygame.image.load("./src/media/movimientosJugador/saltoDerecha2.png"),
#              pygame.image.load("./src/media/movimientosJugador/saltoDerecha3.png"),
#              pygame.image.load("./src/media/movimientosJugador/saltoDerecha4.png")]

# saltoIzquierda=[pygame.image.load("./src/media/movimientosJugador/saltoIzquierda1.png"),
#                pygame.image.load("./src/media/movimientosJugador/saltoIzquierda2.png"),
#                pygame.image.load("./src/media/movimientosJugador/saltoIzquierda3.png"),
#                pygame.image.load("./src/media/movimientosJugador/saltoIzquierda4.png")]

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, "./src/media/player.png")
        print("Player")
        self.speedx = 0
        self.frames = [pygame.Rect((0,  0, 60,  90)), pygame.Rect((90, 0, 90, 90)), pygame.Rect((0, 90, 60, 90)), pygame.Rect((90, 90,  90 , 90 ))]
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
    def jump(self):
        pass
