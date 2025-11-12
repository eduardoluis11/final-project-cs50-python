""" Test game from "Help! How Do I Move An Image?" from Pygame's official documentation. Source of most of the code:
https://www.pygame.org/docs/tut/MoveIt.html .

Source of some of the other snippets used: https://www.pygame.org/docs/tut/PygameIntro.html .
"""

import sys, pygame
pygame.init()

# size = width, height = 1000, 800
# # size = width, height = 320, 240   # This size is too small, so the ball bounces way too quickly
# # speed = [2, 2]
# black = 0, 0, 0
#
# screen = [1, 1, 2, 2, 2, 1]
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#
#
#     # screen.fill(black)
#     # pygame.display.flip()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('intro_ball.gif').convert()
entity = pygame.image.load('intro_ball.gif').convert()
background = pygame.image.load('intro_ball.gif').convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)