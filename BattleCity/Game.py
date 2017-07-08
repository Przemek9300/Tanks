import pygame
from Collision import Collision
from Tanks.Player import Player
from Tanks.Enemy import Enemy
from Tanks.TigerTank import TigerTank
from Level.LevelHandler import LevelHandler
from Tanks.EnemyHandler import EnemyHandler
from Tanks.GhostTank import GhostTank
from Blocks.EaglBlock import EaglBlock


from Credits import Credits


import pygame.mixer


import Setting

CZARNY = pygame.color.THECOLORS["black"]
BIALY = pygame.color.THECOLORS["white"]
class Game(object):
    blocks = pygame.sprite.Group()
    def run(self):


        nrLevel = 0
        pygame.init()
        sound = pygame.mixer.Sound("music/BackGround.wav")
        soundLose = pygame.mixer.Sound("music/Lose.wav")
        soundWin = pygame.mixer.Sound("music/Win.wav")
        sound.play(1)
        screen = pygame.display.set_mode(Setting.resolution, pygame.FULLSCREEN)


        pygame.display.set_caption('Croko')
        clock = pygame.time.Clock()
        main_loop = True
        collision = Collision()
        player = Player("img/PlayerUP.png",1)
        players = pygame.sprite.Group()
        players.add(player)


        level = LevelHandler()

        level.loadFile(Setting.LEVELS[nrLevel])
        level.gen()
        playerBullets = pygame.sprite.Group()
        enemyBullets = pygame.sprite.Group()
        enemy = TigerTank(Setting.EnemySpawn[0])
        enemy1 = GhostTank(Setting.EnemySpawn[1])
        enemy2 = Enemy(Setting.EnemySpawn[2])
        enemy3 = Enemy(Setting.EnemySpawn[3])
        enem = EnemyHandler(enemyBullets)
        enem.tanks.add(enemy)
        enem.tanks.add(enemy1)
        enem.tanks.add(enemy2)
        enem.tanks.add(enemy3)
        credit = Credits()
        self.blocks = pygame.sprite.Group()
        self.blocks.remove(self.blocks)
        self.blocks = level.map()

        while main_loop:


            pygame.mouse.set_visible(False)
            player.getBlocks(self.blocks)
            enem.getBlocks(self.blocks)
            enem.getEnemyTanks()
            if(enem.count <= 0):
                if nrLevel is not Setting.LAST_LEVEL:
                    nrLevel += 1
                    self.blocks.remove(self.blocks)
                    level.loadFile(Setting.LEVELS[nrLevel])
                    level.gen()
                    enem.reset()
                else:
                    sound.stop()
                    soundWin.play(1)
                    pygame.time.wait(4500)
                    credit.run()
                    main_loop = False
            if(player.live <= 0):
                sound.stop()
                soundLose.play(1)
                pygame.time.wait(4500)
                main_loop = False
            for block in self.blocks:
                if isinstance(block, EaglBlock):
                    if block.life <= 0:
                        sound.stop()
                        soundLose.play(1)
                        pygame.time.wait(4500)
                        main_loop = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_loop = False
                    sound.stop()
                else:
                    player.reaction(event, playerBullets)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            main_loop = False
                            sound.stop()

            screen.fill(CZARNY)


            collision.playerCollisionWithEnemy(players,enem.tanks)
            collision.SelfbulletsCollisionWithEnemy(enem.tanks, enemyBullets)
            collision.bulletsCollisionWithPlayer(players, enemyBullets)
            collision.bulletCollisionWithBlocks(playerBullets, self.blocks)
            collision.bulletCollisionWithBlocks(enemyBullets, self.blocks)
            collision.bulletsCollisionWithBullets(enemyBullets, playerBullets)
            enem.bulletsCollisionWithSelf(playerBullets)
            players.draw(screen)
            players.update()
            playerBullets.update()
            playerBullets.draw(screen)
            enem.tanks.draw(screen)
            enem.shot()
            enem.tanks.update()

            enemyBullets.draw(screen)

            enemyBullets.update()
            self.blocks.draw(screen)

            pygame.display.flip()
            clock.tick(30)
