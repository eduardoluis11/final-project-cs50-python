# Final Project: Gold Standard - A video game made in Python

# Author: Eduardo Salinas

""" ## Final Project: Gold Standard - A video game made in Python

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

I will add a rectangle to both the playable character’s name and his HP, and I will add it to their surfaces. That way,
I’ll be able to easily center them horizontally. And that way, I’ll be able to easily put the playable character’s data
inside a box. To whatever Y position the player's name has, I will add 40 units to the Y position of the player's HP.
That distance looks good. Now, I will add the black rectangle within the white rectangle for the box  that will contain
the player’s name and HP. REMEMBER that this box should be in a “layer” BEHIND the layer that contains the text with
the player’s stats. How to draw a rectangle: Clear Code at https://youtu.be/AY9MnQ4x3zk?si=8ZF9bckxd6UbMnYe&t=4811 .

To draw a rectangle, I needed to first use the draw() function from pygame (source: Pygame’s official documentation at
https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect ). Then, in the last parameter of draw.rect(), I needed to
pass either a Rect() game object (a rectangle game object from Pygame), or 4 parameters within parentheses: the the x
coordinate of the left side of the rectangle, the Y coordinate of the top of the rectangle, and the width and the
height of the rectangle (source: Pygame’s official documentation at https://www.pygame.org/docs/ref/rect.html ). If
I want to draw square, I would just put the width and the height as the same value while using draw.rect(). Now, I have
a black rectangle with a white border.

Now, I will add a new text at the top that says “A Hostile Robot Leader has ambushed you / has shown up!”, to indicate
that combat has begun for the boss battle.

To read through the dialogues and windows move (i.e: when the messages “a wild Hostile Robot Boss has shown up!”,
“the Hostile Robot has hit you for 10 HP of damage”), you will have to press “Z”, right shift, space, left mouse click,
etc. That is, you will have to press “Z” to read each combat dialogue message, just like in the Pokemon games. The
messages won’t go by automatically.

The battle messages should be in a variable, and the variable should be constantly updated. Otherwise, I would need to
constantly create new battle messages. I should have the following:
    A message for when the battle starts.
    A message for when the enemy hurts you.
    A message for when you hurt the enemy.
    A message for when you lose.
    A message for when you defeat the enemy.

And remember that the amounts in which the enemy will hurt you and you will hurt the enemy will be random like in the
Final Fantasy games (i.e: you make “20”, “30”, “22”, etc, of damage, instead of a fixed amount). For that, I won’t
create a different surface for each of those messages. Instead, I will store each message in a variable, and render the
variable when needed.

Also, since the battle menu and the battle messages will be rendered in the same Pygame rectangle, I will create only 1
rectangle that I will re-use for both the Battle Menu and the Battle messages. I will create multiple surfaces (1 for
the battle Menu, and 1 for the battle messages), but I will re-use the same Pygame rectangle.

I could create 2 functions: one for when the enemy attacks the user, and another one for when the user attacks the
enemy. Or it could be the same function.

And I could make a function for when you have to use the Battle Menu (for instance, for if you want to choose “attack”,
“defend”, or “use item”).

Since the number of turns really doesn’t matter for my game, I could simply put the default message / string in the
“battle messages” variable to be “an enemy has appeared!”. I will do that since that message will be rendered only in
the very first turn, and won’t be shown up ever again (unless the user returns to the “Press Start” screen after
winning or losing the battle). Now, I’ll insert the black box / rectangle inside the white box for the battle messages
UI.

Now, I need to add events so that, if the user presses any key (such as right shift, “z”, the space bar, a mouse click,
etc), you will go from the battle message to the Battle Menu UI to decide if you want to attack or do something else.

NOTE: I need 2 buttons: one to confirm, and another one to cancel. So, I could use the space bar or the right shift
button to confirm, and the Backspace to cancel. I can’t just put every keyboard key and every mouse click to confirm,
because, otherwise, it would be impossible for me to cancel any actions.

I have an idea: I could detect if the user has pressed either “Z” or right shift (which will be the confirmation
buttons). If they do, I will detect a boolean that detects if it’s the 1st turn or not. That boolean will start as
“True”. Then, if the user presses a confirmation button, that boolean will switch to “False”. Then, I will call a
function that will call the battle menu UI (so that you can select if you want to attack or defend). I will start with
the boolean thing that will switch from “True” to “False” if you press a confirmation button (I could print a debugging
message in the console). Done! I only turn the “display battle intro message” to “False” once, and only after pressing
the “Z” key on the keyboard.

I have an idea: to make the “an enemy has appeared!” message to disappear after pressing the “confirmation” key, I will
simply make an “if” statement saying that the “an enemy has appeared” message to only show up if the “display intro
message” boolean is True. That way, as soon as I press the confirmation key during the very first turn, that message
will disappear for the rest of the game.

So, I have another idea: I will decide whether to render the battle messages, or the battle menu’s UI. If the current
turn requires me to render the battle messages, I will render the battle messages. Otherwise, I will render the battle
menu. Now, to decide whether I should render the battle menu or the battle messages, I could use a boolean. I could
make a boolean that says “should battle menu be rendered” or something like that. By default, it will be false. But,
after pressing the confirmation key during the very first turn, the “should battle menu be rendered” boolean should
switch to “true”. Then, checking the “if” statements of my “while True” snippet, I should check if the “render battle
menu” boolean is set to true. If it is, I should render the battle menu. Otherwise, I should render the battle messages.

If I want to use object oriented programming, I could create a class with the properties for both the player and the
enemy. I could create a class called “Character”. In it, I would put at least 2 properties: attack points, and HP.
“Attack points” would be how much damage each character could do. Meanwhile, “hp” refers to how many life points each
character has (which, in this case, it's just the enemy and the player). This could help me keep my code organized
(using the “character class”). But I don’t know how to call those object oriented classes in my game. I need to have a
look at my object oriented programming classes’ homework assignments to remember how to use object oriented programming
(similar to django’s models).

I could make calls to two functions in the “while True” loop: one for the player’s turn, and another one for the
enemy’s turn. And each of those functions could make a call to a function called “battle_messages()”.
In fact:  during each iteration of the “while true” loop, I could call those 3 functions in the following order:
    display_battle_message()
    players_turn()
    display_battle_message()
    enemys_turn()

And in fact, the very first call to the “display battle message()” could render the “an enemy has appeared!” message.
I don’t need to use booleans. And remember that, since the “while true” loop is an infinite loop, that loop will always
be repeated over and over again. So, in each iteration of the infinite loop, I would first call the function that
displays battle messages, then it would be the player’s turn, then the battle messages would be displayed, and then it
would be the enemy’s turn. Then, the entire loop would be repeated. I could make it so that you would go from the
battle messages to the player’s or the enemy’s turn by pressing “Z”. So, during my very first call to the “display
battle messages()” function, I would display the default message in the “battle message” variable, which is “an enemy
has appeared!”. Well, after that first call, I would then go to the player’s turn via the “players turn()” function.
Well, in the player’s turn() function, I would overwrite the string inside the “battle message” variable for another
battle message (such as “ludwig did {amount of damage} points of damage!”). I don’t need to use any booleans. Then,
in the enemy’s turn, the entire turn would be invisible (it would be in the “backend”). The enemy would decide which
attack to use, or if they would prepare a super attack, or not do anything. But  nothing would be printed onscreen.
Then, after calling again the “display battle message()” function, I would print the enemy’s decision (i.e: “the enemy
has attacked you for {amount of damage} points of damage!”).

I would do the following:

1) I could print the “an enemy has appeared!” message. I could simply print whatever message is stored in the “battle
message” variable.

2) Then, it would be the player’s turn. I would need to make the battle message to disappear.

3) I would print the options for the battle menu. I DON’T have to ask the user to use the arrow keys to select an
attack. I could simply ask the user to press any number between 1 and 3 (“1” for attacking the enemy, “2” for
defending, “3” for selecting an item). That is, I could make the battle menu like in persona 5. This would be easier
to code. Detecting each individual option selected with the arrow keys would be hard to code.


3) After the player selects an option (by pressing “1”, “2”, or “3”), a battle message would be displayed indicating
what the player did (either stating how much damage you did to the enemy, if you healed, or if you guarded against the
next attack).

4) Then, it would be the enemy’s turn. The enemy would automatically decide what to do (attacking, wasting a turn, or
preparing for a super attack). Here, I could update the “battle message” variable to print whatever the enemy decided to do to you. To update the “battle message” variable, I could call a function, and said function should return a string. That string would be the new value for the “battle message” variable.

5) A battle message would be displayed indicating what the enemy did (like attacking you normally, attacking you with a
super attack, or wasting a turn).

6) The entire loop would be repeated.

To import the "randint" library, I need to import it form the "random" library (source: Clear Code on YouTube at
https://youtu.be/AY9MnQ4x3zk?si=mfCvPMEh2o7MNjM0).

To add the variable that will store the music that will play during the game, I need to use
"pygame.mixer.Sound(path to the song)" (source: Clear Code on YouTube at
https://youtu.be/AY9MnQ4x3zk?si=8LvD8ssCubbE2lgY&t=13575). Then, to play the music and to make it loop forever,
I need to use ".play(loops = -1)" (source: Clear Code on YouTube at
https://youtu.be/AY9MnQ4x3zk?si=epfdbPCbvBJeVaE0&t=13645).

===
Copyright information about the song used:

Music done by Alberto Salinas, A.K.A "Nemo", A.K.A "Becktor", A.K.A "ADSReal".
I got his explicit consent to use one of his tracks. DO NOT USE HIS MUSIC WITHOUT
HIS PERMISSION.

Track used: ADSReal-"Industrial Disaster" Original Instrumental Song:
https://soundcloud.com/nemoproducer/adsreal-industrial-disaster?si=4c93760c83084411b80e6e6fc102c211&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

Link to Alberto Salinas' Soundcloud profile, which is were I got the track that
I used: https://soundcloud.com/nemoproducer?ref=clipboard&p=a&c=1&si=216b578bd1c1487694ed1d13f270b191&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
====

====

Copyright information about the Sprite used:

I added a sprite by Penusbmic from his "Sci-Fi Character Pack 8" at itch.io at
https://penusbmic.itch.io/sci-fi-character-pack-8. The sprite used is called "The Storm Head Droid".

How to scale a sprite to make it bigger in Pygame: you need to get the sprite, use the pygame.transform.scale()
function to it, and put as parameters the variable with the sprite in it, the new width, and the new height (source:
Coding With Russ on YouTube at https://youtu.be/Xzmpl5tnJnc?si=58Mj8YgG3SoqKEek&t=54 ).
"""
import sys

