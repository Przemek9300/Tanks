
import pygame
from Blocks.BlockBase import BlockBase
class BushBlock(BlockBase):
    def __init__(self,image_file, pos):
        super().__init__()
        self.image = pygame.image.load(image_file)

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]




