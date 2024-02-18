import pygame

from .config import tamano_bloque


class Salida(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./img/exit.png')
        self.image = pygame.transform.scale(img, (tamano_bloque, int(tamano_bloque * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
