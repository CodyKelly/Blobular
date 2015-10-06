import pygame
from data.blob import Blob
from math import pow


class MoveBlob(Blob):
    # This class is based on the Blob class, and it can:
    # - move
    # - eat other blobs
    # - grow/shrink
    # - split

    def __init__(self, level_rect):
        Blob.__init__(self, level_rect)

        self.mass = 20

        self.speed = self.calc_speed()  # Calculate initial speed

    def update(self, keys, events, joysticks):

        self.calc_speed()

        if joysticks:
            self.joystick_move(joysticks)
            self.change_mass(joysticks)
        else:
            self.move(keys)

        self.pos = (int(self.x), int(self.y))

    def move(self, keys):
        # Moves the blob based on keyboard input
        # Used when no controller is available

        # Move up
        if keys[pygame.K_UP]:
            self.y -= self.speed

        # Move down
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Move left
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        # Move right
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def joystick_move(self, joysticks):
        # Moves the blob based on input from joysticks

        joyThresh = .3  # Joystick threshold, will not move if inputs from joystick are less than this
                        # This prevents unwanted movement based on small inputs

        jX = joysticks[0].get_axis(0)   # X-Axis input
        jY = joysticks[0].get_axis(1)   # Y-Axis input

        # Process input
        if jX > joyThresh or jX < -joyThresh:
            self.x += self.speed * joysticks[0].get_axis(0)
        if jY > joyThresh or jY < -joyThresh:
            self.y += self.speed * joysticks[0].get_axis(1)

    def change_mass(self, joysticks):
        j_y = joysticks[0].get_axis(4)
        self.mass += int(j_y + 0.1)

    def calc_speed(self):
        # Speed is calculated with an exponential formula based on its mass
        return pow(.8, self.mass / 2 - 20) + 1
