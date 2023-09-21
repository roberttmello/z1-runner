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
snail_x_position = 600

while True:  # Loop principal do jogo
    for event in pygame.event.get():  # Percorre uma lista de eventos
        if event.type == pygame.QUIT:  # Se o evento for "Sair" o loop é encerrado
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 480))
    screen.blit(text_surface, (540, 120))
    screen.blit(snail_surface, (snail_x_position, 420))
    snail_x_position -= 4
    if snail_x_position <= -80:
        snail_x_position = 1280

    pygame.display.update()  # Atualiza a tela com os elementos necessários
    clock.tick(60)  # Limita o loop principal a rodar no máximo há 60 fps
