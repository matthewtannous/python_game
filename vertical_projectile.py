import settings

import pygame
import random

pygame.init()

class VerticalProjectile(pygame.sprite.Sprite):
    """Class for vertial projectiles that player must avoid"""

    def __init__(self):
        """
        Initialize attributes for projectiles that fall from the top of the screen
        """

        super().__init__()

        self.set_initial_speed()
        self.image = pygame.surface.Surface(settings.vertical_projectile_size)
        self.image.fill("red")
        self.rect = self.image.get_rect()

        self.reposition()

    def update(self):
        """move the projectile"""
        self.rect.y += self.speed

    def check_if_on_screen(self):
        """
        Check if projectile is below the screen.
        if it is, put it back at the top with increased speed
        """
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.speed += (random.random() / 2 + 0.3)
            self.reposition()
            return True
        return False
    
    def reposition(self):
        """Put projectile on top of screen"""
        self.rect.midbottom = (random.randint(10, settings.SCREEN_WIDTH - 10), 0)
    
    def set_initial_speed(self):
        """Set initial speed for projectile"""
        self.speed = settings.vertical_projectile_speed