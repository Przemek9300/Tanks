import pygame
class Heart():
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([38, 40])
        self.image = pygame.image.load("img/heart.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def draw(self, surface):
        surface.blit(self.image, self.rect)