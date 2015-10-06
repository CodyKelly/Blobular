import pygame
import random
import math
import pygame.gfxdraw


def get_random_color():
    # Returns a random rgb value
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


class Blob:
    # A small, simple blob. Can be absorbed by other blobs for its mass

    def __init__(self, level_rect):
        # Find a random position within the bounds of the level
        # X and Y values can be integers or floats, it doesn't matter
        # because they'll be converted to integers in the draw method
        self.x = random.randint(0, level_rect.width)
        self.y = random.randint(0, level_rect.height)

        self.pos = (int(self.x), int(self.y))   # The position should always be a tuple of integers

        self.mass = 5   # Only 5 mass, it's pretty small

        self.color = get_random_color()  # Get a random color for this blob

    def draw(self, screen):
        # Draws the blob to the screen
        # Pygame doesn't support anti-aliased filled circles, so there are two steps to this method

        # First we draw an anti-aliased circle:
        pygame.gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.mass, self.color)

        # Then we draw a filled circle within the first circle:
        pygame.gfxdraw.filled_circle(screen, self.pos[0], self.pos[1], self.mass, self.color)
