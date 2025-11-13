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

Now, I need to render the enemy as a rectangle, NOT AS A SURFACE. To convert a surface into a rectangle, I need
to use get_rect() (source: Clear Code on YouTube at https://youtu.be/AY9MnQ4x3zk?si=aWRIhi1cXXQjBg8O&t=3360).

The enemy will be either at “midtop” or at the “center” (source of the rectangle’s different values and what they do:
https://youtu.be/AY9MnQ4x3zk?si=MsnmA5-iJE5U5uHq&t=3205 ). I want to use a tuple as a value for the location of the
enemy sprite.

Then, I will need to re-position the enemy to the center of the screen (such as by using “top”, and then dividing by 2
the width of the game’s window, which in this case would be 720 / 2). If I want to place the enemy's sprite on both
the vertical and the horizontal center off the screen, I would have to divide 720 by 2, and 576 by 2. That would be
360 and 288, respectively.

REMEMBER THAT I NEED TO USE AT LEAST 3 FUNCTIONS to pass this final project! Look at Clear Code’s 4-hour long tutorial,
since he made some functions towards the last 3rd of the video.

ALSO remember that I need to create some unit tests to test my game to pass the final project!

I will add a convert() call after loading every sprite as a surface to load the sprites as efficiently and optimized
as possible in the game. Also, if I use PNG files, which will have a transparent background, I need to use
"convert_alpha", NOT "convert" alone (source: https://youtu.be/AY9MnQ4x3zk?si=NkKrtiIpKEUUDDvg&t=3256).

“Pygame comes with a builtin default font, freesansbold. This can always be accessed by passing None as the font
name.” (Source: Pygame’s official documentation at https://www.pygame.org/docs/ref/font.html ). So yeah, pygame already
has a default font. I don’t need to install any fonts to print text in pygame.

To make things simpler, and to not to move the camera like in Earthbound Beginnings’ combat, I will put both the battle
messages (“you have done 20 points of damage to the boss”; “the boss hit you for 30 points of damage”) and the battle
menu at the top of the screen, right above the boss. The only text that will be below the boss will be the name of the
main character and his HP points. So, now I’m going to render white text that says “Midas / Aurelius / Ludwig”, and
his HP points (for instance, “HP: 100/100”). I will render this text right below the enemy. To add a font, even if
it's Pygame's default font, I need to use "pygame.font.Font(font_name, font_size)" (source: Clear Code at
https://youtu.be/AY9MnQ4x3zk?si=wipQ0_t-8tPlMym9&t=2331). For the surface of the text that I will render, I will
specify the message to be rendered (i.e: the name of the playable character), if it has Anti Aliasing (not recommended
if I'll use pixel art-based text), and the text's color. Now, I will render the main character’s HP points. I could at
first render the HP as being hard-coded, that is, I will type the HP will always be 100/100. I will later fix that
so that your HP points go down each  time that the enemy hurts you. I’m already storing the Player’s current HP in a
different variable, so that, if I get hurt, my HP will go down in the UI (since I’m using Python’s formatted strings).

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

# This specifies the font that I will use, and its size. At least, I will use this for the playable character's name.
game_font = pygame.font.Font(None, 35)

players_current_hp = 55    # This stores the current HP for the player. This goes down if the enemy hurts you.

# Sprites and surface
# This loads the enemy sprite, but doesn't render it yet (source:
# https://youtu.be/AY9MnQ4x3zk?si=2sgfMIq-zyCv-eHx&t=2645).
# EDIT LATER, since I'm using a PLACEHOLDER sprite.
enemy_surface = pygame.image.load('assets/images/sprites/red-rectangle-enemy-placeholder.png').convert_alpha()

# This creates a rectangle for the enemy sprite's surface. I will place it around the center of the screen.
enemy_rectangle = enemy_surface.get_rect(center=(360, 288))

# Text surfaces.
# Surface for the Playable Character's name
playable_characters_name_surface = game_font.render('Midas', False, 'White')

# Surface for the Playable Character's HP (Hit Points / life points)
players_hp_surface = game_font.render(f'HP: {players_current_hp}/100', False, 'White')

# End of text surfaces

while True:  # Infinite loop that will pretty much make the entire game run

    # For any input taken by the user (such as clicking the mouse or closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks "X" on the window's tab to close the game

            # This will efficiently close the game
            pygame.quit()
            exit()

    # If no input is detected by the user (if they don't click nor press any keys), this will execute

    # This renders the sprites

    # This renders the enemy's sprite. The position will be rendered with a rectangle.
    game_window.blit(enemy_surface, enemy_rectangle)

    # This render's the playable character's name. It should be in the horizontal center, and below the enemy.
    game_window.blit(playable_characters_name_surface, (320, 400))

    # Player's current HP
    game_window.blit(players_hp_surface, (320, 450))

    # This should render the game's window, and every sprite
    pygame.display.update()

# End of the snippet that renders a black screen once you execute a pygame game (source:
# https://youtu.be/AY9MnQ4x3zk?si=28DorTag9IRSrUi3&t=1099)
