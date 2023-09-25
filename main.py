import pygame
from sys import exit
from random import randint

WIDTH = 1280
HEIGHT = 720


def display_score():
    current_time = (int(pygame.time.get_ticks() / 1000) - start_time)
    score_surface = font.render(f'Score:  {current_time}', False, '#444444')
    score_rectangle = score_surface.get_rect(center=(WIDTH/2, 80))
    screen.blit(score_surface, score_rectangle)
    return current_time


def enemies_movement(enemies_rect_list):
    if enemies_rect_list:
        for enemy_rect in enemies_rect_list:
            enemy_rect.x -= 10
            screen.blit(snail_surface, enemy_rect)
        # Deleting enemies that are off-screen.
        enemies_rect_list = [enemy for enemy in enemies_rect_list if enemy.x > -100]
        return enemies_rect_list
    else:
        return []


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', 64)
game_active = False
start_time = 0
player_gravity = 0
score = 0

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Enemies
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 480))

enemies_rectangle_list = []


# Player
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(120, 480))

# Intro screen
player_stand_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 3)
player_stand_surface_rectangle = player_stand_surface.get_rect(center=(WIDTH/2, 360))

game_name_surface = font.render('Z1 RUNNER', False, '#66ccaa')
game_name_surface_rectangle = game_name_surface.get_rect(center=(WIDTH/2, 180))

game_message_surface = font.render(f'Press "SPACE" to run', False, '#66ccaa')
game_message_surface_rectangle = game_message_surface.get_rect(center=(WIDTH/2, 580))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

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

            if event.type == obstacle_timer:
                enemies_rectangle_list.append(snail_surface.get_rect(midbottom=(randint(1380, 1680), 480)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = WIDTH
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 480))
        screen.blit(snail_surface, snail_rectangle)
        score = display_score()

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 480:
            player_rectangle.bottom = 480
        screen.blit(player_surface, player_rectangle)

        # Enemies movement
        enemies_rectangle_list = enemies_movement(enemies_rectangle_list)

        # Collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill('#5588aa')
        screen.blit(player_stand_surface, player_stand_surface_rectangle)

        score_message_surface = font.render(f'Your score: {score}', False, '#66ccaa')
        score_message_surface_rectangle = score_message_surface.get_rect(center=(WIDTH/2, 580))
        screen.blit(game_name_surface, game_name_surface_rectangle)

        if score == 0:
            screen.blit(game_message_surface, game_message_surface_rectangle)
        else:
            game_message_surface = font.render(f'Press "SPACE" to restart', False, '#66ccaa')
            game_message_surface_rectangle = game_message_surface.get_rect(center=(WIDTH/2, 660))
            screen.blit(score_message_surface, score_message_surface_rectangle)
            screen.blit(game_message_surface, game_message_surface_rectangle)

    pygame.display.update()
    clock.tick(60)
