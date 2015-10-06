import pygame

WHITE = (255, 255, 255)


class Arena:
    # This maintains game arena, draws the grid and has all game objects drawn onto it
    def __init__(self, size):
        self.size = size  # Size of the arena, in pixels
        self.surface = pygame.Surface((size, size))  # Surface to draw grid and any blobs in game onto
        self.numGridLines = 500  # Number of grid lines from top to bottom and left to right

    def update(self):
        self.surface.fill(WHITE)
        self.draw_grid()

    def draw(self, screen):
        pass

    def scale(self, amount):
        # Scales the surface by a certain amount
        pass

    def draw_grid(self):
        # Draws grid on surface
        for x in range(0, self.numGridLines):
            pygame.draw.line()

    def get_draw_area(self, objects):
        # Returns a surface taken from self.surface, only showing what is needed (area around players)
        pass
