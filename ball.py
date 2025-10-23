import pygame
import settings

pygame.init()

vec = pygame.math.Vector2 # 2 for two dimensional
# vec is creating vectors

class Ball:
    """Class for the ball the player controls"""

    def __init__(self):
        """Initialize ball and its attributes"""
        self.image = pygame.transform.scale(pygame.image.load("images/SoccerBall.png"), settings.BALL_SIZE)
        self.rect = self.image.get_rect()

        self.center()
        # # Initialize rotation angle (if needed)
        # self.angle = 0


        self.is_jump = False
        self.jump_count = 0

    def move_ball(self, keys):
        """Move the ball according to user input"""
        # Code for ball movement is from an online tutorial (https://coderslegacy.com/python/pygame-platformer-game-development/)
        self.acc = vec(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= settings.ball_y_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.acc.x = -settings.ACC
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.acc.x = settings.ACC
            
        self.acc.x += self.vel.x * settings.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Prevent ball from moving off-screen
        if self.rect.right > settings.SCREEN_WIDTH:
            self.pos -= self.vel + 0.5 * self.acc
            self.pos.x -= 1
        elif self.rect.left < 0:
            self.pos -= self.vel + 0.5 * self.acc
            self.pos.x += 1

        self.rect.midbottom = self.pos

    def jump(self):
        # jump_count is initially 22
        if self.is_jump:
            self.pos.y -= self.jump_count
            self.rect.midbottom = self.pos
            
            if self.jump_count > -settings.jump_max: # while count is bigger than -22
                self.jump_count -= 1
            else:
                self.is_jump = False
    
    def center(self):
        """
        Position ball on the center of the screen and
        Initialize movement vectors
        """
        self.pos = vec(settings.BALL_ORIGINAL_POSITION) # vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)