# Author: Eduardo Salinas

""" Final Project: Gold Standard - A video game made in Python

I will make “Gold Standard” (WORKING TITLE, it may be subject to change): a game inspired by Mother 2, which teaches
about economics.

For this project though, I will focus on just making the gameplay aspect of it. I won’t put the lore, nor story, nor
dialogues (if I don’t have the time).

I will make my game using Pygame.

I will use copyright free / royalty free music, images, and other assets.

To simplify things, I will put only 1 battle: a boss battle.

I’ll just focus on adding turn based combat, and that you need a strategy to win. Then, I will think about how to
implement mother 3’s musical combat into my game.

I will first just render a black screen when you execute the game.

I will simply imitate the “Press Start” or “Intro” screen from Clear Code’s 4-hour long pygame tutorial (source: Clear
Code on YouTube at  https://youtu.be/AY9MnQ4x3zk?si=mfCvPMEh2o7MNjM0 ). In that screen, there’s only text (like the
game’s name and the instructions), and the player’s sprite. That’s all that I need for the boss battle for the game
I want to make: the sprite of the enemy, and text, which will represent the player. I will look at the 4 hour long
tutorial, and just find out how to make the “Press Start / Intro” screen with the player sprite and the text. I will
later replace the player sprite with a red rectangle for the enemy, and I will later put all the text below the enemy
in a box to represent the player character.

I will use a 576p resolution to make a test for the game's window. The 576p resolution has 720 x 576 px as dimensions
(source: Wikipedia at https://en.wikipedia.org/wiki/Display_resolution).

Now, I need to render text (which indicates the player’s remaining HP, the player’s name) at the bottom of the screen.
The text needs to be centered.

Then, I could put a white box on the background of the player’s “box” that has their HP and name. I could either put a
white box, then a black box within it, and put white text inside the white box to make it readable.

I want to imitate either Earthbound beginnings or Dragon Quest 3’s UI for the battle screen, to make it look retro.
That’s why I want to use a black backgrouns, white boxes with black boxes within them, and then white text inside.

Or, I could also render a red rectangle, which will represent the enemy (the boss). I could either create my own
placeholder sprite (since I want to use a royalty-free sprite for the enemy later on), or just render a red rectangle
using Pygame. Given that I want to replace the red rectangle placeholder for a royalty free sprite, I think it’s best
that I use a red rectangle sprite.

Since the game will graphically look similar to Earthbound Beginnings or Dragon Quest 3, I will put the battle menu UI
above the enemy. The HP and the name of the player will be below the enemy. That way, it will look a bit different than
Earthbound Beginnings or Dragon Quest 3.

This part of Clear Code’s 4-hour long Pygame tutorial explain how to import a sprite into pygame:
https://youtu.be/AY9MnQ4x3zk?si=3JoYUoGl800VV2dq&t=2645 . Note that it would be better if I use a "rectangle" to
render each sprite. Normally, I need to load a sprite by using a "surface". Well, rendering surfaces directly isn't
a good idea. To better manipulate the position of each sprite (such as by using keywords such as "bottom", and "top"),
it's a good idea to transform the surface into a rectangle, and THEN render the rectangle to render the sprite
(source: https://youtu.be/AY9MnQ4x3zk?si=PXioHwUA3M8AuL7S) .

Now, I need to render the enemy as a rectangle, NOT AS A SURFACE.

Then, I will need to re-position the enemy to the center of the screen (such as by using “top”, and then dividing by 2
the width of the game’s window, which in this case would be 720 / 2).

REMEMBER THAT I NEED TO USE AT LEAST 3 FUNCTIONS to pass this final project! Look at Clear Code’s 4-hour long tutorial,
since he made some functions towards the last 3rd of the video.

ALSO remember that I need to create some unit tests to test my game to pass the final project!

"""

import pygame

from sys import exit  # If I want to exit the game properly, I'll use sys.exit()

# All of this code should make it so that a black screen shows up when you execute this python script (source:
# https://youtu.be/AY9MnQ4x3zk?si=28DorTag9IRSrUi3&t=1099).
pygame.init()

# This will render any screen / window, be it the battle screen, the press start screen, etc
game_window = pygame.display.set_mode((720, 576))

# This will add the game's title to the window's tab
pygame.display.set_caption("Gold Standard")

# Sprites
# This loads the enemy sprite, but doesn't render it yet (source:
# https://youtu.be/AY9MnQ4x3zk?si=2sgfMIq-zyCv-eHx&t=2645).
# EDIT LATER, since it's using a PLACEHOLDER sprite.
enemy_surface = pygame.image.load('assets/images/sprites/red-rectangle-enemy-placeholder.png')


while True:  # Infinite loop that will pretty much make the entire game run

    # For any input taken by the user (such as clicking the mouse or closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks "X" on the window's tab to close the game

            # This will efficiently close the game
            pygame.quit()
            exit()

    # If no input is detected by the user (if they don't click nor press any keys), this will execute

    # This renders the sprites

    # This renders the enemy's sprite.
    # I NEED TO FIX THE POSITION LATER, AND use a "rectangle" instead of rendering the "surface".
    game_window.blit(enemy_surface, (100, 100))

    # This should render the game's window, and every sprite
    pygame.display.update()

# End of the snippet that renders a black screen once you execute a pygame game (source:
# https://youtu.be/AY9MnQ4x3zk?si=28DorTag9IRSrUi3&t=1099)
