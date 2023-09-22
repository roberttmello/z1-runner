import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', 72)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score = 0
score_surface = font.render(f'Score: {score}', False, '#404040')
score_rectangle = score_surface.get_rect(center=(640, 80))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 480))


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print('collision')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 480))
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
    screen.blit(score_surface, score_rectangle)
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)
    snail_rectangle.x -= 3
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 1280

    # mouse_position = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_position):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
