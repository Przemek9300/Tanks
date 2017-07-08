import pygame
import Setting
from Blocks.BrickBlock import BrickBlock
from Blocks.SolidBlock import SolidBlock
from Blocks.BushBlock import BushBlock
from Blocks.WaterBlock import WaterBlock
from Blocks.EaglBlock import  EaglBlock


class LevelHandler:
    blocks = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    solids = pygame.sprite.Group()
    water = pygame.sprite.Group()
    bushes = pygame.sprite.Group()  # mistaken use of a class variable
    row = 0
    sizeX = int (Setting.resolution[0]/25)
    sizeY = int(Setting.resolution[1]/25)
    def __init__(self):
        pass
    def emptyTemplate(self):
        lvl = []
        for cols in range(self.sizeY):
            lvl.append([])
            for row in range(self.sizeX):
                lvl[cols].append(' ')

        return lvl

    def gen(self):
        x = y = 0
        for row in self.level:
            for col in row:
                if col == "B":
                    self.blocks.add(BrickBlock("img/brick.png", [x, y]))
                if col == "S":
                    self.blocks.add(SolidBlock("img/solid.png", [x, y]))
                if col == "P":
                    self.blocks.add(BushBlock("img/bush.png", [x, y]))
                if col == "W":
                    self.blocks.add(WaterBlock("img/water.png", [x, y]))
                if col == "O":
                    self.blocks.add(EaglBlock("img/Eagl.png", [x, y]))
                x += 25
            y += 25
            x = 0

    def gen2(self, level):
        x = y = 0
        for row in level:
            for col in row:
                if col == "B":
                    self.blocks.add(BrickBlock("img/brick.png", [x, y]))
                if col == "S":
                    self.blocks.add(SolidBlock("img/solid.png", [x, y]))
                if col == "P":
                    self.blocks.add(BushBlock("img/bush.png", [x, y]))
                if col == "W":
                    self.blocks.add(WaterBlock("img/water.png", [x, y]))
                if col == "O":
                    self.blocks.add(EaglBlock("img/Eagl.png", [x, y]))
                x += 25
            y += 25
            x = 0

    def map(self):
        return self.blocks

    def loadFile(self,loc):
        with open(loc) as f:
            self.level = f.read().splitlines()




