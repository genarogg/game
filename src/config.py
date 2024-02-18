import pygame


tamano_bloque = 50

ancho_pantalla = 1000
alto_pantalla = 1000

grupo_blobs = pygame.sprite.Group()
grupo_plataformas = pygame.sprite.Group()
grupo_lava = pygame.sprite.Group()
grupo_monedas = pygame.sprite.Group()
grupo_salida = pygame.sprite.Group()

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

fx_salto = pygame.mixer.Sound('img/jump.wav')

mundo = Mundo(datos_mundo)