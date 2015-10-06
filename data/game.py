import pygame
from sys import exit as sys_exit
from data import moveblob
from data import blob

WHITE = (255, 255, 255)


def run():

    pygame.init()

    windowRect = pygame.Rect((0, 0), (1440, 900))

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Main game surface

    clock = pygame.time.Clock()  # Clock to regulate FPS

    caption = 'Blobular'  # Window caption

    pygame.display.set_caption(caption)  # Set the caption

    bob = moveblob.MoveBlob(windowRect)  # Test blob

    num_of_players = 1

    # Create and initialize joysticks
    joysticks = []  # List to hold joystick objects

    pygame.mouse.set_visible(False)

    for x in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(x))  # Append new joystick object to joysticks with ID of x
        joysticks[x].init()  # Initialize newly created joystick object

    while True:
        clock.tick(60)  # Cap game to 60 fps
        screen.fill(WHITE)  # Fill screen with white

        events = pygame.event.get()      # Holds a list of pygame events
        keys = pygame.key.get_pressed()  # Holds a list of keys being held down

        # If there's a QUIT event, quit Pygame and exit program
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys_exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys_exit()

        bob.update(keys, events, joysticks)

        bob.draw(screen)

        pygame.display.flip()
