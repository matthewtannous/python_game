import pygame
import settings

pygame.init()

class Button:
    """Class to model a pressable button"""

    def __init__(self, message):
        """Initialize button attributes"""
        self.font = pygame.font.Font(size=30)
        self.set_message(message)        

        self.background_surface = pygame.surface.Surface((settings.button_width, settings.button_height))

        self.background_surface.fill((60,60,60))

        self.rect = pygame.rect.Rect(settings.button_left, settings.button_top,
                                                 settings.button_width, settings.button_height)

    def set_message(self, message):
        """Change the button's displayed message"""
        self.message = message
        self.text_surface = self.font.render(message, True, "purple")

    def draw(self, screen):
        """Draw button to the screen"""
        screen.blit(self.background_surface, self.rect)
        screen.blit(self.text_surface,
                (settings.SCREEN_WIDTH // 2 - 170, settings.SCREEN_HEIGHT // 2))
        