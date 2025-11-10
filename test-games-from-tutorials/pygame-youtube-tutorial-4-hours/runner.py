import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# This will render the sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()  # This renders the ground
score_surf = test_font.render('My game', False, (64, 64, 64))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# snail_x_pos = 600   # Initial position for the snail

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))  # Rectangle for the player

# Rectangle for the Snail
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

# Rectangle for the text / score
score_rect = score_surf.get_rect(center=(400, 50))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # My answer (DIDN'T WORK)
        # if event.type == pygame.MOUSEMOTION:  # If the player moves the mouse
        #     if player_rect.collidepoint(event.pos) and pygame.mouse.get_pressed():  # If the user touches the player  with the mouse
        #
        #         # The player will jump
        #         player_gravity = -20
        #
        #         # # If the user clicks their mouse
        #         # if :
        #         # print('collision')

        # Instructor's answer
        if event.type == pygame.MOUSEBUTTONDOWN:  # If the player clicks their mouse

            # If the user touches the player with the mouse
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:

                player_gravity = -20    # The player will jump

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:  # If the player hits the Space Bar

                player_gravity = -20    # This makes the player jump

                # # My answer: This adds an extra condition that makes the player jump ONLY once, and only if they
                # # are touching the ground.
                # if player_rect.y == 216:
                #
                #     # This makes the player jump
                #     player_gravity = -20

        if event.type == pygame.KEYUP:
            print('key up')

        # # DEBUG: This prints the Y position of the player.
        # # Prints "216"
        # print(player_rect.y)

    screen.blit(sky_surface, (0, 0))  # This renders the sky
    screen.blit(ground_surface, (0, 300))  # This should render the ground
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

    screen.blit(score_surf, score_rect)

    # # This draws a line (source: https://www.pygame.org/docs/ref/draw.html#pygame.draw.line) (my answer)
    # pygame.draw.line(sky_surface, 'Yellow', (0, 0), (800, 400))

    # # This draws a line (INSTRUCTOR'S ANSWER)
    # pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10)

    # # My answer
    # if snail_x_pos > -100:  # If the snail is visible and hasn't crossed the left edge of the screen
    #     snail_x_pos -= 4    # The snail will move to the left
    # else:   # If the snail is no longer visible since it crossed the left edge of the screen
    #     snail_x_pos = 900   # The snail should teleport to the right edge of the screen

    # This makes the snail move by using its rectangle's X coordinate
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800

    # This renders the snail by using a rectangle, not by inserting X and Y positions individually
    screen.blit(snail_surf, snail_rect)

    # Player
    player_gravity += 1
    # Instructor's answer
    # This makes the player fall by using gravity. I will change his Y coordinate.
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf, player_rect)

    # # My answer
    # # This makes the player fall by using gravity. I will change his Y coordinate.
    # player_rect.y = player_gravity

    pygame.display.update()
    clock.tick(60)
