import pygame
import Setting
from Level.LevelHandler import LevelHandler
from Blocks.CustomBlock import CustomBlock


CZARNY = pygame.color.THECOLORS['black']
def saveLevel(level):
    plik = open('Level/Custom/level.txt', 'w')
    i = 0
    for line in level:
        if i != 0:
            plik.write('\n')
        i += 1
        for char in line:
            plik.write(char)
class Construction():

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Setting.resolution,pygame.FULLSCREEN)
        pygame.display.set_caption('CREATOR')
        clock = pygame.time.Clock()
        custom = CustomBlock("img/statek.png")
        levelHandler = LevelHandler()
        level = levelHandler.emptyTemplate()
        levelHandler.gen2(level)
        blocks = levelHandler.map()
        main_loop = True
        while main_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_loop = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_loop = False
                    if event.key == pygame.K_s:
                        saveLevel(level)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(int(custom.rect.y/25))
                        print(int(custom.rect.x/25))
                        level[int(custom.rect.y/25)][int(custom.rect.x/25)] = custom.currentState
                        blocks.empty()
                        levelHandler.gen2(level)
                        blocks = levelHandler.map()
                        print(blocks)

                    else:
                        custom.reaction(event)
                else:
                    custom.stop()
            screen.fill(CZARNY)
            blocks.draw(screen)
            custom.draw(screen)
            custom.update()
            pygame.display.flip()
            clock.tick(10)