import pygame

from sys import exit  # If I want to exit the game properly, I'll use sys.exit()

import random

# I will import "random" and "randint" so that the characters do random amounts of damage based on their base attack
from random import randint

# # Class which will store the characters' Health Points and Attack Points as properties
# class Character:

# All of this code should make it so that a black screen shows up when you execute this python script (source:
# https://youtu.be/AY9MnQ4x3zk?si=28DorTag9IRSrUi3&t=1099).
# I think this activates Pygame. Without this, I can't activate the font for the game.
pygame.init()

# This will render any screen / window, be it the battle screen, the press start screen, etc
game_window = pygame.display.set_mode((720, 576))

# This will add the game's title to the window's tab
pygame.display.set_caption("Gold Standard")

# Music. ACTIVATE LATER.
game_music = pygame.mixer.Sound("assets/audio/industrial-disaster-alberto-salinas-no-guitar.mp3")  # Game's music
game_music.play(loops=-1)  # This plays the music, and makes it loop indefinitely

""" Class that stores the properties for each character (both the player and the enemy).

Now, I could consider creating the Character class so that I can store the character’s name, HP, and attack points by 
using object oriented programming, so that I can easily access the remaining HP and the attack points from both the 
player and the enemy. Also, by using “name” as another property or field, I could easily render the name of the main 
character and the enemy by using formatted strings (“f({variable})”).

First, I need to make an __init__ function, and I will pass "self", and the health points, attack points, and 
the character's name as parameters (source: my "Cookie Jar" 2025 Homework submission from Week 8 for 
CS50 Python's Harvard's course.)

To be able to easily read the properties of the Character class, I will also create a __str__() function, and 
return each property of it (source: my "Cookie Jar" 2025 Homework submission from Week 8 for CS50 Python's Harvard's 
course.)

I’m properly adding and creating the main character by using the Character class by using object oriented programming.

I created both the player and the enemy as global variables since I want to access the player and the enemy's 
properties in all of my functions, be it on main(), or be it in the other 3 functions that I need to create.

I reactivated  the music, added 1 more potion so that you have 3 potions in total, and I fixed the “game over” 
message so that it’s shorter and doesn’t overflow the text box. I’m done with the coding aspect of this project.
"""


