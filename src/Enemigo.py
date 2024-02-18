import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion_movimiento = 1
        self.contador_movimiento = 0

    def update(self):
        self.rect.x += self.direccion_movimiento
        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 50:
            self.direccion_movimiento *= -1
            self.contador_movimiento *= -1

