# screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

framerate = 60

# Ball settings
BALL_SIZE = (90, 90)

# Original position
BALL_ORIGINAL_X = SCREEN_WIDTH // 2 - 10
BALL_ORIGINAL_Y = SCREEN_HEIGHT - 65
BALL_ORIGINAL_POSITION = (BALL_ORIGINAL_X, BALL_ORIGINAL_Y)

# horizontal movement
ACC = 1
FRIC = -0.12

# Vertical movement (jumping)
jump_max  = 22


# Vertical projectile settings
vertical_projectile_number = 4
vertical_projectile_speed = 5
vertical_projectile_size = (20, 50)

# Horizontal projectile settings
horizontal_projectile_number = 1
horizontal_projectile_speed = 3
horizontal_projectile_size = (50, 20)

# Score settings
SCORE_POSITION = (SCREEN_WIDTH // 2 - 65, 20)
HIGHSCORE_POSITION = (20, 20)

HIGHSCORE_FILE = "highscore.txt"

# Button settings
button_left = SCREEN_WIDTH // 2 - 200
button_top = SCREEN_HEIGHT // 2 - 45
button_width = 440
button_height = 100