class Character:

    # Init() function
    def __init__(self, name, health_points, attack_points):
        # Character's name
        self.name = name

        # Character's health points (HP)
        self.health_points = health_points

        # Total number of health points (this will never go down during battle)
        self.total_hp = health_points

        # Character's attack points
        self.attack_points = attack_points

    # __str__() function
    def __str__(self):
        return f"{self.name} - HP: {self.health_points} - Attack points: {self.attack_points}"


# This creates the player and the enemy by using the Character class
# This will create the player's stats by using the Character class
player = Character("Ludwig", 100, 20)

# This creates the enemy's statistics / stats by using the Character class
# You will need to use potions to beat this enemy
enemy = Character("Hostile Robot Leader", 190, 20)
# enemy = Character("Hostile Robot Leader", 500, 50)  # High on HP. Hard so that you can lose.
# enemy = Character("Hostile Robot Leader", 100, 15)  # Low on HP so that you can win easily

# # DEBUG: this should print me the enemy's properties
# print("Enemy's stats: ")
# print(str(enemy))

# # DEBUG: this should print me the properties of the playable character
# print("Player's stats: ")
# print(str(player))

# This specifies the font that I will use, and its size. At least, I'll use this for the playable character's name.
game_font = pygame.font.Font(None, 32)
players_current_hp = 100  # This stores the current HP for the player. This goes down if the enemy hurts you.
players_number_of_potions = 3  # Initial number of potions that the player has.


battle_message = "A Hostile Robot Leader has appeared!"  # Battle message. This will change throughout the game.
battle_message_2 = ""  # If I need to add a second line of text to avoid text from overflowing the dialogue box.
display_battle_intro_message = True  # Boolean that will tell me if I should display "Enemy has appeared!" message.
display_battle_menu = False  # Boolean that will tell the game if it should render the battle menu's UI.

# Sprites and surface
# This loads the enemy sprite, but doesn't render it yet (source:
# https://youtu.be/AY9MnQ4x3zk?si=2sgfMIq-zyCv-eHx&t=2645).
# EDIT LATER, since I'm using a PLACEHOLDER sprite.
enemy_surface_small_sprite = pygame.image.load('assets/images/sprites/enemy-sprite-penusbmic.png').convert_alpha()
# This scales the sprite to make it bigger
enemy_surface = pygame.transform.scale(enemy_surface_small_sprite, (70, 110))

# This creates a rectangle for the enemy sprite's surface. I will place it around the center of the screen.
enemy_rectangle = enemy_surface.get_rect(center=(360, 288))

# Text surfaces and rectangles.

# Surface for the Battle Messages
battle_messages_surface = game_font.render(battle_message, False, 'White')
battle_messages_rectangle = battle_messages_surface.get_rect(topleft=(35, 30))  # Battle messages' rectangle
battle_messages_2_rectangle = battle_messages_surface.get_rect(topleft=(35, 65))  # Battle message 2's rectangle

# Surface for the Playable Character's name
playable_characters_name_surface = game_font.render('Ludwig', False, 'White')

# Playable character's name's rectangle
playable_characters_name_rectangle = playable_characters_name_surface.get_rect(center=(360, 440))

# Surface for the Playable Character's HP (Hit Points / life points)
players_hp_surface = game_font.render(f'HP: {player.health_points}/{player.total_hp}', False, 'White')

# Rectangle for the Player's HP
players_hp_rectangle = players_hp_surface.get_rect(center=(360, 480))

# Surface for the Enemy's HP (Health Points)
enemys_hp_surface = game_font.render(f'Enemy\'s HP: {enemy.health_points}/{enemy.total_hp}', False, 'White')

# Rectangle for the Enemy's HP
enemys_hp_rectangle = enemys_hp_surface.get_rect(midleft=(50, 238))

# Battle Menu UI
attack_command_surface = game_font.render('[1]: Attack', False, 'White')  # Attack command's surface
attack_command_rectangle = attack_command_surface.get_rect(topleft=(35, 30))  # Attack command's rectangle

guard_command_surface = game_font.render('[2]: Guard', False, 'White')  # Guard command's surface
guard_command_rectangle = guard_command_surface.get_rect(midleft=(35, 80))  # Guard command's rectangle

potion_command_surface = game_font.render(f'[2]: Use Potion ({players_number_of_potions} remaining)',
                                          False, 'White')  # Use Potion command
potion_command_rectangle = potion_command_surface.get_rect(midtop=(360, 30))  # Use Potion command's rectangle
# End of the Battle Menu UI
# End of text surfaces

# Booleans that keep track of the player and the enemy's turns
has_player_attacked = False  # This tells me if the player selected the "Attack" command
is_players_turn = True  # This tells me if the current turn is the player's turn
is_enemys_turn = False  # This tells me if the current turn is the enemy's turn.
did_enemy_use_regular_attack = False  # This tells me if the enemy used a normal attack

# Game over and Victory booleans
victory = False
game_over = False

# Exit game boolean
should_exit_game = False

# Functions / methods.

