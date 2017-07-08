import pygame, time

class Credits:
    def run(self):
        pygame.init()

        window = pygame.display.set_mode((1100, 700),pygame.FULLSCREEN)

        pygame.display.set_caption('Battle City')
        graphic = pygame.image.load('img/backgroundCredits.jpg')
        screen = pygame.display.get_surface()
        screen.blit(graphic, (0,0))
        pygame.display.flip()

        time.sleep(5)
        exit()