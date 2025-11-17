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


"""

import pygame

from sys import exit  # If I want to exit the game properly, I'll use sys.exit()

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

# This specifies the font that I will use, and its size. At least, I'll use this for the playable character's name.
game_font = pygame.font.Font(None, 32)
players_current_hp = 100  # This stores the current HP for the player. This goes down if the enemy hurts you.
players_number_of_potions = 5  # Initial number of potions that the player has.

battle_message = "A Hostile Robot Leader has appeared!"  # Battle message. This will change throughout the game.
display_battle_intro_message = True  # Boolean that will tell me if I should display "Enemy has appeared!" message.
display_battle_menu = False  # Boolean that will tell the game if it should render the battle menu's UI.

# Sprites and surface
# This loads the enemy sprite, but doesn't render it yet (source:
# https://youtu.be/AY9MnQ4x3zk?si=2sgfMIq-zyCv-eHx&t=2645).
# EDIT LATER, since I'm using a PLACEHOLDER sprite.
enemy_surface = pygame.image.load('assets/images/sprites/red-rectangle-enemy-placeholder.png').convert_alpha()

# This creates a rectangle for the enemy sprite's surface. I will place it around the center of the screen.
enemy_rectangle = enemy_surface.get_rect(center=(360, 288))

# Text surfaces and rectangles.

# Surface for the Battle Messages
battle_messages_surface = game_font.render(battle_message, False, 'White')
battle_messages_rectangle = battle_messages_surface.get_rect(topleft=(35, 30))  # Battle messages' rectangle

# Surface for the Playable Character's name
playable_characters_name_surface = game_font.render('Ludwig', False, 'White')

# Playable character's name's rectangle
playable_characters_name_rectangle = playable_characters_name_surface.get_rect(center=(360, 440))

# Surface for the Playable Character's HP (Hit Points / life points)
players_hp_surface = game_font.render(f'HP: {players_current_hp}/100', False, 'White')

# Rectangle for the Player's HP
players_hp_rectangle = players_hp_surface.get_rect(center=(360, 480))

# Battle Menu UI
attack_command_surface = game_font.render('[1]: Attack', False, 'White')  # Attack command's surface
attack_command_rectangle = attack_command_surface.get_rect(topleft=(35, 30))  # Attack command's rectangle

guard_command_surface = game_font.render('[2]: Guard', False, 'White')  # Guard command's surface
guard_command_rectangle = guard_command_surface.get_rect(midleft=(35, 80))  # Guard command's rectangle

potion_command_surface = game_font.render(f'[3]: Use Potion ({players_number_of_potions} remaining)',
                                          False, 'White')  # Use Potion command
potion_command_rectangle = potion_command_surface.get_rect(midtop=(360, 30))  # Use Potion command's rectangle
# End of the Battle Menu UI
# End of text surfaces

# Booleans that keep track of the player and the enemy's turns
has_player_attacked = False  # This tells me if the player selected the "Attack" command

is_players_turn = True  # This tells me if the current turn is the player's turn
is_enemys_turn = False  # This tells me if the current turn is the enemy's turn.

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

I’ll make the first variables into global variables, since I need to sue them in multiple functions. To work with a global variable in any of my functions, i need to type “global”, and then I should put the name of the global variable that I’m trying to access to right after it (source: David Malan’s “Etcetera” lecture from CS50 Python at https://youtu.be/6pgodt1mezg?si=OxrGP1zD_d6kUBae&t=964 ).

That is, IF I need to use global variables to begin with.

I just want to render a message that says “you’ve dealt (points of damage) points of damage to the enemy” right after 
selecting “attack”. The battle message that says how much damage you did to the enemy SHOULD APPEAR ONLY after the 
battle message “the player attacks!” shows up! To do this, I need to insert a new “if” statement after the “the player 
attacks!” message shows up.

It would be a good idea to make 2 new booleans: one for keeping track if it’s your turn, and another one for keeping 
track if it’s the enemy’s turn. That will make things much easier for me.
"""