""" Main() function.

I will call the 3 functions required for this project from this function. 

I think I will call the “while True” function from the main() function. Otherwise, I have no arguments to pass to the 
main() function. Most of the code that will make the game run will be on the main() function.

Infinite loop that will render the game.

I could later on use a “match / case” so that, depending on the button that you pressed (“1”, “2”, or “3”), I will do
the selected command (I will either attack, defend, or heal).

My plan worked! If I update the surface variable for the battle message (which contains the battle message), and then I
try to render the battle message via using blit(), the “battle message” variable will be updated with the modified
battle message. In my case, i’m updating the “battle message” variable to “you have attacked the enemy!” if you press
the “1” key. Then further down the “while true” loop, if the “display battle menu” boolean is false (the battle menu
isn’t being rendered), when I render the surface of the battle message by using blit(), I re-create the surface for the
battle message. Otherwise, the “battle message” variable inserted as the 1st parameter of the surface will eb the one
declared before the “while true” loop, which, at that point, is “an enemy has appeared!”

Now, I think I will update the battle message based on the command selected on the battle menu (“you have attacked the 
enemy!”, “you’re on guard!”, etc) by calling a function. This way, I’ll have one out of the 3 functions that I’ll need 
to pass all the requirements for this project.

I could make a function for the player’s turn, another one for the enemy’s turn, another one for calculating the damage 
that you or the enemy will make (since it will be random, but based on the attack points of each character); and one 
for determining if you won. I could make another one for displaying a game over screen if you get killed.

I’ll make the first variables into global variables, since I need to sue them in multiple functions. To work with a 
global variable in any of my functions, i need to type “global”, and then I should put the name of the global variable 
that I’m trying to access to right after it (source: David Malan’s “Etcetera” lecture from CS50 Python at 
https://youtu.be/6pgodt1mezg?si=OxrGP1zD_d6kUBae&t=964 ).

That is, IF I need to use global variables to begin with.

I just want to render a message that says “you’ve dealt (points of damage) points of damage to the enemy” right after 
selecting “attack”. The battle message that says how much damage you did to the enemy SHOULD APPEAR ONLY after the 
battle message “the player attacks!” shows up! To do this, I need to insert a new “if” statement after the “the player 
attacks!” message shows up.

It would be a good idea to make 2 new booleans: one for keeping track if it’s your turn, and another one for keeping 
track if it’s the enemy’s turn. That will make things much easier for me.

Now, I want to actually reduce the enemy’s HP by 15 when the player hits him. I don’t want to hard code a message 
without actually reducing the enemy’s hit points. Then, I will use the random library so that the player can do random 
damage between +10 and -10 points from their base attack points (i.e: that the player can do between 10 and 30 points 
of damage if their base attack points are 20).

I will need to find a way to create multi-line dialogues in pygame. And no: using “n” didn’t work. I need to find a 
way to either render a proper line-break while rendering the text surface; or render the string surface twice, but by 
using slice() to first render the first half of the dialogue, and then using slice from the second half of the dialogue. 
That, or I could make another variable called “battle_message_2”, which would store the 2nd half of the dialogue there 
(I would hard-code that string that would always be inside the “battle message 2” variable). Creating the “battle 
message 2” variable and hard-coding the text that would go into it would be the fastest solution, even if it’s not the 
most efficient one. I would need to render this new battle message variable’s surface right below the first battle 
message. I would also need to declare and leave empty the “battle message 2” variable as a global variable.

I will use "random.randint(smallest_number, largest_number)" to randomly generate the damage output from each
character, so that their attacks always deal random damage to add variety to the gameplay (source: Clear Code on 
YouTube at https://youtu.be/AY9MnQ4x3zk?si=mfCvPMEh2o7MNjM0). However, the damage output
won't be 100% random. It will be based on the character's base damage. For instance, the attack could be either 10 
points lower or 10 times higher than the character's base damage. 

Let’s see: now, let’s create the enemy’s turn. To do that, let’s first make the enemy render a battle message that 
says “the enemy attacks the player!”. This message should show up right after the player’s turn ends (be it for 
attacking, be it for guarding, or be it from drinking a potion). It's pointless to check if the battle menu is
being rendered during the enemy's turn, since the battle menu will never be rendered on the enemy's turn. I need
to also create another boolean to detect if the enemy has done a regular attack. Then, if I detect that the enemy
did a regular attack, I will also detect if the player pressed the confirmation key. If the player hit the 
confirmation key after the boolean that detects if the enemy attacked is true, then I will render how much damage
the enemy did to the player.

Note: to simplify things, and to avoid confusion, instead of printing the player’s name, I will print “you” in the 
battle messages. You only have 1 party member, after all. 

The battle can keep going on and on, correctly switching between the player’s turn and the enemy’s turn. And it can 
keep going until the player has negative HP points.

Now the UI is being updated to show that the Player’s HP is being reduced by the enemy’s attack.

Also, after the enemy hits the player, I want to render the battle menu again, since it would start the player’s turn 
once again. Now, after the enemy finishes attacking you, the battle menu is rendered again during the player’s turn.
And you can attack again right after hitting “1” in the battle menu! And pressing “Z” in the battle menu doesn’t cause 
any bugs.

Well, I think that I can now put the winning and the losing conditions. I’ll make it so that, if the player has less or 
equal to 0, I will render a message that says “You lost all of your HP. Game Over”. Meanwhile, if your enemy’s HP is 
less or equal to 0, I will render the message “Congrats! You won! You defeated the boss!”

I made a modification to the variables that display in the UI how much life you have left: instead of hard-coding that 
you have a total of 100 HP points while you’re in full health, I created a new property in the Character class called 
“Total HP”. In it, I will store the total number of health points that the character has. This total number of HP 
points will NEVER go down. It just indicates how much HP you have lost during the battle. Since I will also display 
the enemy’s HP in a UI, I want to also display the total number of HP points from him.

Also, to make things easier for me (and to provide “feedback” or “game feel” to the user), I will display in the UI the 
enemy’s remaining HP. 

BUGFIX: I fixed a bug in which, if I harmed the enemy, the enemy’s UI’s HP would render both the text with the enemy’s 
HP when he was at full health, as well as another text slightly to the side showing the reduced number of HP points of 
the enemy after being attacked by the player. Now, I’m rendering a black box with a white border to center to censor 
the HP of the enemy from the past turn, so that the HP text always looks good in the UI: Sure: that means that, each 
turn, my HP text from previous turns is accumulating behind the black rectangle. That is, my game is inefficient. 
However, for the time being, the game works, so I’ll leave it at that for the time being.

First things first: let’s implement the “you win” screen if you win.

If you defeat the enemy, I will do the following:
1) I will make the enemy’s UI to display “0” instead of negative numbers once you defeat him.

2) I will exit the game by using sys.exit() once you win (or get a game over, for that matter).

3) I will try to display how much damage the player did in the battle message BEFORE showing the victory message. This 
could be done by checking yet another boolean, and by detecting if the player presses “Z” once again in the “if it’s 
the player’s turn” in the “for” loop that detects for events. 

Making a boolean for when you get a game over, and making a boolean for when you beat the game would be a good idea. 
They don’t need to be global variables. The could be local variables within the main() function, since the main 
function renders most of the game, anyways. But, given that I will need to use asserts later on to make unit tests, 
and since the additional functions that I need to create need to be OUTSIDE of the main function, I’m better off by 
creating as many global variables as possible (unless I want to pass any values as parameters to the new functions 
that I need to create.)

Now, if the player deals the finishing blow, I will first render the battle message showing how much damage I did to 
the enemy. Then, if you hit the confirmation key once again, you render the victory message.

Then, I will exit the game with sys.exit() after you hit the confirmation key right after reading the victory message.

Now, I will do a similar thing if I lose the game: I will exit the game after hitting the confirmation key after 
rendering the Game Over screen.

Now, when you get defeated:

1) I will render how much damage the enemy did to me in the finishing blow BEFORE rendering the Game Over screen.

2) I will update the Player’s UI so that negative numbers are never rendered as HP. That is, that, if the enemy gives 
me the finishing blow, I will render “0” in the HP UI for the player.

I will NEVER activate the battle menu during the enemy’s turn if the player loses all of their HP.

Now, if I hit the “z” key after the “game over” message, I correctly close the game.

I’ve removed the “Guard” command, and now, to drink a potion, you need to press the “2” key. Also, I replaced the 
number in the drinking potion command to be a “2” instead of a “3”

Now, the amount that you heal from drinking a potion is stored in a variable, and is printed dynamically via formatted 
strings. 

Now, if I drink a potion, and I could heal over my total HP, my total HP healed is NEVER above my current total number 
of HP points.

You can no longer use the “potion” command if you run out of potions. Pressing "2" won't do anything if you run out
of potions.

One way to fix the bug in which the player attacks the enemy immediately after drinking a potion would be to use 
booleans to detect whether the user is attacking or using a potion. I don’t like overusing booleans, but that would 
work. If the player is attacking, I would put a boolean that says “player is attacking”. Meanwhile, if the player is 
drinking a potion, I will put a boolean saying “player is drinking potion”. Then after doing either action, I will pass 
the turn to the enemy. And when the player’s turn begins, I will set both the “attacking” and the “drinking potion” 
booleans to false.

In the end, I didn't even need to create a boolean for drinking potions, and I had created a long time ago a boolean
for keeping track if you're attacking. The bug that caused the player to attack right after drinking a potion was that 
the "has player attacked" boolean was never being disabled after attacking. Also, I fixed the bug in which the game 
froze if I drank a potion on the very first turn. The bug was that the player's turn never ended after drinking a
potion.

So, now I will try my strategy of requiring the player to drink a potion to defeat the enemy. I will make the enemy 
have like 300 HP. So, you will have to use your potions only when you’re really low on HP to be able to last enough 
turns to defeat the enemy. The player will need a strategy in order to beat the boss. Just hitting the attack button 
won’t work.

The game now has some strategy. You can no longer win by spamming the “attack” command. And you can’t drink the potions 
whenever you feel like. You need to drink them whenever your HP is really low. If you drink them while your HP is high, 
you waste them, and you will most likely lose at the end. If the boss has 200 HP and the same attack points as the 
player, the difficulty is just right (medium to medium-easy, if you know when to drink the potions). 

My additional functions aren't particularly complex. But at least I'll be able to put an assert to them.


"""


def main():
    # Global variables. This snippet will let me access all the global variables declared.
    global display_battle_intro_message
    global display_battle_menu
    global players_number_of_potions
    # global hp_amount_that_potions_heal
    global battle_message
    global battle_message_2
    global has_player_attacked  # This keeps track of whether the player chooses the "Attack" command.
    global is_players_turn
    global is_enemys_turn
    global did_enemy_use_regular_attack
    global players_hp_surface
    global enemys_hp_surface
    # global enemys_hp_rectangle
    global battle_messages_surface
    global potion_command_surface
    global victory
    global game_over
    global should_exit_game

    # End of the Global Variables

    # I could create some local variables. I don't need to use that many global variables.
    # is_player_attacking = False
    # is_player_using_potion = False  # This keeps track of whether the player chose the "Potion" command.

    while True:  # Infinite loop that will pretty much make the entire game run
        # while not should_exit_game:  # Loop that will pretty much make the entire game run. Exits if Game over or
        # Victory.

        # For any input taken by the user (such as clicking the mouse or closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks "X" on the window's tab to close the game

                # This will efficiently close the game
                pygame.quit()
                exit()

            # If the user presses a key
            if event.type == pygame.KEYDOWN:

                # If it's still the enemy's turn, but the battle menu is activated and you press "Z"
                if is_enemys_turn and display_battle_menu and event.key == pygame.K_z:
                    # I will activate the player's turn, and deactivate the enemy's turn
                    is_players_turn = True
                    is_enemys_turn = False

                # If you either won or got a Game Over, and press the confirmation key
                if should_exit_game and event.key == pygame.K_z:
                    # This will exit the game.
                    sys.exit("You have exited the game.")

                elif game_over and event.key == pygame.K_z:  # If you get defeated

                    # # I want the player's HP to be equal to 0 if it's a negative number
                    # if player.health_points < 0:
                    #     player.health_points = 0

                    # I will render "Game Over" in a battle message
                    battle_message = "You've been defeated."
                    battle_message_2 = "GAME OVER"

                    # This should overwrite the battle message surface with the new battle message after any action in
                    # the game.
                    battle_messages_surface = game_font.render(battle_message, False, 'White')

                    # This renders the text for the current battle message
                    game_window.blit(battle_messages_surface, battle_messages_rectangle)

                    # This renders the second line of text if the text is too long
                    battle_messages_2_surface = game_font.render(battle_message_2, False, 'White')
                    game_window.blit(battle_messages_2_surface, battle_messages_2_rectangle)

                    # This will let me exit the game the next time the user presses the confirmation key
                    should_exit_game = True


                # If it's the player's turn
                elif is_players_turn:

                    # # If you either won or got a Game Over
                    # if should_exit_game and event.key == pygame.K_z:
                    #
                    #     sys.exit("You have exited the game.")

                    # If the user presses a "confirmation" key ("Z") while the "enemy has appeared" message is being
                    # displayed.
                    if event.key == pygame.K_z and display_battle_intro_message:
                        # This will turn the boolean that displays the "enemy has appeared!" message to "False"
                        display_battle_intro_message = False

                        # This will let me render the battle menu's UI
                        display_battle_menu = True

                        # # DEBUG: This should print "False" for the boolean that displays the intro message
                        # print("Intro message boolean's current state: " + str(display_battle_intro_message))

                    if display_battle_menu:  # If the battle menu is being displayed

                        # # I will use a match / case to detect which of the 3 battle command keys are being pressed
                        # match event.key:

                        # If the user presses the "1" key
                        if event.key == pygame.K_1:

                            # case pygame.K_1:  # If the user presses "1"

                            # This makes the battle menu to disappear so that the battle messages are rendered
                            display_battle_menu = False

                            # # This tells the game that the player is attacking, not using a potion.
                            # is_player_attacking = True

                            # DEBUG: this will modify the battle message so that it says that you attacked the enemy.
                            # NONE OF THESE 2 lines of code work! They don't render anything to the screen!
                            # battle_message = "Ludwig attacks the enemy!"
                            # game_window.blit(battle_messages_surface, battle_messages_rectangle)

                            # This updates the battle message to indicate that the player attacked the enemy
                            battle_message = f"{player.name} attacks the {enemy.name}!"

                            battle_message_2 = ""  # Second line of the battle message (empty)

                            # # DEBUG: print "you attacked"
                            # print(f"{player.name} attacks the enemy!")

                            # This tells me that the player just selected the "attack" command, and not using a potion
                            has_player_attacked = True

                            # DEBUG: This tells me what the current value of the "has player attacked" boolean
                            print("has player attacked boolean value: " + str(has_player_attacked))

                            # # This should stop the "for event" loop (source: w3schools at
                            # # https://www.w3schools.com/python/ref_keyword_continue.asp).
                            # break

                            # # If you press the "confirmation" key again ("Z"), a new battle message will show up
                            # if event.key == pygame.K_z:
                            #     # This shows how much damage you've dealt to the enemy
                            #     battle_message = "You've dealt 15 points of damage to the enemy!"

                            # case pygame.K_2:  # If the user presses "2"
                            #
                            #     # This makes the battle menu to disappear so that the battle messages are rendered
                            #     display_battle_menu = False
                            #
                            #     # This updates the battle message to indicate that you're guarding
                            #     battle_message = "Ludwig is on guard!"
                            #
                            #     # DEBUG: print "you are on guard"
                            #     print("Ludwig is on guard!")
                            #
                            #     # Your turn ends, and the enemy's turn begins
                            #     is_players_turn = False
                            #     is_enemys_turn = True

                        # If the user presses "2", I'll handle the potion drinking mechanic
                        elif event.key == pygame.K_2 and players_number_of_potions > 0:

                            # This makes the battle menu to disappear so that the battle messages are rendered
                            display_battle_menu = False

                            # I could all of this in the drink_potion() function, and just return the total HP healed

                            # This restores the player's HP by calling a function that will make them use a potion.
                            # The function will make sure to not heal the player beyond their total HP.
                            player.health_points = drink_potion(player.health_points, player.total_hp)

                            # I should update the UI so that players can see that their HP has increased
                            players_hp_surface = game_font.render(f'HP: {player.health_points}/{player.total_hp}',
                                                                  False,
                                                                  'White')

                            # Now, the enemy's turn begins, and the player's turn ends
                            is_players_turn = False
                            is_enemys_turn = True



                    else:  # If I'm no longer rendering the battle menu, and I'm rendering battle messages

                        # # If the user presses a key
                        # if event.type == pygame.KEYDOWN:

                        # If the player chose "Attack" and presses the confirmation key.
                        if has_player_attacked and event.key == pygame.K_z:

                            # FIRST OF ALL, I need to tell the game that the player is no longer attacking.
                            # This will prevent the character from attacking right after they drink a potion.
                            has_player_attacked = False

                            # This randomly calculates the damage that the player can do to the enemy (from -10 to 10).
                            # I COULD REFACTOR THIS TO PUT IT ON A FUNCTION OUTSIDE OF main()!
                            randomly_generated_damage_output = damage_calculation(player.attack_points)
                            # randomly_generated_damage_output = player.attack_points + random.randint(-10, 10)

                            # This shows how much damage you've dealt to the enemy
                            battle_message = (
                                f"{player.name} has dealt {randomly_generated_damage_output} points of "
                                f"damage")

                            # battle_message = f"{player.name} has dealt {player.attack_points} points of damage"

                            # Second line of text to prevent the text from getting outside the dialogue box
                            battle_message_2 = f"to the {enemy.name}!"

                            # This should reduce the enemy's HP from the player's attack.
                            # I COULD REFACTOR THIS TO PUT IT ON A FUNCTION OUTSIDE OF main()!
                            # This sends the enemy's HP and the damage they suffered into a function to update
                            # their HP.
                            enemy.health_points = health_points_remaining_calculation(enemy.health_points,
                                                                                      randomly_generated_damage_output)
                            # enemy.health_points = enemy.health_points - randomly_generated_damage_output

                            # I will update the UI that displays the enemy's HP
                            # Surface for the Enemy's HP (Health Points)
                            enemys_hp_surface = game_font.render(f'Enemy\'s HP: {enemy.health_points}/{enemy.total_hp}',
                                                                 False, 'White')

                            if enemy.health_points == 0:  # If you defeat the enemy, you win
                                victory = True

                            # # DEBUG: This tells me how many HP points the enemy has after being attacked
                            # print("Enemy's HP points left: " + str(enemy.health_points))

                            # Now, the enemy's turn begins. The player's turn ents
                            is_players_turn = False
                            is_enemys_turn = True

                elif victory and event.key == pygame.K_z:  # If you defeated the enemy

                    # # If the enemy loses all of their HP, you win, and you beat the game
                    # if enemy.health_points <= 0:
                    # I will render "You Win! Congrats" in a battle message
                    battle_message = "You've defeated the enemy!"
                    battle_message_2 = "Congrats!"

                    # This should overwrite the battle message surface with the new battle message after any action in the game.
                    battle_messages_surface = game_font.render(battle_message, False, 'White')

                    # This renders the text for the current battle message
                    game_window.blit(battle_messages_surface, battle_messages_rectangle)

                    # This renders the second line of text if the text is too long
                    battle_messages_2_surface = game_font.render(battle_message_2, False, 'White')
                    game_window.blit(battle_messages_2_surface, battle_messages_2_rectangle)

                    # This will let me exit the game after hitting the confirmation key one more time
                    should_exit_game = True

                    # # This will close the game and exit the program. I want to display this AFTER the user hits the
                    # # confirmation key again.
                    # sys.exit("You've beaten the game! Congrats!")

                elif is_enemys_turn:  # If it's the enemy's turn

                    # If the user presses the confirmation key and the enemy does a regular attack
                    if event.key == pygame.K_z and did_enemy_use_regular_attack is False:

                        # The dialogue box shows you that the enemy is attacking the player
                        battle_message = f"The {enemy.name} attacks you!"
                        battle_message_2 = ""  # Second line of the battle message (empty)

                        # This will render the message with the enemy deling damage with a regular attack
                        did_enemy_use_regular_attack = True

                    elif did_enemy_use_regular_attack and event.key == pygame.K_z:
                        # This randomly calculates the damage that the enemy can do to the player (from -10 to 10)
                        # CALL A FUNCTION HERE, so that the calculation is done in a function.
                        randomly_generated_damage_output = damage_calculation(enemy.attack_points)

                        # This shows how much damage you've dealt to the enemy
                        battle_message = (
                            f"The {enemy.name} has dealt {randomly_generated_damage_output} points of "
                            f"damage")

                        # Second line of text to prevent the text from getting outside the dialogue box
                        battle_message_2 = f"to you!"

                        # This should reduce the enemy's HP from the player's attack.
                        # I COULD REFACTOR THIS TO PUT IT ON A FUNCTION OUTSIDE OF main()!
                        # This will update the player's HP by sending their current HP and the damage suffered to a
                        # function.
                        player.health_points = health_points_remaining_calculation(player.health_points,
                                                                                   randomly_generated_damage_output)
                        # player.health_points = player.health_points - randomly_generated_damage_output

                        # If the Player gets negative HP or 0
                        # if player.health_points <= 0:
                        #     # I will always change the HP to "0" if the player is defeated
                        #     player.health_points = 0

                        if player.health_points == 0:  # If the player loses all their HP
                            game_over = True  # You lose the game if you lose all of your HP

                        else:  # If the player still has some HP left

                            # This will display the battle menu after the enemy attacks the player
                            display_battle_menu = True

                        # Updating the Player's HP in the UI
                        players_hp_surface = game_font.render(f'HP: {player.health_points}/{player.total_hp}', False,
                                                              'White')

                        # # DEBUG: This tells me how many HP points the enemy has after being attacked
                        # print("Your HP points left: " + str(player.health_points))

                        # This will let the enemy render the "enemy attacks!" message after the player's turn
                        did_enemy_use_regular_attack = False

                        # # Now, the player's turn begins
                        # is_players_turn = True
                        # is_enemys_turn = False

        # If no input is detected by the user (if they don't click nor press any keys), this will execute

        # This renders the sprites

        # This renders the enemy's sprite. The position will be rendered with a rectangle.
        game_window.blit(enemy_surface, enemy_rectangle)

        # Battle Messages' UI.

        # White rectangle. This will act as a border for a black box that will contain the battle messages.
        # In the last 4 parameters, I will first specify the X and Y coordinates, and then the width and the height.
        pygame.draw.rect(game_window, 'White', ((20, 15), (680, 160)))

        # Black rectangle. This rectangle needs to be within the white rectangle so that my white text can be read.
        pygame.draw.rect(game_window, 'Black', ((30, 25), (660, 140)))

        if display_battle_menu and is_players_turn:  # If the boolean that lets me render the battle menu is true and if it's the player's turn

            # Show the battle menu
            game_window.blit(attack_command_surface, attack_command_rectangle)  # Render the "attack" command
            # game_window.blit(guard_command_surface, guard_command_rectangle)  # Render the "guard" command
            game_window.blit(potion_command_surface, potion_command_rectangle)  # Render the "use potion" command

        else:  # If the battle menu is set to False, render the battle messages

            # This should overwrite the battle message surface with the new battle message after any action in the game.
            battle_messages_surface = game_font.render(battle_message, False, 'White')

            # This renders the text for the current battle message
            game_window.blit(battle_messages_surface, battle_messages_rectangle)

            # This renders the second line of text if the text is too long
            battle_messages_2_surface = game_font.render(battle_message_2, False, 'White')
            game_window.blit(battle_messages_2_surface, battle_messages_2_rectangle)

        # END OF THE SNIPPET THAT I NEED TO REACTIVATE LATER.

        # End of the Battle Messages' UI.

        # Player's UI.
        # White rectangle. This will act as a border for a black box / rectangle that will contain the player's stats.
        # I'll look up Pygame's documentation to learn how to draw a box / rectangle with custom dimensions.
        pygame.draw.rect(game_window, 'White', ((260, 400), (200, 160)))

        # Black rectangle. This rectangle needs to be within the white rectangle so that my white text can be read.
        pygame.draw.rect(game_window, 'Black', ((270, 410), (180, 140)))

        # pygame.Rect((360, 280), (200, 50))

        # This render's the playable character's name. It should be in the horizontal center, and below the enemy.
        game_window.blit(playable_characters_name_surface, playable_characters_name_rectangle)
        game_window.blit(players_hp_surface, players_hp_rectangle)  # Player's current HP
        # End of the Player's UI.

        # UI that displays the Enemy's HP
        # White rectangle. This will act as a border for a black box that will contain the Enemy's HP.
        pygame.draw.rect(game_window, 'White', ((30, 200), (260, 70)))

        # Black rectangle. This rectangle needs to be within the white rectangle so that my white text can be read.
        pygame.draw.rect(game_window, 'Black', ((40, 210), (240, 50)))

        game_window.blit(enemys_hp_surface, enemys_hp_rectangle)  # Enemy's current HP
        # End of the UI for the Enemy's HP

        # # For any input taken by the user (such as clicking the mouse or closing the window)
        # for event in pygame.event.get():
        #
        #     # If the user presses a key
        #     if event.type == pygame.KEYDOWN:
        #
        #         if has_player_attacked and event.type == pygame.K_z:
        #             # If the player chose "Attack" and presses the confirmation key.
        #
        #             # This shows how much damage you've dealt to the enemy
        #             battle_message = "You've dealt 15 points of damage to the enemy!"

        # This should render the game's window, and every sprite
        pygame.display.update()

    # End of the snippet that renders a black screen once you execute a pygame game (source:
    # https://youtu.be/AY9MnQ4x3zk?si=28DorTag9IRSrUi3&t=1099)

    # # This will close the game. It will only be executed if you press the confirmation key after Game over or Victory
    # sys.exit("You have exited the game.")


