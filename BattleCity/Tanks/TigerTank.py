import pygame
import random
import Setting
from Bullet import Bullet
from Tanks.TankBase import TankBase
from Blocks.BushBlock import BushBlock
class TigerTank(TankBase):
    max_bullet = 5
    speed = 7
    tanks = []
    blocks = []
    spawnPoint = ()
    def __init__(self, pos ):
        super().__init__()
        self.image = pygame.image.load("img/enemyLEFT.png")
        self.rect = self.image.get_rect()
        self.spawnPoint = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.move_x = 0
        self.move_y = 0
        self.state = self.states[2]
        self.fireSpeed = 900
        self.changeImage()
    def spawn(self):
        self.rect.x = self.spawnPoint[0]
        self.rect.y = self.spawnPoint[1]

    def getTanks(self, tanks):
        self.tanks = tanks

    def changeImage(self):
        if self.state == self.states[0]:
            self.image = pygame.image.load("img/TigerUP.png")
        if self.state == self.states[1]:
            self.image = pygame.image.load("img/TigerLEFT.png")
        if self.state == self.states[2]:
            self.image = pygame.image.load("img/TigerRIGHT.png")
        if self.state == self.states[3]:
            self.image = pygame.image.load("img/TigerDOWN.png")
    def changeDir(self):
        self.state = random.choice(self.states)
        self.changeImage()
    def oppositDir(self):
        if self.state == "UP":
            self.state = "DOWN"
        if self.state == "LEFT":
            self.state = "RIGHT"
        if self.state == "LEFT":
            self.state = "RIGHT"
        if self.state == "DOWN":
            self.state = "UP"

    def move(self, state):
        if(state==self.states[0]):
            self.move_y = -self.speed
        if(state==self.states[1]):
            self.move_x = -self.speed
        if(state==self.states[2]):
            self.move_x = self.speed
        if(state==self.states[3]):
            self.move_y = self.speed

    def shot(self, bullets):
        now = pygame.time.get_ticks()

        if len(bullets) < self.max_bullet and now - self.last >= self.fireSpeed:
            self.last = now
            bullet = Bullet("img/Bullet.png")
            bullet.state = self.state
            if self.state == "UP":
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.bottom = self.rect.top

            if self.state == "DOWN":
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.top = self.rect.bottom

            if self.state == "LEFT":
                bullet.rect.centery = self.rect.centery
                bullet.rect.right = self.rect.left

            if self.state == "RIGHT":
                bullet.rect.centery = self.rect.centery
                bullet.rect.left = self.rect.right
            bullets.add(bullet)

    def update(self):
        self.move_x = 0
        self.move_y = 0
        self.move(self.state)
        self.rect.x += self.move_x

        tanks_hit_list = pygame.sprite.spritecollide(self, self.tanks, False)
        for tank in tanks_hit_list:
            if tank is not self:
                if self.move_x > 0:
                    self.changeDir()
                    self.rect.right = tank.rect.left
                else:
                    # Otherwise if we are moving left, do the opposite.
                    self.changeDir()
                    self.rect.left = tank.rect.right


        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if not isinstance(block, BushBlock):
                if self.move_x > 0:
                    self.changeDir()
                    self.rect.right = block.rect.left
                else:
                    # Otherwise if we are moving left, do the opposite.
                    self.changeDir()
                    self.rect.left = block.rect.right
        if self.rect.right > Setting.resolution[0]:
            self.rect.right = Setting.resolution[0]
            self.changeDir()
        if self.rect.left < 0:
            self.rect.left = 0
            self.changeDir()
        self.rect.y += self.move_y

        tanks_hit_list = pygame.sprite.spritecollide(self, self.tanks, False)
        for tank in tanks_hit_list:
            if tank is not self:
            # Reset our position based on the top/bottom of the object.
                if self.move_y > 0:
                    self.changeDir()
                    self.rect.bottom = tank.rect.top
                else:
                    self.changeDir()
                    self.rect.top = tank.rect.bottom

        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            if not isinstance(block, BushBlock):
            # Reset our position based on the top/bottom of the object.
                if self.move_y > 0:
                    self.changeDir()
                    self.rect.bottom = block.rect.top
                else:
                    self.changeDir()
                    self.rect.top = block.rect.bottom
        if self.rect.top < 0:
            self.rect.top = 0
            self.changeDir()
        if self.rect.bottom > Setting.resolution[1]:
            self.rect.bottom = Setting.resolution[1]
            self.changeDir()
