import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports

# Global Variables for the game
FPS = 40  # number of times the frame will be rendered in 1 sec
SCREENWIDTH = 289  # defining width
SCREENHEIGHT = 511  # defining height
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # sending height and
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}

PLAYER = "gallery/sprites/bird.png"
BACKGROUND = "gallery/sprites/background.png"
PIPE = "gallery/sprites/pipe.png"


def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES["player"].get_height()) / 2)
    messagex = int((SCREENWIDTH - GAME_SPRITES["message"].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    # Game
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES["background"], (0, 0))
                SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
                SCREEN.blit(GAME_SPRITES["message"], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[0]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[0]["y"]},
    ]
    # my List of lower pipes
    lowerPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[1]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[1]["y"]},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8  # velocity while flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):

                if playery > 0:  # Player is in the screen
                    playerVelY = playerFlapAccv

        crashTest = isCollide(
            playerx, playery, upperPipes, lowerPipes
        )  # This function will return true if the player is crashed
        if crashTest:
            return

        if playerVelY < playerMaxVelY:

            playerVelY += playerAccY
            print(playerVelY)

        playerHeight = GAME_SPRITES["player"].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe["x"] += pipeVelX
            lowerPipe["x"] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]["x"] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])

            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]["x"] < -GAME_SPRITES["pipe"][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES["background"], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES["pipe"][0], (upperPipe["x"], upperPipe["y"]))
            SCREEN.blit(GAME_SPRITES["pipe"][1], (lowerPipe["x"], lowerPipe["y"]))

        SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 25 or playery < 0:

        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES["pipe"][0].get_height()
        if (
            playery < pipeHeight + pipe["y"]
            and abs(playerx - pipe["x"]) < GAME_SPRITES["pipe"][0].get_width()
        ):

            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES["player"].get_height() > pipe["y"]) and abs(
            playerx - pipe["x"]
        ) < GAME_SPRITES["pipe"][0].get_width():

            return True

    return False


def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES["pipe"][0].get_height()
    print(pipeHeight)
    # print(pipeHeight)
    offset = SCREENHEIGHT / 3
    y2 = random.randrange(
        int(offset),
        int(SCREENHEIGHT - GAME_SPRITES["base"].get_height() - 0.5 * offset),
    )
    """range is always 100,220 """
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + 100
    pipe = [{"x": pipeX, "y": -y1}, {"x": pipeX, "y": y2}]  # upper Pipe  # lower Pipe
    return pipe


# This will be the main point from where our game will start
pygame.init()  # Initialize all pygame's modules
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird CSI")

GAME_SPRITES["message"] = pygame.image.load(
    "gallery/sprites/message.png"
).convert_alpha()
GAME_SPRITES["base"] = pygame.image.load("gallery/sprites/base.png").convert_alpha()
GAME_SPRITES["pipe"] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha(),
)


GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()
print(GAME_SPRITES["pipe"])
while True:
    welcomeScreen()  # Shows welcome screen to the user until he presses a button
    mainGame()  # This is the main game function
