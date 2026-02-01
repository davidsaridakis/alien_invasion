import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')  # Returns a surface representing the ship
        self.rect = self.image.get_rect()  # Access the surface's rect attribute (for the ship)
        self.screen_rect = screen.get_rect()  # Access the rect attribute for the screen surface

        # Start each new ship at the bottom centre of the screen.
        self.rect.centerx = self.screen_rect.centerx  # Match the x-coord of the ship with the x-coord of the screen
        self.rect.bottom = self.screen_rect.bottom  # Align the bottom of the ship rect to the bottom of the screen

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # If the moving_right flag is set to True
            # (via a held right arrow keypress) and the ships right edge is not at the right edge of the screen.
            self.center += self.ai_settings.ship_speed_factor  # Increase the position of the ship x coord by 1.
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx


