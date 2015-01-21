import pygame
import themeloader
import random

class Bomb(pygame.sprite.Sprite):
    """
    Base class of a boooomb!
    """

    def __init__(self, image_handle):

        # Initialize the parent(super) class before we do anything.
        super().__init__()

        # Create a reference to the sprite in memory.
        self.image = image_handle

        # Get the hitbox(?)
        self.rect = self.image.get_rect()

    # Resets the position to a random x and y above the board, determined by the theme blocksize.
    def reset_position(self):
        self.rect.x = random.randrange(0, themeloader.SCREEN_WIDTH_BLOCKS) * themeloader.block_size
        self.rect.y = random.randrange(-(themeloader.block_size * 5), 0, 16)

    def update(self):
        self.rect.y += themeloader.block_size

        if self.rect.y > (themeloader.block_size * 12):
            # self.rect.y = -16
            self.reset_position()

class BlackBomb(Bomb):
    """
    Class for regular black bombs that go boom!
    """

    def __init__(self, image_handle):

        # Pass the image_handle into parent's __init__
        super().__init__(image_handle)

        self.does_explode = True
        self.does_score = True

class RedBomb(Bomb):
    """
    Class for the red, screen-clearing bomb!
    """

    def __init__(self, image_handle):
        super().__init__(image_handle)

        self.does_explode = False
        self.type = "Red"
        self.does_score = False