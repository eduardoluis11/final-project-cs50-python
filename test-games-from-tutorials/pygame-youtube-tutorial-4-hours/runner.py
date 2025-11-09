import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# This will render the sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()   # This renders the ground
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))   # This renders the sky
    screen.blit(ground_surface, (0, 300))   # This should render the ground
    screen.blit(text_surface, (300, 50))

    # # My answer
    # if snail_x_pos > -100:  # If the snail is visible and hasn't crossed the left edge of the screen
    #     snail_x_pos -= 4    # The snail will move to the left
    # else:   # If the snail is no longer visible since it crossed the left edge of the screen
    #     snail_x_pos = 900   # The snail should teleport to the right edge of the screen

    # What the instructor did
    snail_x_pos -= 4

    if snail_x_pos < -100: snail_x_pos = 800

    screen.blit(snail_surface, (snail_x_pos, 250))  # This renders the snail

    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)

















