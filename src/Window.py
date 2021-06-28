import pygame

def createWindow():
    pygame.init()

    size = 800, 600

    screen1 = pygame.display.set_mode(size)

    pygame.display.set_caption("Juego del chino")

    flag = True

    while flag:
        pygame.time.delay(50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False