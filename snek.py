#Imports the pygame library 
import pygame as pg
from random import randrange 
import menu as gameMenu
from menu import gameOverMenu


# Initialize variables for game state and menu state
in_game = False
gameMenu.menu()

# Set window caption to SNEK
pg.display.set_caption("SNEK")

# Set window and tile size variables for the game
WINDOW = 1000
tileSize = 50
range = (tileSize // 2, WINDOW - tileSize // 2, tileSize)
score = 0

# Create a lambda function to get a random position within the window based on the range variable
getRandomPos = lambda: [randrange(*range), randrange(*range)]

# Create the snek as a rect rectangle object with the segments being copies of the main snake object. The snekDir variable is used to keep track of the direction the snek is moving in
snek = pg.rect.Rect([0,0, tileSize - 2 , tileSize - 2])
snek.center = getRandomPos()
length = 1
segments = [snek.copy()]
snekDir = (0,0)

# Set time and time step variables for snek movement. Time step (time is in ms) being how much the snek moves during each clock cycle  (time_step = 100 means the snek moves 10 pixels per second)
time, time_step = 0, 100

# Create the apple as a rectangle object, cloned from how the snek spawns
apple = snek.copy()
apple.center = getRandomPos()

# Create the window, based on how big the WINDOW variable is. In this case the screen size would be (WINDOW, WINDOW) meaning (1000,1000) pixels 
screen = pg.display.set_mode([WINDOW] * 2)

# Create a clock object for frame rate, determine the amount of updates there is per second FPS = 60
clock = pg.time.Clock()

# Create a directions dictionary to keep track of the allowed keys for movement 
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

# Function to handle keydown events. If the key pressed is escape, the game is reset and the main menu is called. If the key pressed is a direction key, the snek is moved in that direction
def keydownEvent(event):
    if event.key == pg.K_ESCAPE:
        resetGame()
        gameMenu.menu()
    elif event.key == pg.K_w and dirs[pg.K_w]:
        moveSnake((0, -tileSize))
    elif event.key == pg.K_s and dirs[pg.K_s]:
        moveSnake((0, tileSize))
    elif event.key == pg.K_a and dirs[pg.K_a]:
        moveSnake((-tileSize, 0))
    elif event.key == pg.K_d and dirs[pg.K_d]:
        moveSnake((tileSize, 0))

# Function to move the snake in a certain direction based on the key pressed
def moveSnake(direction):
    global snekDir
    snekDir = direction
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
    dirs[direction] = 0

# Resets the game when called. If resetFromMainMenu is True, it resets the snake, apple, and other game variables to their initial state 
def resetGame():
    global snek, apple, segments, length, snekDir, score
    snek.center, apple.center = getRandomPos(), getRandomPos()
    length, snekDir = 1, (0, 0)
    segments = [snek.copy()]
    score = 0

# Keeps the score saved 
def handleScore():
    global score
    score += 1

# Function to handle the game score logic and update the game state 
def displayScore(score, screen):
    font = pg.font.Font(None, 30)

    textScore = font.render(f"        {score}", True, ("gold"))
    textRectScore = textScore.get_rect()
    textRectScore.right = screen.get_width() - 10
    textRectScore.bottom = screen.get_height() - 10

    text = font.render("Score:       ", True, ("white"))
    textRect = text.get_rect()
    textRect.right = screen.get_width() - 10
    textRect.bottom = screen.get_height() - 10


    # Draw the rectangle object
    rect = pg.Rect(textRect.left - 15, textRect.top - 10, textRect.width + 25, textRect.height + 20)
    pg.draw.rect(screen, ("gray"), rect, 2)

    screen.blit(textScore, textRectScore)
    screen.blit(text, textRect)


# Main game loop 
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            keydownEvent(event)

    # Set the in game background color to black
    screen.fill('black')

    # Check for collision with borders and the snek going into it's own body "selfeating". If the snek collided with anything else other then the apple it loads up the game over menu and resets the game 
    selfEating = pg.Rect.collidelist(snek, segments[:-1]) != -1
    if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > WINDOW or selfEating:
        gameOverMenu()
        score = 0
        snek.center, apple.center = getRandomPos(), getRandomPos()
        length, snekDir = 1, (0, 0)
        segments = [snek.copy()]

    # Check apple collision with snek, if it collided correctly it will remove the apple and respawn it thus increasing the snek length by 1 (adding another segment to its body) and updating the score
    if snek.center == apple.center:
        apple.center = getRandomPos()
        length += 1 
        handleScore()
        

    # Draw apple, make sure that the apple can be seen by the user 
    pg.draw.rect(screen, "red", apple)

    # Draw snek, make sure that the snek is rendered the same goes for its segments 
    [pg.draw.rect(screen,"green", segment) for segment in segments]

    # Move snek based on time & speed 
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snek.move_ip(snekDir)
        segments.append(snek.copy())
        segments = segments[-length:]

    # Fps and main displaying feature 
    displayScore(score, screen)      
    pg.display.flip()
    clock.tick(60)


