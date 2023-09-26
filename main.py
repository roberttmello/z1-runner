import pygame
from sys import exit
from random import randint

WIDTH = 1920
HEIGHT = 1080


def display_score():
    current_time = (int(pygame.time.get_ticks() / 1000) - start_time)
    score_surface = font.render(f'Score:  {current_time}', False, '#444444')
    score_rectangle = score_surface.get_rect(center=(WIDTH/2, int(11.11 * HEIGHT / 100)))
    screen.blit(score_surface, score_rectangle)
    return current_time


def enemies_movement(enemies_rect):
    if enemies_rect:
        for enemy_rect in enemies_rect:
            enemy_rect.x -= 8

            if enemy_rect.bottom == int(66.67 * HEIGHT / 100):
                screen.blit(snail_surface, enemy_rect)
            else:
                screen.blit(fly_surface, enemy_rect)

        # Deleting enemies that are off-screen.
        enemies_rect = [enemy for enemy in enemies_rect if enemy.x > -100]
        return enemies_rect
    else:
        return []


def collisions(player, enemies_rect):
    if enemies_rect:
        for enemy_rectangle in enemies_rect:
            if player.colliderect(enemy_rectangle):
                return False
    return True


def player_animation():
    global player_surface, player_index
    if player_rectangle.bottom < int(66.67 * HEIGHT / 100):
        player_surface = player_jump
    else:
        player_index += 0.15
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', 64)
game_active = False
start_time = 0
score = 0

# Load scene images
if WIDTH == 1280:
    sky_surface = pygame.image.load('graphics/sky-width_1280.png').convert()
    ground_surface = pygame.image.load('graphics/ground-width_1280.png').convert()

else:
    sky_surface = pygame.image.load('graphics/sky-width_1920.png').convert()
    ground_surface = pygame.image.load('graphics/ground-width_1920.png').convert()

# ENEMIES
# Snail
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# Fly
fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

enemies_rectangle_list = []

# Player
player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/player_jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom=(120, int(66.67 * HEIGHT / 100)))
player_gravity = 0

# Intro screen
player_stand_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 3)
player_stand_surface_rectangle = player_stand_surface.get_rect(center=(WIDTH/2, HEIGHT/2))

game_name_surface = font.render('Z1 RUNNER', False, '#66ccaa')
game_name_surface_rectangle = game_name_surface.get_rect(center=(WIDTH/2, int(25 * HEIGHT / 100)))

game_message_surface = font.render(f'Press  "SPACE"  to  START  or  "ESC"  to  exit!', False, '#66ccaa')
game_message_surface_rectangle = game_message_surface.get_rect(center=(WIDTH/2, int(80.56 * HEIGHT / 100)))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= int(66.67 * HEIGHT / 100):
                    player_gravity = -25

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= int(66.67 * HEIGHT / 100):
                    player_gravity = -25

            if event.type == obstacle_timer:
                if randint(0, 2):
                    enemies_rectangle_list.append(snail_surface.get_rect(
                        midbottom=(randint(WIDTH + 100, WIDTH + 400), int(66.67 * HEIGHT / 100))))
                else:
                    enemies_rectangle_list.append(fly_surface.get_rect(
                        midbottom=(randint(WIDTH + 100, WIDTH + 400), int(54.17 * HEIGHT / 100))))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, int(66.67 * HEIGHT / 100)))
        score = display_score()

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= int(66.67 * HEIGHT / 100):
            player_rectangle.bottom = int(66.67 * HEIGHT / 100)
        player_animation()
        screen.blit(player_surface, player_rectangle)

        # Enemies movement
        enemies_rectangle_list = enemies_movement(enemies_rectangle_list)

        # Collision
        game_active = collisions(player_rectangle, enemies_rectangle_list)

    else:
        screen.fill('#5588aa')
        screen.blit(player_stand_surface, player_stand_surface_rectangle)
        enemies_rectangle_list.clear()
        player_rectangle.midbottom = (int(9.375 * WIDTH / 100), int(66.67 * HEIGHT / 100))
        player_gravity = 0

        score_message_surface = font.render(f'Your score: {score}', False, '#66ccaa')
        score_message_surface_rectangle = score_message_surface.get_rect(center=(WIDTH/2, int(80.56 * HEIGHT / 100)))
        screen.blit(game_name_surface, game_name_surface_rectangle)

        if score == 0:
            screen.blit(game_message_surface, game_message_surface_rectangle)
        else:
            game_message_surface = font.render(f'Press  "SPACE"  to  RESTART  or  "ESC"  to  exit!', False, '#66ccaa')
            game_message_surface_rectangle = game_message_surface.get_rect(center=(WIDTH/2, int(91.67 * HEIGHT / 100)))
            screen.blit(score_message_surface, score_message_surface_rectangle)
            screen.blit(game_message_surface, game_message_surface_rectangle)

    pygame.display.update()
    clock.tick(60)
