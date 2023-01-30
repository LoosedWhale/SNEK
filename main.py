import pygame as pg
import sys
from random import randrange 

WINDOW = 1000
TileSize = 50
range = (TileSize // 2, WINDOW - TileSize // 2, TileSize)
getRandomPos = lambda: [randrange(*range), randrange(*range)]
snek = pg.rect.Rect([0,0, TileSize - 2 , TileSize - 2])
snek.center = getRandomPos()
length = 1
segments = [snek.copy()]
snekDir = (0,0)
#time speed control change the later value to change speed
time, time_step = 0, 100
apple = snek.copy()
apple.center =getRandomPos()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snekDir = (0, -TileSize)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snekDir = (0, TileSize)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snekDir = (-TileSize, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snekDir = (TileSize,0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

                            

    screen.fill('black')
    #check borders and selfeating 
    selfEating = pg.Rect.collidelist(snek, segments[:-1]) != -1
    if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > WINDOW or selfEating:
        snek.center, apple.center = getRandomPos(), getRandomPos()
        length, snekDir = 1, (0, 0)
        segments = [snek.copy()]
    #check apple collision with snek
    if snek.center == apple.center:
        apple.center = getRandomPos()
        length += 1 
    #Draw apple
    pg.draw.rect(screen, "red", apple)
    #Draw snek
    [pg.draw.rect(screen,"green", segment) for segment in segments]
    #Move snek based on time & speed
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snek.move_ip(snekDir)
        segments.append(snek.copy())
        segments = segments[-length:]
    pg.display.flip()
    clock.tick(60)