# """ Display battle message() function.
#
# This will display all the battle messages. That includes the default one: the one that says "an enemy has appeared!".
#
# Let me se Clear Code's 4-hour long tutorial, and see how he created and called the functions in his pygame game.
# """
#
#
# def display_battle_message():
#     return 1


""" Function 1: Damage calculation function. 

This function calculates damage to be dealt to either the player or the enemy.

I will refactor my snippets that calculates damage to extract it into a function. I will insert the attack points from 
the player and from the enemy as a parameter when I call the function. Then, in the function that calculates the 
damage, I will return the calculated damage as an integer. This function should raise a value error if the total damage 
is a float instead of an integer.

Then, I will create a unit test that will test that damage calculating function. If the assert has a float, it should 
return a value error.

I will take the damage dealt from my main function, which should be an integer, and then make the calculation here 
instead of making it in the main() function.

The damage calculation function should never give a negative number, and should never give a float. I could put a Value 
Error there to check that no floats nor negative numbers are assigned to it.

I think randint always generates an integer. So, you can only add a number generated by randint if the other
number isn't a string.

So, I will raise a value error if the damage points passed as a parameter isn't an integer. 

Also, I would like it that the damage points are never negative, since, for the time being, you're not healing
while taking damage from the enemy.

To check if a variable is an integer, I should use isinstance(variable, int) (source: Katriel on Stack Overflow
at https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not).
"""


