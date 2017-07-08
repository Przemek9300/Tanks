import pygame

from Blocks.BrickBlock import BrickBlock
from Blocks.WaterBlock import WaterBlock
from Blocks.SolidBlock import SolidBlock
from Blocks.EaglBlock import EaglBlock

class Collision():

    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

    def bulletCollisionWithBlocks(self, bullets, blocks):
        for bullet in bullets:
            for block in blocks:
                if(pygame.sprite.collide_rect(bullet, block) and isinstance(block,BrickBlock)):
                    bullet.kill()
                    block.kill()
                if (pygame.sprite.collide_rect(bullet, block) and isinstance(block, SolidBlock)):
                    bullet.kill()
                if (pygame.sprite.collide_rect(bullet, block) and isinstance(block, EaglBlock)):
                    bullet.kill()
                    block.destroy()


    def bulletsCollisionWithBullets(self, bullets, enemybullets):
        pygame.sprite.groupcollide(bullets, enemybullets, True, True)

    def bulletsCollisionWithPlayer(self, players, enemyBullets):
        for bullet in enemyBullets:
            for player in players:
                if pygame.sprite.collide_rect(player, bullet):
                    #sound.play()
                    bullet.kill
                    if player.live > 0:
                        player.live -= 1
                        player.spawn()
                    else:
                        player.kill()

    def playerCollisionWithEnemy(self, players, enemes):
        for enemem in enemes:
            for player in players:
                if pygame.sprite.collide_rect(player, enemem):
                    if player.live > 0:
                        player.live -= 1
                        player.spawn()
                    else:
                        player.kill()
    def SelfbulletsCollisionWithEnemy(self, enemes, enemyBullets):
        pygame.sprite.groupcollide(enemes, enemyBullets, False, True)

