import pygame

from .config import tamano_bloque


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, mover_x, mover_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./img/platform.png')
        self.image = pygame.transform.scale(img, (tamano_bloque, tamano_bloque // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_movimiento = 0
        self.direccion_movimiento = 1
        self.mover_x = mover_x
        self.mover_y = mover_y

    def update(self):
        self.rect.x += self.direccion_movimiento * self.mover_x
        self.rect.y += self.direccion_movimiento * self.mover_y
        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 50:
            self.direccion_movimiento *= -1
            self.contador_movimiento *= -1
