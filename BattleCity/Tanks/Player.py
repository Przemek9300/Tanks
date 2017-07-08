import pygame
from Tanks.TankBase import TankBase
from Tanks.Bullet import Bullet
from Level.LevelHandler import LevelHandler
from Blocks.CustomBlock import CustomBlock
from Blocks.BushBlock import BushBlock
import Setting
from Blocks.SolidBlock import SolidBlock
from Blocks.WaterBlock import  WaterBlock

class Player(TankBase):
    max_bullet = 20
    blocks = []
    live = Setting.PlayerLive
    speed = Setting.PlayerSpeed
    pygame.init()

    def spawn(self):
        self.rect.x = Setting.PlayerSpawn[0]
        self.rect.y = Setting.PlayerSpawn[1]

    def __init__(self, image_file, move_x = 5, move_y = 5):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
        self.rect.x = Setting.PlayerSpawn[0]
        self.rect.y = Setting.PlayerSpawn[1]
        self.state = self.states[0]
        self.sound = pygame.mixer.Sound("music/ShotPlayer.wav")

    def move_up(self):
        self.image = pygame.image.load("img/PlayerUP.png")
        self.state = self.states[0]
        self.move_y = -self.speed

    def move_left(self):
        self.image = pygame.image.load("img/PlayerLEFT.png")
        self.state = self.states[1]
        self.move_x = -self.speed

    def move_right(self):
        self.image = pygame.image.load("img/PlayerRIGHT.png")
        self.state = self.states[2]
        self.move_x = self.speed


    def move_down(self):
        self.image = pygame.image.load("img/PlayerDOWN.png")
        self.state = self.states[3]
        self.move_y = self.speed

    def stop(self):
        self.move_x = 0
        self.move_y = 0

    def reaction(self, event, bullets_group):
        if event.type == pygame.KEYDOWN and self.live >= 0:
            if event.key == pygame.K_RIGHT:
                self.changeImage()
                self.move_right()
            if event.key == pygame.K_LEFT:
                self.changeImage()
                self.move_left()
            if event.key == pygame.K_UP:
                self.move_up()
            if event.key == pygame.K_DOWN:
                self.move_down()
            if event.key == pygame.K_SPACE:
                self.sound.play()
                if self.state is self.states[0]:
                    self.shot(bullets_group)
                if self.state is self.states[1]:
                    self.shot(bullets_group)
                if self.state is self.states[2]:
                    self.shot(bullets_group)
                if self.state is self.states[3]:
                    self.shot(bullets_group)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.move_x < 0 :
                self.stop()


            if event.key == pygame.K_RIGHT  and self.move_x > 0:
                self.stop()
            if event.key == pygame.K_DOWN and self.move_y > 0 :
                self.stop()
            if event.key == pygame.K_UP and self.move_y < 0:
                self.stop()

    def changeImage(self):
        if self.state == self.states[0]:
            self.image = pygame.image.load("img/statek.png")
        if self.state == self.states[1]:
            self.image = pygame.image.load("img/statekLEFT.png")
        if self.state == self.states[2]:
            self.image = pygame.image.load("img/statekRIGHT.png")
        if self.state == self.states[3]:
            self.image = pygame.image.load("img/statekDOWN.png")

    def update(self):
        self.rect.x += self.move_x
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if not isinstance(block, BushBlock):
                if self.move_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        if self.rect.right > Setting.resolution[0]:
            self.rect.right = Setting.resolution[0]
        if self.rect.left < 0:
            self.rect.left = 0
        self.rect.y += self.move_y
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if not isinstance(block, BushBlock):
                if self.move_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Setting.resolution[1]:
            self.rect.bottom = Setting.resolution[1]

    def shot(self, bullets_group):
        now = pygame.time.get_ticks()

        if len(bullets_group) < self.max_bullet and now - self.last >= self.fireSpeed:
            self.last = now
            bullet = Bullet("img/Bullet.png")
            bullet.state = self.state
            if self.state == "UP":
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.bottom = self.rect.top + 20

            if self.state == "DOWN":
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.top = self.rect.bottom


            if self.state == "LEFT":
                bullet.rect.centery = self.rect.centery
                bullet.rect.left = self.rect.left


            if self.state == "RIGHT":
                bullet.rect.centery = self.rect.centery
                bullet.rect.right = self.rect.right

            bullets_group.add(bullet)



