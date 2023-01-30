#Imports the pygame library 
import pygame as pg
import sys
from pygame.math import Vector2
from random import randrange 

# Set window caption to SNEK
pg.display.set_caption("SNEK")

class SNEK:
    def __init__(self):
        #self.x = randrange(0, tileNum)
        #self.y = randrange(0, tileNum)
        #self.body = [Vector2(self.x, self.y + 1), Vector2(self.x, self.y), Vector2(self.x, self.y - 1)]
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.newBlock = False

        self.head_up = pg.image.load('Graphics/headUp.png').convert_alpha()
        self.head_down = pg.image.load('Graphics/headDown.png').convert_alpha()
        self.head_right = pg.image.load('Graphics/headRight.png').convert_alpha()
        self.head_left = pg.image.load('Graphics/headLeft.png').convert_alpha()
        self.onEatSound = pg.mixer.Sound('Sound/windowsShutdown.wav')

    def drawSnek(self):
        self.updateHeadGraphics()

        for index, block in enumerate(self.body):
            xPos = int(block.x * tileSize)
            yPos = int(block.y * tileSize)
            snekRect = pg.Rect(xPos, yPos, tileSize, tileSize)

            if index == 0:
                screen.blit(self.head, snekRect)
            
            else:
                pg.draw.rect(screen, (0, 200, 0), snekRect)
    
    def updateHeadGraphics(self):
        headRelation = self.body[1] - self.body[0]
        if headRelation == Vector2(1, 0): self.head = self.head_right
        elif headRelation == Vector2(-1, 0): self.head = self.head_left
        elif headRelation == Vector2(0, 1): self.head = self.head_down
        elif headRelation == Vector2(0, -1): self.head = self.head_up

    def moveSnek(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]
            self.newBlock = False
        else:
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]

    def addBlock(self):
        self.newBlock = True

    def playSound(self):
        self.onEatSound.play()
    
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()
    
    def drawFruit(self):
        fruitRect = pg.Rect(int(self.pos.x * tileSize), int(self.pos.y * tileSize),tileSize,tileSize)
        screen.blit(apple, fruitRect)


    def randomize(self):
        self.x = randrange(0, tileNum)
        self.y = randrange(0, tileNum)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snek = SNEK()
        self.apple = FRUIT()

    def update(self):
        self.snek.moveSnek()
        self.checkCollision()
        self.checkFail()
    

    def drawElements(self):
        self.apple.drawFruit()
        self.snek.drawSnek()
        self.drawScore()

    def checkCollision(self):
        if self.apple.pos == self.snek.body[0]:
            self.apple.randomize()
            self.snek.addBlock()
            self.snek.playSound()
        
        for block in self.snek.body[1:]:
            if block == self.apple.pos:
                self.apple.randomize()

    def checkFail(self):
        if not 0 <= self.snek.body[0].x < tileNum or not 0 <= self.snek.body[0].y < tileNum:
            self.gameOver()
        for block in self.snek.body[1:]:
            if block == self.snek.body[0]:
                self.gameOver()
        
    def gameOver(self):
        self.snek.reset()

    def drawScore(self):
        scoreText = str(len(self.snek.body) - 3)
        scoreSurface = gameFont.render(scoreText, True, ("gold"))
        scoreX = int(500)
        scoreY = int(20)
        scoreRect = scoreSurface.get_rect(center = (scoreX, scoreY))
        screen.blit(scoreSurface, scoreRect)


pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
# Set tile size variables for the game
tileSize = 40
tileNum = 25
clock = pg.time.Clock() 
screen = pg.display.set_mode((tileNum * tileSize, tileNum * tileSize))
apple = pg.image.load("Graphics/apple.png").convert_alpha()
gameFont = pg.font.Font("Font/PoetsenOne-Regular.ttf", 25)

# Create a lambda function to get a random position within the window based on the range variable
SCREENUPDATE = pg.USEREVENT
pg.time.set_timer(SCREENUPDATE, 100)

mainGame = MAIN()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            sys.exit()
        if event.type == SCREENUPDATE:
            mainGame.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                if mainGame.snek.direction.y != 1:
                    mainGame.snek.direction = Vector2(0, -1)
            if event.key == pg.K_s:
                if mainGame.snek.direction.y != -1:
                    mainGame.snek.direction = Vector2(0, 1)
            if event.key == pg.K_a:
                if mainGame.snek.direction.x != 1:
                    mainGame.snek.direction = Vector2(-1, 0)
            if event.key == pg.K_d:
                if mainGame.snek.direction.x != -1:
                    mainGame.snek.direction = Vector2(1, 0)

        screen.fill("black")
        mainGame.drawElements()
        pg.display.update()
        clock.tick(60)