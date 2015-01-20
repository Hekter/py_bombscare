import pygame
import os

class Player(pygame.sprite.Sprite):
    """
    The class for the player! Weee.
    """
    def __init__(self, image_handle):

        super().__init__()

        # Set self.image to the passed-in image handle.
        self.image = image_handle

        # Maor hitbox(?)
        self.rect = self.image.get_rect()