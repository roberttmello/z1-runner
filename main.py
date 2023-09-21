import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))  # Cria uma tela preta vazia (Display surface)
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/pixeltype.ttf', 72)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = font.render('Start Now!!!', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 480))


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 480))

while True:  # Loop principal do jogo
    for event in pygame.event.get():  # Percorre uma lista de eventos
        if event.type == pygame.QUIT:  # Se o evento for "Sair" o loop é encerrado
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 480))
    screen.blit(text_surface, (500, 120))
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)
    snail_rectangle.x -= 3
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 1280
    # player_rectangle.x += 3
    # if player_rectangle.left >= 1280:
    #     player_rectangle.right = 0

    pygame.display.update()  # Atualiza a tela com os elementos necessários
    clock.tick(60)  # Limita o loop principal a rodar no máximo há 60 fps
