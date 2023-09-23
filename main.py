import pygame
from sys import exit


def display_score():
    current_time = (int(pygame.time.get_ticks() / 1000) - start_time)
    score_surface = font.render(f'Score:  {current_time}', False, '#404040')
    score_rectangle = score_surface.get_rect(center=(640, 80))
    screen.blit(score_surface, score_rectangle)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', 72)
game_active = True
start_time = 0
player_gravity = 0

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 480))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 480))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 480:
                    player_gravity = -25

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 480:
                    player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 1280
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 480))
        screen.blit(snail_surface, snail_rectangle)
        display_score()

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 480:
            player_rectangle.bottom = 480
        screen.blit(player_surface, player_rectangle)

        snail_rectangle.x -= 8
        if snail_rectangle.right <= 0:
            snail_rectangle.left = 1280

        # Collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill('#ffbb00')

    pygame.display.update()
    clock.tick(60)
