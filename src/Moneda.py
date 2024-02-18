import pygame

from .config import tamano_bloque

class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./img/coin.png')
        self.image = pygame.transform.scale(img, (tamano_bloque // 2, tamano_bloque // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)