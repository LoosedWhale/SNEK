# Definiera klasser till speler
# Snake, Apple, Menu, mm.
# PyGame

import pygame as pg
from pygame import * 
from pygame.math import Vector2
from random import randrange 

pg.display.set_caption("SNEK GAME")

class SNEK:
    def __init__(self):
        
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
    
        
    def drawSnek(self):
        #self.updateHeadGraphics()

        for index, block in enumerate(self.body):
            xPos = int(block.x * tileSize)
            yPos = int(block.y * tileSize)
            snekRect = pg.Rect(xPos, yPos, tileSize, tileSize)

            if index == 0:
                pg.draw.rect(screen,(0, 200, 0), snekRect)
            
            else:
                pg.draw.rect(screen, (0, 200, 0), snekRect)

    def moveSnek(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]
    
    def updateHeadGraphics(self):   
        pass


    
class FRUIT:
    def __init__(self):
        self.randomize()
    
    def drawFruit(self):
        fruitRect = pg.Rect(int(self.pos.x * tileSize), int(self.pos.y * tileSize),tileSize,tileSize)
        pg.draw.rect(screen,("red"), fruitRect)


    def randomize(self):
        self.x = randrange(0, tileNum)
        self.y = randrange(0, tileNum)
        self.pos = Vector2(self.x, self.y)
    
        
class MENU:
    def __init__(self):
        pass
        

class MAIN:
    def __init__(self):
        self.snek = SNEK()
        self.apple = FRUIT()

    def drawElements(self):
        self.apple.drawFruit()
        self.snek.drawSnek()
    
    def update(self):
        self.snek.moveSnek()
    
    def gameOver(self):
        self.snek.reset()


pg.init()
tileSize = 40
tileNum = 25
screen = pg.display.set_mode((tileNum * tileSize, tileNum * tileSize))
fps = pg.time.Clock()
SCREENUPDATE = pg.USEREVENT
pg.time.set_timer(SCREENUPDATE, 100)
Game = MAIN()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
        if event.type == SCREENUPDATE:
            Game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                if Game.snek.direction.y != 1:
                    Game.snek.direction = Vector2(0, -1)
            if event.key == pg.K_s:
                if Game.snek.direction.y != -1:
                    Game.snek.direction = Vector2(0, 1)
            if event.key == pg.K_a:
                if Game.snek.direction.x != 1:
                    Game.snek.direction = Vector2(-1, 0)
            if event.key == pg.K_d:
                if Game.snek.direction.x != -1:
                    Game.snek.direction = Vector2(1, 0)
            if event.key == pg.K_r:
                Game.apple.randomize()

    screen.fill("black")
    Game.drawElements()
    pg.display.update()
    fps.tick(60)
