import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()  # This is Python 2.7 syntax. super().__init__() works fine.
        """Initialize the attributes specific to the child class."""
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # Create rect attribute for
        # the bullet. Creating a rect needs (x,y) coordinates, a height and a width.
        self.rect.centerx = ship.rect.centerx  # Match the centre of the bullet rect with the centre of the ship rect.
        self.rect.top = ship.rect.top  # Match the top of the bullet rect with the top of the ship rect

        # Store the bullet's y-coordinate position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color  # Set the color (pulled from Settings)
        self.speed_factor = ai_settings.bullet_speed_factor  # Set the speed (pulled from Settings)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

