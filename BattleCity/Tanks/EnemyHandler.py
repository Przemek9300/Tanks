import Setting
import pygame
from Tanks import Enemy


class EnemyHandler():

    pygame.init()

    def __init__(self,enemyBullets):
        self.enemyBullets = enemyBullets
        self.tanks = pygame.sprite.Group()
        self.count = Setting.EnemyCount
        self.sound = pygame.mixer.Sound("music/DestroyedTank.wav")

    def reset(self):
        self.count = Setting.EnemyCount
        for tank in self.tanks:
            tank.spawn()
    def shot(self):
        for tank in self.tanks:
            tank.shot(self.enemyBullets)
    def getBlocks(self,bloks):
        for tank in self.tanks:
            tank.getBlocks(bloks)
    def getEnemyTanks(self):
        for tank in self.tanks:
            tank.getTanks(self.tanks)
    def getPlayers(self, players):
        for tank in self.tanks:
            tank.getTanks(players)


    def bulletsCollisionWithSelf(self, playerBullets):
        for bullet in playerBullets:
            for eneme in self.tanks:
                if pygame.sprite.collide_rect(eneme, bullet):
                    bullet.kill()
                    if self.count > 0:
                        self.count -= 1
                        eneme.spawn()
                    else:
                        self.sound.play()
                        eneme.kill()