def damage_calculation(damage_points):

    # If the damage points are negative or aren't an integer
    if not isinstance(damage_points, int) or damage_points < 0:

        # I will raise a Value Error
        raise ValueError

    total_damage_dealt = damage_points + random.randint(-10, 10)

    return total_damage_dealt


"""  Function 2: Health Points remaining after being attacked.

This function calculates how much HP is remaining for that character, be it the enemy, or the player. The HP should be 
a float, and always positive.

The first parameter will be a character class, NOT an integer nor a string.

The third parameter will be
the total damage dealt to that character (which already adds the random number to the damage dealt).

I will make a function that will calculate how many health points the character has left (be it either the enemy
or the player). It will return an integer, which will be the new number that should be added to the enemy or to
the player's health points. Sure, the hp remaining() function is just a subtraction, but it also makes the HP
automatically zero if the HP is negative. Neither the player nor the enemy should show negative HP.

This should also always return and integer, and 0 or a positive number. I will add a Raise ValueError here otherwise.
I need to look at the parameters to raise Value Errors, though. So, since neither the total damage dealt nor the 
current HP can be a float, and neither can be strings, I could raise a value error. I'll raise a value error
if either of thise values are not integers.
"""


def health_points_remaining_calculation(current_hp, total_damage_dealt):

    # If the current HP isn't an integer
    # If the damage points are negative or aren't an integer
    if not isinstance(current_hp, int) or not isinstance(total_damage_dealt, int):

        # I will raise a Value Error
        raise ValueError


    # This updates the character's current number of health points
    hp_remaining = current_hp - total_damage_dealt

    # If the character gets negative HP or 0
    if hp_remaining <= 0:
        # I will always change the HP to "0" if the enemy's defeated
        hp_remaining = 0

        # victory = True  # You win the game if you defeat the enemy

        # # This will close the game after you hit the confirmation key one more time
        # should_exit_game = True


    return hp_remaining


