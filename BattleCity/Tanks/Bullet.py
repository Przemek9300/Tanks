import pygame
import Setting
class Bullet(pygame.sprite.Sprite):
    states = ["UP", "LEFT", "RIGHT", "DOWN"]
    state = ""
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.move_y = Setting.BulletSpeed
        self.move_x = Setting.BulletSpeed
    def draw(self,surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if(self.state == "LEFT"):
            self.rect.x -= self.move_y
        if(self.state == "RIGHT"):
            self.rect.x += self.move_y
        if (self.state == "UP"):
            self.rect.y -= self.move_y
        if (self.state == "DOWN"):
            self.rect.y += self.move_y
        if self.rect.bottom < 0:
            self.kill()


