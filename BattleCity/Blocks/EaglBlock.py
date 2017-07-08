from Blocks.BlockBase import BlockBase
import pygame
class EaglBlock(BlockBase):
    life = True
    def __init__(self,image_file, pos):
        super().__init__()
        self.image = pygame.image.load("img/Eagl.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def destroy(self):
        self.image = pygame.image.load("img/EaglDead.png")
        self.life = False