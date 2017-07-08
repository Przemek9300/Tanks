import pygame
from abc import ABCMeta, abstractmethod

class TankBase(pygame.sprite.Sprite):
    states = ["UP","LEFT","RIGHT","DOWN"]
    state = ""
    angle = 0
    __metaclass__ = ABCMeta
    def __init__(self):
        super().__init__()
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.last = pygame.time.get_ticks()
        self.fireSpeed = 300
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([38, 40])

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def getBlocks(self, blocks):
        self.blocks = blocks
    @abstractmethod
    def update(self):
        pass
