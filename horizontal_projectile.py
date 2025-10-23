import settings

import pygame
import random

pygame.init()

class HorizontalProjectile(pygame.sprite.Sprite):
    """Class for vertial projectiles that player must avoid"""

    def __init__(self):
        """
        Initialize attributes for projectiles that move from left to right
        """

        super().__init__()

        self.set_initial_speed()
        self.image = pygame.surface.Surface(settings.horizontal_projectile_size)
        self.image.fill("yellow")
        self.rect = self.image.get_rect()

        self.reposition()

    def update(self):
        """move the projectile"""
        self.rect.x -= self.speed

    def check_if_on_screen(self): #TODO
        """
        Check if projectile is at the left of the screen.
        if it is, put it back at the right with increased speed
        """
        if self.rect.right < 0:
            self.speed += (random.random() / 2 + 1)
            self.reposition()
            return True
        return False
    
    def reposition(self):
        """Put projectile on left side of the screen"""
        self.rect.midleft = (settings.SCREEN_WIDTH ,random.randint(int(settings.SCREEN_HEIGHT * 0.66), settings.SCREEN_HEIGHT - 30))

    def set_initial_speed(self):
        """Set initial speed for projectile"""
        self.speed = settings.horizontal_projectile_speed