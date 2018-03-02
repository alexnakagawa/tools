try:
    import pygame
    import sys
    import random
    import math
    import os
    import time
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
    pygame.mouse.set_visible(False)
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
    pygame.time.wait(100)
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

    pygame.time.wait(100)

    sb = create_text("Press the [spacebar] to continue", c.PREF_FONTS, 16, c.RED)
    sb_pos = sb.get_rect()
    sb_pos.topleft = c.SPACEBAR_LOC
    background.blit(sb, sb_pos)
    screen.blit(background, screen.get_rect())
    pygame.display.update()
    wait()
    # ----------------------------------

    # Surface 3: Ready Screen -------------
    countdown_background = pygame.Surface(screen.get_size())
    countdown_background = countdown_background.convert()
    countdown_background.fill(c.WHITE)

    get_ready = create_text("Get Ready...", c.PREF_FONTS, 24, c.BLACK)
    get_ready_pos = get_ready.get_rect()
    get_ready_pos.centerx = countdown_background.get_rect().centerx
    get_ready_pos.centery = countdown_background.get_rect().centery - 100
    countdown_background.blit(get_ready, get_ready_pos)
    screen.blit(countdown_background, countdown_background.get_rect())
    pygame.display.update()
    pygame.time.wait(1000)

    sb = create_text("Press the [spacebar] when you are ready", c.PREF_FONTS, 16, c.RED)
    sb_pos = sb.get_rect()
    sb_pos.topleft = c.SPACEBAR_LOC
    countdown_background.blit(sb, sb_pos)
    screen.blit(countdown_background, screen.get_rect())
    pygame.display.update()
    wait()

    start = create_text("START", c.PREF_FONTS, 50, c.GREEN)
    start_pos = start.get_rect()
    start_pos.centerx = countdown_background.get_rect().centerx
    start_pos.centery = countdown_background.get_rect().centery + 100
    countdown_background.blit(start, start_pos)
    screen.blit(countdown_background, countdown_background.get_rect())
    pygame.display.update()

    pygame.time.wait(500)
    # Surface 4,5,6: Variation #1,2,3 ----------
    clean_background = pygame.Surface(screen.get_size())
    clean_background = clean_background.convert()
    clean_background.fill(c.WHITE)

    for i in range(1, 4):
        var_text = create_text('Variation %d' % i, c.PREF_FONTS, 32, c.BLACK)
        var_text_pos = var_text.get_rect()
        var_text_pos.centerx = clean_background.get_rect().centerx
        clean_background.blit(var_text, var_text_pos)
        screen.blit(clean_background, clean_background.get_rect())
        sb = create_text("Press the [spacebar] when you are ready", c.PREF_FONTS, 16, c.RED)
        sb_pos = sb.get_rect()
        sb_pos.topleft = c.SPACEBAR_LOC
        clean_background.blit(sb, sb_pos)
        screen.blit(clean_background, screen.get_rect())
        pygame.display.update()

        wait()

        clean_background.fill(c.WHITE)
        screen.blit(clean_background, screen.get_rect())
        pygame.display.update()
        player.new_variation()
        current_var = player.variations[i]
        current_var_attributes = current_var.get_attributes()
        # TODO: MUSIC
        # pygame.mixer.music.load(current_var_attributes[2])
        # pygame.mixer.music.play()
        clock = pygame.time.Clock()
        for j in range(1, 6):
            current_var.new_trial()
            current_trial = current_var.trials[j]
            delay_time = random.randrange(1000, 5000)
            x_pos, y_pos = random.randrange(35, clean_background.get_width() - 35),\
                           random.randrange(35, clean_background.get_height() - 35)

            current_trial.set_delay_time(delay_time)
            current_trial.set_x_pos(x_pos)
            current_trial.set_y_pos(y_pos)
            # Trials --------------------------
            pygame.time.wait(delay_time)
            clock.tick()
            if current_var_attributes[0] == 1:
                pygame.draw.circle(clean_background, c.COLOR_DICT[current_var_attributes[1]], (x_pos, y_pos), 20)
            elif current_var_attributes[0] == 2:
                pygame.draw.rect(clean_background, c.COLOR_DICT[current_var_attributes[1]], Rect(x_pos, y_pos, 35, 35))
            else:
                raise ValueError('Something is wrong...')
            screen.blit(clean_background, screen.get_rect())
            pygame.display.update()
            wait()
            clock.tick()
            current_trial.set_reaction_time(clock.get_time())
            clean_background.fill(c.WHITE)
            screen.blit(clean_background, screen.get_rect())
            pygame.display.update()
        # pygame.mixer.music.stop()
            # ---------------------------------
    # ----------------------------------

    end_screen = pygame.Surface(screen.get_size())
    end_screen = end_screen.convert()
    end_screen.fill(c.WHITE)

    concludes = create_text('This concludes the test.', c.PREF_FONTS, 24, c.BLACK)
    concludes_pos = concludes.get_rect()
    concludes_pos.centerx = end_screen.get_rect().centerx
    concludes_pos.centery = end_screen.get_rect().centery - 80
    end_screen.blit(concludes, concludes_pos)

    f_query = create_text("To save the data, please press 'f'.", c.PREF_FONTS, 24, c.BLACK)
    f_query_pos = f_query.get_rect()
    f_query_pos.centerx = end_screen.get_rect().centerx
    f_query_pos.centery = end_screen.get_rect().centery
    end_screen.blit(f_query, f_query_pos)

    esc_query = create_text("To delete the data, please press 'esc'.", c.PREF_FONTS, 24, c.BLACK)
    esc_query_pos = esc_query.get_rect()
    esc_query_pos.centerx = end_screen.get_rect().centerx
    esc_query_pos.centery = end_screen.get_rect().centery + 80
    end_screen.blit(esc_query, esc_query_pos)

    screen.blit(end_screen, screen.get_rect())
    pygame.display.update()

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
