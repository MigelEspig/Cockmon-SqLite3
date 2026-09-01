import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))

back_color = (135, 206, 235)
ground = (34, 139, 34)

pikachu_image = pygame.image.load("./Sprites/pikachuTeste.PNG").convert_alpha()
pikachu_image = pygame.transform.flip(pikachu_image, True, False)  # espelha horizontalmente
pikachu_image = pygame.transform.rotozoom(pikachu_image, 0, 0.25)
pikachu_position = pikachu_image.get_rect()
pikachu_position.center = (135, 125)

bulbassaur_image = pygame.image.load("./Sprites/back_bulbassaur.webp").convert_alpha()
bulbassaur_image = pygame.transform.flip(bulbassaur_image, True, False)  # espelha horizontalmente
bulbassaur_image = pygame.transform.rotozoom(bulbassaur_image, 0, 0.2)
bulbassaur_position = bulbassaur_image.get_rect()
bulbassaur_position.center = (650, 420)

working = True

while working:
    screen.fill(back_color)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:


            # Verificação provisória de troca de cor do fundo
            if event.key == pygame.K_SPACE:
                back_color = (30, 144, 255)

    # Molde de chão para os CockMon
    ground_01 = (450, 400, 380, 190)

    ground_02 = (30, 100, 250, 130)

    # Desenhar o chão para ambos os CockMon
    pygame.draw.ellipse(screen, ground, ground_01)
    pygame.draw.ellipse(screen, ground, ground_02)

    screen.blit(pikachu_image, pikachu_position)
    screen.blit(bulbassaur_image, bulbassaur_position)


    pygame.display.flip()
pygame.quit()
