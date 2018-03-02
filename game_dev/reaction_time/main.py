try:
    import pygame
    import sys
    import random
    import math
    import os
    from pygame.locals import *
    from objects import *
    import constants as c
except ImportError as err:
    print("couldn't load module: %s" % err)
    sys.exit(2)

_cached_fonts = {}
_cached_text = {}


def main(argv):
    # Helper functions
    def wait():
        print('Waiting for input...')
        while True:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_SPACE:
                        print('[Space bar] was pressed.')
                        return
                    if ev.key == K_ESCAPE:
                        print('[Esc] was pressed. Exiting program...')
                        pygame.quit()
                        sys.exit()

    def make_font(fonts, size):
        available = pygame.font.get_fonts()
        # get_fonts() returns a list of lowercase spaceless font names
        choices = map(lambda x: x.lower().replace(' ', ''), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        return pygame.font.Font(None, size)

    def get_font(font_preferences, size):
        global _cached_fonts
        key = str(font_preferences) + '|' + str(size)
        font = _cached_fonts.get(key, None)
        if font is None:
            font = make_font(font_preferences, size)
            _cached_fonts[key] = font
        return font

    def create_text(text, fonts, size, text_color):
        global _cached_text
        key = '|'.join(map(str, (fonts, size, text_color, text)))
        image = _cached_text.get(key, None)
        if image is None:
            font = get_font(fonts, size)
            image = font.render(text, True, text_color)
            _cached_text[key] = image
        return image

    # Game Initialized -----------------
    pygame.init()
    fps = 30  # frames per second setting
    fps_clock = pygame.time.Clock()
    fps_clock.tick(fps)
    # ----------------------------------

    # Base
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Reaction Time Simulation')

    try:
        player = Subject(user_id=argv[0], first_name=argv[1], last_name=argv[2])
    except IndexError:
        print('ERROR: You must set arguments in the command line like so:\
               \npython main.py user_id first_name last_name\
               \npython main.py 01      Alex       Nakagawa')
        return
    print('Simulation has begun for:')
    print(player)

    # Surface 1: Background ------------
    background = pygame.Surface(screen.get_size())
    background = background.convert(background)
    background.fill(c.WHITE)

    # Title
    title = create_text("Reaction Time Simulation", c.PREF_FONTS, 36, c.BLACK)
    title_pos = title.get_rect()
    title_pos.centerx = background.get_rect().centerx
    background.blit(title, title_pos)

    # Blit background to the screen
    screen.blit(background, (0, 0))
    pygame.display.update()
    # ----------------------------------

    # Surface 2: Instructions ----------
    lines = ["INSTRUCTIONS:",
             "You will be the test subject in three variations of the same experiment.",
             "A countdown will begin at the start of each round.",
             "At the end of the countdown, wait for an object to appear on the screen.",
             "As soon as you spot it, press down and release the spacebar as quick as possible."]
    for i, line in enumerate(lines):
        instructions = create_text(line, c.PREF_FONTS, 24, c.RED)
        instructions_pos = instructions.get_rect()
        instructions_pos.centerx = background.get_rect().centerx
        instructions_pos.centery = background.get_rect().centery - (270 - 48*i)
        background.blit(instructions, instructions_pos)

    sb = create_text("Press the [spacebar] to continue", c.PREF_FONTS, 16, c.RED)
    sb_pos = sb.get_rect()
    sb_pos.topleft = c.SPACEBAR_LOC
    background.blit(sb, sb_pos)
    screen.blit(background, screen.get_rect())
    pygame.display.update()
    wait()
    # ----------------------------------

    # Surface 3: Countdown -------------
    countdown_background = pygame.Surface(screen.get_size())
    countdown_background = countdown_background.convert()
    countdown_background.fill(c.WHITE)

    get_ready = create_text("Get Ready...", c.PREF_FONTS, 24, c.BLACK)
    get_ready_pos = get_ready.get_rect()
    get_ready_pos.centerx = countdown_background.get_rect().centerx
    get_ready_pos.centery = countdown_background.get_rect().centery
    countdown_background.blit(get_ready, get_ready_pos)

    sb = create_text("Press the [spacebar] to continue", c.PREF_FONTS, 16, c.RED)
    sb_pos = sb.get_rect()
    sb_pos.topleft = c.SPACEBAR_LOC
    countdown_background.blit(sb, sb_pos)
    screen.blit(background, countdown_background.get_rect())
    pygame.display.update()
    wait()

    # ----------------------------------

    # INSERT COUNTDOWN HERE

    screen.blit(countdown_background, (0, 0))

    # Surface 4,5,6: Variation #1,2,3 ----------
    for i in range(3):
        player.new_variation()
        print(player.display_variations())

    # TODO: Implement music
    # pygame.mixer.music.load('foo.mp3')
    # pygame.mixer.music.play(0)
    # ----------------------------------

    # Final Event loop -----------------------
    while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_f:
                        print('[f] was pressed.\nSaving (not yet) data...')
                        # SAVE DATA HERE
                        pygame.quit()
                        print('Exiting program...')
                        sys.exit()
        pygame.display.update()
    # ----------------------------------

if __name__ == '__main__':
    main(sys.argv[1:])
