import pygame

from .config import tamano_bloque

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        self.image = pygame.transform.scale(img, (tamano_bloque, tamano_bloque // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
