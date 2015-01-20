import pygame
import themeloader

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

    def update(self):
        self.rect.y += themeloader.block_size

class BlackBomb(Bomb):
    """
    Class for regular black bombs that go boom!
    """

    def __init__(self, image_handle):

        # Pass the image_handle into parent's __init__
        super().__init__(image_handle)

        self.does_explode = True
        self.does_score = True