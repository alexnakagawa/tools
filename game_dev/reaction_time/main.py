import pygame, sys, random
from pygame.locals import *
from objects import *

def main(argv):

    # Game Initialized -----------------

    pygame.init()
    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()

    # ----------------------------------

    # Colors
    WHITE  = (255, 255, 255)
    YELLOW = (255, 255, 0  )
    RED    = (255, 0,   0  )
    PURPLE = (128, 0,   128)
    BLACK  = (10 , 10,  10 )

    #Fonts
    FONT36 = pygame.font.Font(None, 36)
    FONT18 = pygame.font.Font(None, 18)

    # Base
    DISPLAY_SCREEN = pygame.display.set_mode((1024, 780))
    pygame.display.set_caption('Reaction Time Simulation')

    player = Subject(first_name=argv[0], last_name=arg[1], user_id=argv[2])
    print(player)

    # Fill background
    background = pygame.Surface(DISPLAY_SCREEN.get_size())
    background = background.convert()
    background.fill(WHITE)

    # Title
    title = FONT36.render("Reaction Time Simulation", 1, (10, 10, 10))
    title_pos = title.get_rect()
    title_pos.centerx = background.get_rect().centerx
    background.blit(title, title_pos)

    # Blit background to the screen
    DISPLAY_SCREEN.blit(background, (0, 0))
    pygame.display.flip()

    # Instructions
    instructions = FONT18.render("INSTRUCTIONS:", 1, BLACK)
    instructions_pos = instructions.get_rect()
    instructions_pos.centerx = background.get_rect().centerx
    instructions_pos.centery = background.get_rect().centery - 300
    DISPLAY_SCREEN.blit(instructions,instructions_pos)

    # Event loop -----------------------

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # pressed = pygame.key.get_pressed()

        pygame.display.update()

    # ----------------------------------


if __name__ == '__main__':
    main(sys.argv[1:])