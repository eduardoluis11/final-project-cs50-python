# GOLD STANDARD
Here's my final project for Harvard University's CS50 Python course. I will submit this in 2025.


#### Video Demo:  https://youtu.be/EkhsLT5MJIM  


#### Author:
Eduardo Salinas

#### Description:
	
For my final project, I made a video game in Python by using the Pygame pip module. The game is a turn-based RPG. 

The objective of the game is to defeat the only enemy in the game. You need to attack them until you deplete their Health Points (HP). If you attack the enemy until their HP drops to zero, you will get a victory message. After pressing the “Z” key during the victory message, you will exit the game.

 If you lose all of your HP by getting attacked multiple times by the enemy, you will get a “Game Over” screen. And, just like when you defeat the enemy, if you press the “Z” key during this screen telling you that you were defeated, you will close the game.

The game is basically just reading messages during the battle by pressing the “Z” key. However, once your turn begins, you need to press either the “1” or the “2” key to do the next action in the battle menu that will show up. To damage the enemy, you need to press “1” to select the “Attack” command. Meanwhile, to heal yourself, you’ll need to drink one of your potions by selecting the “Potion” command by pressing “2”.

The reason why you need to press either “1” or “2” in the menu to select an action is that it was the easiest way for me to implement a battle menu to let you select a command. I initially tried to implement a traditional turn-based RPG menu where there were multiple commands, and you needed to select one by using the up arrow or the down arrow keys, and then pressing a key. However, doing that was way too difficult for me. Therefore, the easiest way of being able to select one of multiple commands in a menu was to just assign a key to each command. As a fun fact, this is exactly what games like Persona 5 do.

Originally, I was going to make a game with combat similar to the one used in Mother 3. In that game, you need to press the attack button to the beat of the background music during battles to deal a lot of damage to enemies. In fact, making a game similar to Mother 3, and calling the game “Gold Standard”, is an idea that I had over a year ago. However, I couldn’t implement Mother 3’s music-based combat, since it was too difficult for me to implement. Instead, I ended up creating a traditional turn-based RPG. I left the background black and used white menus to make the game look like old Japanese RPGs like Mother 1 / Earthbound Beginnings, or Dragon Quest 3.

The damage dealt by both the player and the enemy is randomly generated. Many Japanese RPGs, such as Final Fantasy, make both the enemies and the player deal random damage to give variety to the combat. Therefore, since I wanted to give variety to my game, I also made my characters deal random damage when they attack. However, the damage isn’t 100% random. Both the player and the enemy have abase attack of “20”. Well, I have a function that adds a random integer between -10 and 10 to their base attack. That is, both the player and the enemy can deal between 10 and 30 points of damage. In other words, the damage that the characters can deal is a random number between 10 and 30 points of damage.

The game requires a strategy to win. You can’t just select the “Attack” command over and over again without using any strategy, or you’ll most likely lose the game. Instead, you need to use your potions to heal you, so that you can last enough turns to deal enough damage to defeat the enemy. However, you need to use your potions wisely. If you use your potions while your HP is still high, you will have pretty much wasted that potion. You have a total of 100 HP, and you recover 80 HP per potion. If you drink a potion if you have, for instance, 90 HP, you will have a total of 100 HP after drinking it. Your HP will never be higher than your maximum HP, which is 100 HP. And you only have a few potions.

If you run out of potions too early by drinking them while your HP was relatively high, you won’t last enough turns to defeat the enemy, and you will lose. However, if you wait until your HP is relatively low to drink your potions, you will last enough turns to deal enough damage to the enemy to beat the game. 

However, you could still lose the game even if you drink your potions in an efficient way. Since the damage dealt by both the player and the enemy is randomly generated, if the enemy has good luck, they can deal you high amounts of damage. So, even while drinking your potions wisely, you could still lose the game sometimes. I would need to balance the difficulty later on to prevent the fact that you will sometimes lose due to back luck or bad “RNG”.

I named the main character “Ludwig” as a reference to “Ludwig van Beethoven”. Since the game was supposed to have a music-based combat, I wanted to put a musical reference to the game. So, I decided to put the name of a famous composer as the name of the main character.


##### What each file and folder does:

- project.py: This script is where all of the code for the game is located. You only need to execute this file to play the game properly.

- test_project.py: This script contains all the unit tests that you can execute with pytest to test my game.

- requirements.txt: This text file contains all the packages that you need to install to be able to run my game.

- credits.txt: This text file contains some of the references and other sources used for this project. Although I cited and gave credit to all my sources in the source code, I added this file as a redundant way of giving proper credit to every source that I used. 

- “assets” folder: This is where I stored the game’s music and art. The only track that I used for the game’s music is stored in the “audio” folder. Meanwhile, the only sprite or piece of game art that I used is in the “images/sprites” folder.


##### Instructions:

###### Controls:

- “Z”: Scroll through the messages to read them and continue with the battle. It doesn’t do anything if the battle menu that shows the “Attack” and “Potion” commands is visible.
 
- “1”: Attack. You can only use it if the battle menu that displays the “attack” and “potion” commands is visible.

- “2”: Use a potion. You can only use it if the battle menu showing the “attack” and potion commands is visible. And you can only use it if you have any potions left. If the player doesn’t have any potions left, pressing this key on your keyboard won’t do anything.

###### How to install:

You need to use Python 3.11 or an older version to run this game. YOU SHOULD NOT USE PYTHON 3.12 NOR NEWER VERSIONS OF PYTHON. This game runs on Pygame, and Pygame cannot be installed if you use any version of Python newer than Python 3.11. Therefore, use Python 3.11.4, or any older version of Python. It should run well on Python 3.9.

Install all the requirements from the requirements.txt file to be able to run my Python game. You can choose to either use a virtual environment to install the pip packages, or you could also install them directly on your local machine.


##### How to run

After installing Python 3.11 or older, and after installing the pip modules in the requirements.text file, you need to use the command “python project.py” to run the game on Windows. 

##### References, sources, and Copyright disclaimers

###### Music used


I used the track "Industrial Disaster", which was done by my younger brother, Alberto Salinas, A.K.A "Nemo", A.K.A "Becktor", A.K.A "ADSReal". I got his explicit consent to use this track. DO NOT USE HIS MUSIC WITHOUT HIS PERMISSION. I edited the original track by using Kdenlive. Link to the track: https://soundcloud.com/nemoproducer/adsreal-industrial-disaster 


###### Images and art used:

I added a sprite by Penusbmic from his "Sci-Fi Character Pack 8" from itch.io at
https://penusbmic.itch.io/sci-fi-character-pack-8. The sprite used is called "The Storm Head Droid". Link to their itch.io profile: https://penusbmic.itch.io/ 