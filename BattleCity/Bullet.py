import pygame
import Setting
class Bullet(pygame.sprite.Sprite):
    states = ["UP", "LEFT", "RIGHT", "DOWN"]
    state = ""
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.speed = Setting.BulletSpeed
    def draw(self,surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if(self.state == "LEFT"):
            self.rect.x -= self.speed
        if(self.state == "RIGHT"):
            self.rect.x += self.speed
        if (self.state == "UP"):
            self.rect.y -= self.speed
        if (self.state == "DOWN"):
            self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > Setting.resolution[1]:
            self.kill()
        if self.rect.left > Setting.resolution[0]:
            self.kill()
        if self.rect.right < 0:
            self.kill()

