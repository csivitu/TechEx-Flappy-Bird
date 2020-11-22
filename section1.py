import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame 
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 40  # number of times the frame will be rendered in 1 sec
SCREENWIDTH = 289   # defining width
SCREENHEIGHT = 511  # defining height
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # sending height and 
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}

PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    #Game
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)


pygame.init() # Initialize all pygame's modules
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird CSI')
GAME_SPRITES['numbers'] = ( 
    pygame.image.load('gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('gallery/sprites/1.png').convert_alpha(),
    pygame.image.load('gallery/sprites/2.png').convert_alpha(),
    pygame.image.load('gallery/sprites/3.png').convert_alpha(),
    pygame.image.load('gallery/sprites/4.png').convert_alpha(),
    pygame.image.load('gallery/sprites/5.png').convert_alpha(),
    pygame.image.load('gallery/sprites/6.png').convert_alpha(),
    pygame.image.load('gallery/sprites/7.png').convert_alpha(),
    pygame.image.load('gallery/sprites/8.png').convert_alpha(),
    pygame.image.load('gallery/sprites/9.png').convert_alpha(),
)

GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()



welcomeScreen() # Shows welcome screen to the user until he presses a button
