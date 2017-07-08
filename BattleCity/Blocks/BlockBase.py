import pygame
from abc import ABCMeta, abstractmethod


class BlockBase(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    @abstractmethod
    def update(self):
        pass