""" Function 3: Potion Drinking function.

The potion function would be a good one. It would heal the player, and it would reduce the number of potions in your 
backpack by one. Also, it should never be called if it’s 0. However, what should it return? It needs to return 
something. It could return a string. It could return a console message such as “you have consumed a potion” if you have 
at least 1 potion remaing, or “you don’t have any potions remaining. You’ll have to do something else with your turn”. 
This would only be read in the console. But, for the rest, it would consume 1 potion, and heal the player in the 
“backend”. OR, the string that could return could be the battle message saying that the user drank a potion.

The total amount that potions heal, instead of being a global variable, could be a local variable inside of the 
drink_potion() function. So, the amount healed to the player would need to be returned by the drink_potion() function.

Heck, even the fact that your HP should never go beyond your total HP points if you were at full health could also be 
inside the drink_potion() function.

Also, I would raise errors if the HP healed by the potion is either negative, or float numbers, or a string.

"""


def drink_potion(current_hp, total_hp):

    # Global variables that I'll use
    # This takes your number of potions from a global variable
    global players_number_of_potions
    global battle_message
    global battle_message_2
    global potion_command_surface

    # Amount of HP that potions heal. This can be a local variable within this function.
    hp_amount_that_potions_heal = 80  # Number of Health Points that you can heal from drinking potions

    # This reduces the number of potions that you have by 1
    players_number_of_potions = players_number_of_potions - 1

    # This will increase the Player's HP to heal them by using the potion.
    # The player should NEVER get any more HP than their total number of HP point
    if current_hp + hp_amount_that_potions_heal > total_hp:
        players_hp_after_using_potion = 100
    else:
        # If you don't go over your total HP, add potion's HP amount to player's HP
        players_hp_after_using_potion = current_hp + hp_amount_that_potions_heal

    # This updates the battle message to indicate that you're drinking a potion
    battle_message = f"You drank a potion!"
    battle_message_2 = f"You have recovered {hp_amount_that_potions_heal} points of HP!"

    # This will update the battle menu's UI to update the number of potions remaining
    potion_command_surface = game_font.render(
        f'[2]: Use Potion ({players_number_of_potions} remaining)',
        False, 'White')  # Use Potion command

    # # # DEBUG: print "you have drank a potion"
    # # print(f"Ludwig drank a potion! You have recovered {hp_amount_that_potions_heal} points of HP!")
    # # This prints how many potions you have remaining
    # print(f"Now, you have {players_number_of_potions} potions left.")

    return players_hp_after_using_potion


""" This lets me use the main function if I import this script as a library without any issues (source: my 
"Shirtificate" assignment from Week 8 from my 2025 homework assignment submission for Harvard's CS50 Python's course).
"""
if __name__ == "__main__":
    main()
