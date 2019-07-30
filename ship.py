import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen.screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_left = False
        self.moving_right = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value.
        if self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.centerx < self.screen_rect.width:
            self.center += self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
