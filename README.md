# ROLL BALL
#### Video Demo: https://youtu.be/qKdlFxm91wo
#### Description:

##### Overview:
Roll Ball is a game made with Python using the pygame library.
In the game, the player controls a ball and must move left and right (with the left and right arrow keys), as well as jump (with the space key) to avoid projectiles coming from the top or from the side.
The player can leave the game by pressing q, the escape key or by clicking the 'X' button on the top right of the game window.
The project consists of 6 python files, as well as a text file to store the highscore.


##### settings.py
This file only contains constants used in other files, so that changing any aspect of the game, such as speed or colors, becomes easier.

##### ball.py
This file contains the class Ball which is used to model the ball that the player controls.
The image for the ball is from google images, and pygame's scale() method is used to reduce the size of the ball to fit nicely on the screen.
Then a Rect object is created from the image and placed on the bottom center of the screen using the center() method.
Initially, the code for moving the ball left and right was much simpler as it was simply adding or subtracting from the ball rect's x value, but I then decided to use the code of an online tutorial that made the ball movement smoother.
The code for the jump mechanic is from Stack Overflow.

##### vertical_projectile.py
This file contains the class VerticalProjectile which is used to model a projectile that appears at the top of the screen and moves downwards at a constant speed.
A projectile is created by using the information in settings.py, and positioned at a random position at the top of the screen using the reposition() method.
This method sets the projectiles x value to a random integer (using python's random module) that is between 10 and the total screen width - 10, so that it always appears on the screen. The y value is always 0 initially, so that the projectile is on top of the screen.
The class also contains the methods update() to change the projectile's position, set_initial_speed() that sets the projectile's starting speed, and check_if_on_screen(), which checks if it has left the screen and, if it has, repositions it and increases its speed.

##### horizontal_projectile.py
This file contains the class HorizontalProjectile which is used to model a projectile that appears on the lower right side of the screen and moves to the left at a constant speed.
A horizontal projectile has the same functionality of a vertical projectile, and the same methods.

##### button.py
This file contains the class Button which is used to model a button that appears on the screen when the player has lost the game.
A button is created by providing a string message, and the class surrounds it with a background and displays it on the screen using the draw method, which takes a screen as argument.
By default, the button is displayed at the center of the screen.

##### main.py
This is the main file of the project, which contains the class Main used to create and run a game.
The class begins by defining one instance of most game elements needed (ball, screen, button), a background image (from google images) and many projectiles, grouped together in a pygame Group object. It also starts a timer and creates a font to display the current survived time and the highscore.

The highscore is obtained and saved to a text file, *highscore.txt*. If an error occurs while reading the highscore, it is automatically set to 0. The highscore is always saved, even if the player exits in the middle of a running game.

The game's main loop updates the projectiles' position, check for player input, collisions and updates the screen at a rate of 60 fps.
The time is obtained by setting the start_time to the time a game begins (using time.time()) and subtracting it from the current time at each pass through the loop. Then the obtained float value is converted to a string, which is then converted to a surface using the pre-defined font at the start. A similar approach is used for the highscore, and both are displayed at the top of screen.

If the player collides with ANY projectile, the game ends, and a button appears asking the player if they would like to play again. If they do, projectile speeds and survivied time are reset to their original values and the game starts.

Outside the class, at the end of the file, an instance of the game is created and its run_game() method is called, starting a game.

##### highscore.txt
Text file used to store the highscore of the game. It will be recreated if the old one is deleted, or if it contains invalid information.

##### requirements.txt

Text file stating all requirements to run the project (besides python). Only pygame is needed.