def main():
    # Global variables. This snippet will let me access all the global variables declared.
    global display_battle_intro_message
    global display_battle_menu
    global players_number_of_potions
    global battle_message
    global has_player_attacked

    # End of the Global Variables

    while True:  # Infinite loop that will pretty much make the entire game run

        # For any input taken by the user (such as clicking the mouse or closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks "X" on the window's tab to close the game

                # This will efficiently close the game
                pygame.quit()
                exit()

            # If the user presses a key
            if event.type == pygame.KEYDOWN:

                # If the user presses a "confirmation" key ("Z") while the "enemy has appeared" message is being displayed
                if event.key == pygame.K_z and display_battle_intro_message:
                    # This will turn the boolean that displays the "enemy has appeared!" message to "False"
                    display_battle_intro_message = False

                    # This will let me render the battle menu's UI
                    display_battle_menu = True

                    # # DEBUG: This should print "False" for the boolean that displays the intro message
                    # print("Intro message boolean's current state: " + str(display_battle_intro_message))

                if display_battle_menu:  # If the battle menu is being displayed

                    # I will use a match / case to detect which of the 3 battle command keys are being pressed
                    match event.key:

                        case pygame.K_1:  # If the user presses "1"

                            # This makes the battle menu to disappear so that the battle messages are rendered
                            display_battle_menu = False

                            # DEBUG: this will modify the battle message so that it says that you attacked the enemy.
                            # NONE OF THESE 2 lines of code work! They don't render anything to the screen!
                            # battle_message = "Ludwig attacks the enemy!"
                            # game_window.blit(battle_messages_surface, battle_messages_rectangle)

                            # This updates the battle message to indicate that the player attacked the enemy
                            battle_message = "Ludwig attacks the enemy!"

                            # DEBUG: print "you attacked"
                            print("Ludwig attacks the enemy!")

                            # This tells me that the player just selected the "attack" command
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

                        case pygame.K_2:  # If the user presses "2"

                            # This makes the battle menu to disappear so that the battle messages are rendered
                            display_battle_menu = False

                            # This updates the battle message to indicate that you're guarding
                            battle_message = "Ludwig is on guard!"

                            # DEBUG: print "you are on guard"
                            print("Ludwig is on guard!")

                        case pygame.K_3:  # if the user presses "3"

                            # This makes the battle menu to disappear so that the battle messages are rendered
                            display_battle_menu = False

                            # This updates the battle message to indicate that you're drinking a potion
                            battle_message = "Ludwig drank a potion! You have recovered 30 points of HP!"

                            # This reduces the number of potions that you have by 1
                            players_number_of_potions = players_number_of_potions - 1

                            # DEBUG: print "you have drank a potion"
                            print("Ludwig drank a potion! You have recovered 30 points of HP!")
                            # This prints how many potions you have remaining
                            print(f"Now, you have {players_number_of_potions} potions left.")

                else:   # If I'm no longer rendering the battle menu, and I'm rendering battle messages

                    # If the user presses a key
                    if event.type == pygame.KEYDOWN:

                        if has_player_attacked and event.key == pygame.K_z:
                            # If the player chose "Attack" and presses the confirmation key.

                            # This shows how much damage you've dealt to the enemy
                            battle_message = "You've dealt 15 points of damage to the enemy!"

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

        if display_battle_menu:  # If the boolean that lets me render the battle menu is true

            # Show the battle menu
            game_window.blit(attack_command_surface, attack_command_rectangle)  # Render the "attack" command
            game_window.blit(guard_command_surface, guard_command_rectangle)  # Render the "guard" command
            game_window.blit(potion_command_surface, potion_command_rectangle)  # Render the "use potion" command


        else:  # If the battle menu is set to False, render the battle messages

            # This should overwrite the battle message surface with the new battle message after any action in the game.
            battle_messages_surface = game_font.render(battle_message, False, 'White')

            # This renders the text for the current battle message
            game_window.blit(battle_messages_surface, battle_messages_rectangle)

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


""" This lets me use the main function if I import this script as a library without any issues (source: my 
"Shirtificate" assignment from Week 8 from my 2025 homework assignment submission for Harvard's CS50 Python's course).
"""
if __name__ == "__main__":
    main()
