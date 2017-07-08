import pygame
import Setting
from Blocks.BlockBase import BlockBase


class CustomBlock(BlockBase):
    states = ['B', 'S', 'W', 'P', 'T', " ", "O"]
    images = ["img/brick.png", "img/solid.png", "img/water.png", "img/bush.png", "img/statek.png", "img/empty.png", "img/Eagl.png"]
    currentImage = images[0]
    currentState = states[0]
    currentIndex = 0
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.move_x = 0
        self.move_y = 0

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def nextImage(self):
        if self.currentImage == self.images[len(self.images)-1]:
            self.currentIndex = 0
            self.currentImage = self.images[self.currentIndex]
            self.currentState = self.states[self.currentIndex]
        else:
            self.currentIndex+=1
            self.currentImage = self.images[self.currentIndex]
            self.currentState = self.states[self.currentIndex]

    def changeImage(self, image_file):
        self.image = pygame.image.load(image_file)

    def move_up(self):
        self.move_y = -25

    def move_left(self):
        self.move_x = -25

    def move_right(self):
        self.move_x = 25

    def move_down(self):
        self.move_y = 25

    def stop(self):
        self.move_x = 0
        self.move_y = 0
    def reaction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right()
            if event.key == pygame.K_LEFT:
                self.move_left()
            if event.key == pygame.K_UP:
                self.move_up()
            if event.key == pygame.K_DOWN:
                self.move_down()
            if event.key == pygame.K_r:
                self.nextImage()
                self.changeImage(self.currentImage)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.move_x < 0 :
                self.stop()
            if event.key == pygame.K_RIGHT  and self.move_x > 0:
                self.stop()
            if event.key == pygame.K_DOWN and self.move_y > 0 :
                self.stop()
            if event.key == pygame.K_UP and self.move_y < 0:
                self.stop()
    def update(self):
        self.rect.x += self.move_x
        if self.rect.right > Setting.resolution[0]+25:
            self.rect.right = Setting.resolution[0]+25
        if self.rect.left < 0:
            self.rect.left = 0
        self.rect.y += self.move_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Setting.resolution[1]+25:
            self.rect.bottom = Setting.resolution[1]+25
