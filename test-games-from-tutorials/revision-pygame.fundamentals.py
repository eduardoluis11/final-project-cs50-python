#!/usr/bin/env python
#
# Tom's Pong
# A simple pong game with realistic physics and AI
# http://tomchance.org.uk/projects/pong
#
# Released under the GNU General Public License

""" Source of this code for this Pong tutorial game: Pygame's official documentation at:
https://www.pygame.org/docs/tut/tom_games3.html .

"""

VERSION = "0.4"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *

except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

if __name__ == '__main__': main()