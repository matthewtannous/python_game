"""Main file of project"""
import time
import sys

import pygame

import settings
from ball import Ball
from vertical_projectile import VerticalProjectile
from horizontal_projectile import HorizontalProjectile
from button import Button
# pygame setup
pygame.init()

class Main:
    """Overall class for the game"""

    def __init__(self):
        """Initialize game attributes"""

        # Initialize ball
        self.ball = Ball()

        # Initialize screen
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE) # self.screen is a Surface
        pygame.display.set_caption("Roll Ball") # sets the caption on top of the game window
        pygame.display.set_icon(self.ball.image) # sets the icon on top of the game window
        self.background = pygame.transform.scale(pygame.image.load("images/background.jpg"),
                                                  (settings.SCREEN_WIDTH + 30, settings.SCREEN_HEIGHT + 30))

        # Initialize projectiles

        self.projectiles = pygame.sprite.Group() # Group for both vertical and horizontal projectiles

        for _ in range(settings.vertical_projectile_number):
            self.projectiles.add(VerticalProjectile())

        for _ in range(settings.horizontal_projectile_number):
            self.projectiles.add(HorizontalProjectile())
        
        # Start a game immediately after running
        self.running = True
        pygame.mouse.set_visible(False)

        # Initialize clock and time
        self.clock = pygame.time.Clock()
        
        # Initialize font for displaying time on screen
        self.font = pygame.font.Font(size=60)
        self.start_time = time.time()

        self.highscore = self.get_highscore()

        # Initialize play again button
        self.play_again_button = Button("Press ENTER or click here to play again")

    def get_highscore(self):
        """Read highscore from file or start at zero"""
        try:
            with open(settings.HIGHSCORE_FILE) as file:
                try:
                    return float(file.read())
                except ValueError:
                    return 0
        except FileNotFoundError:
            return 0

    def run_game(self):
        """Main game loop"""
        while True:
            self.check_events()
            if self.running:
                self.projectiles.update()
                self.check_projectiles()
                self.check_collisions()
                self.update_time()

            self.update_screen()       
            self.clock.tick(settings.framerate)


    def check_events(self):
        """Checks for user input"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # Exit button on top right
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.ball.is_jump: 
                        # Start a jump
                        # Code for jumping is from stack overflow
                        self.ball.is_jump = True
                        self.ball.jump_count = settings.jump_max
                    if event.key == pygame.K_q: # Quit
                        self.quit()
                    if event.key == pygame.K_RETURN and self.running == False:
                        self.reset_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_pressed = self.play_again_button.rect.collidepoint(pygame.mouse.get_pos())
                    if button_pressed and not self.running:
                        self.reset_game()

        self.ball.jump()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            self.quit()

        # Move the ball only when the game is still going
        if self.running:
            self.ball.move_ball(keys)

    def quit(self):
        """Save highscore and exit the game"""
        
        with open(settings.HIGHSCORE_FILE, 'w') as file:
            file.write(self.string_highscore)
        sys.exit()

    def reset_game(self):
        """Reset game attributes before starting a new game"""
        # Put projectiles at starting positions
        for projectile in self.projectiles:
            projectile.set_initial_speed()
            projectile.reposition()
        # Center ball
        self.ball.center()
        # Reset time
        self.start_time = time.time()
        # Make mouse invisible
        pygame.mouse.set_visible(False)
        # Start new game
        self.running = True


    def check_projectiles(self):
        """Check if any projectile is below the screen"""
        for projectile in self.projectiles:
            projectile.check_if_on_screen()
    

    def check_collisions(self):
        """Check if player hit a projectile"""
        # collisions is the projectile that collided
        collisions = pygame.sprite.spritecollideany(self.ball, self.projectiles)
        if collisions:
            # Player lost
            self.running = False
            pygame.mouse.set_visible(True)


    def update_time(self):
        """Update survived time"""
        cur_time = time.time() - self.start_time
        self.string_time = "{:.2f}".format(cur_time)

        # Update highscore if reached
        if cur_time > self.highscore:
            self.highscore = cur_time

        self.string_highscore = "{:.2f}".format(self.highscore)

        self.surface_time = self.font.render(self.string_time, False, "black", None)
        self.surface_highscore = self.font.render(self.string_highscore, False, "black", None)
        
    

    def update_screen(self):
        """Make changes to the screen"""
        #self.screen.fill("blue")
        self.screen.blit(self.background, (0, 0))

        # draw the ball
        self.screen.blit(self.ball.image, self.ball.rect) # blit is used to draw a Rect on a Surface
        
        # draw the projectiles
        self.projectiles.draw(self.screen)

        # display time
        self.screen.blit(self.surface_time, settings.SCORE_POSITION)

        # display highscore
        self.screen.blit(self.surface_highscore, settings.HIGHSCORE_POSITION)

        # display play again button if the game is not running
        if not self.running:
            self.play_again_button.draw(self.screen)

        # flip() to display work on the screen
        pygame.display.flip()


if __name__ == "__main__":
    # Start a game instance and run the game
    game = Main()
    game.run_game()