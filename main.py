import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))  # Cria uma tela preta vazia (Display surface)
pygame.display.set_caption("Z1 RUNNER")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/pixeltype.ttf', 72)

sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('Start Now!!!', False, 'black')

while True:  # Loop principal do jogo
    for event in pygame.event.get():  # Percorre uma lista de eventos
        if event.type == pygame.QUIT:  # Se o evento for "Sair" o loop é encerrado
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 480))
    screen.blit(text_surface, (540, 120))

    pygame.display.update()  # Atualiza a tela com os elementos necessários
    clock.tick(60)  # Limita o loop principal a rodar no máximo há 60 fps
