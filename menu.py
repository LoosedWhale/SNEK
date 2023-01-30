# Imports 
import pygame as pg
import sys

# Defines values for tje variables screen, clock and calls the integrated pygame init functions 
pg.init()
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()

# The main menu. Determines The; caption name, font , keydown events, how and where the text labels should be placed, colors.  
def menu():
    menuRunning = True
    pg.display.set_caption("SNEK menu")
    font = pg.font.SysFont("comicsansms", 30)
    font_big = pg.font.SysFont("comicsansms", 50)
    while menuRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    menuRunning = False
                    pg.display.set_caption("SNEK")
        screen.fill("black")
        label = font_big.render("SNEK", 1, (255, 255, 0))
        label_rect = label.get_rect(center=(500,150))
        screen.blit(label, label_rect)
        label = font.render("WASD to move", 1, (255, 255, 0))
        label_rect = label.get_rect(center=(500, 300))
        screen.blit(label, label_rect)
        label = font.render("Press 'SPACE' to start", 1, (255, 255, 0))
        label_rect = label.get_rect(center=(500, 350))
        screen.blit(label, label_rect)
        pg.display.flip()
        clock.tick(60)

# The game over menu. Determines The; caption name, font , keydown events, how and where the text labels should be placed, colors.  
def gameOverMenu():
    gameOverRunning = True
    pg.display.set_caption("SNEK GAME OVER")
    font = pg.font.SysFont("comicsansms", 30)
    font_big = pg.font.SysFont("comicsansms", 50)
    while gameOverRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gameOverRunning = False
                    pg.display.set_caption("SNEK")
                    menu()
        screen.fill("black")
        label = font_big.render("Game Over", 1, (255, 0, 0))
        label_rect = label.get_rect(center=(500,150))
        screen.blit(label, label_rect)
        label = font.render("Press 'SPACE' to return to main menu", 1, (255, 255, 0))
        label_rect = label.get_rect(center=(500, 300))
        screen.blit(label, label_rect)
        pg.display.flip()
        clock.tick(60)
