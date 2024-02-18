import pygame

from .config import  fx_salto
from mi_modulo import mundo

class Jugador():
    def __init__(self, x, y):
        self.reiniciar(x, y)

    def actualizar(self, fin_juego):
        dx = 0
        dy = 0
        enfriamiento_caminar = 5
        umbral_colision = 20

        if fin_juego == 0:
            # Obtiene las teclas presionadas
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_SPACE] and not self.saltando and not self.en_aire:
                fx_salto.play()
                self.vel_y = -15
                self.saltando = True
            if not tecla[pygame.K_SPACE]:
                self.saltando = False
            if tecla[pygame.K_LEFT]:
                dx -= 5
                self.contador += 1
                self.direccion = -1
            if tecla[pygame.K_RIGHT]:
                dx += 5
                self.contador += 1
                self.direccion = 1
            if not tecla[pygame.K_LEFT] and not tecla[pygame.K_RIGHT]:
                self.contador = 0
                self.indice = 0
                if self.direccion == 1:
                    self.imagen = self.imagenes_derecha[self.indice]
                if self.direccion == -1:
                    self.imagen = self.imagenes_izquierda[self.indice]

            # Maneja la animación
            if self.contador > enfriamiento_caminar:
                self.contador = 0
                self.indice += 1
                if self.indice >= len(self.imagenes_derecha):
                    self.indice = 0
                if self.direccion == 1:
                    self.imagen = self.imagenes_derecha[self.indice]
                if self.direccion == -1:
                    self.imagen = self.imagenes_izquierda[self.indice]

            # Agrega gravedad
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Verifica colisiones
            self.en_aire = True
            for bloque in mundo.lista_bloques:
                # Verifica colisión en dirección x
                if bloque[1].colliderect(self.rect.x + dx, self.rect.y, self.ancho, self.alto):
                    dx = 0
                # Verifica colisión en dirección y
                if bloque[1].colliderect(self.rect.x, self.rect.y + dy, self.ancho, self.alto):
                    # Verifica si está debajo del suelo, es decir, saltando
                    if self.vel_y < 0:
                        dy = bloque[1].bottom - self.rect.top
                        self.vel_y = 0
                    # Verifica si está encima del suelo, es decir, cayendo
                    elif self.vel_y >= 0:
                        dy = bloque[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.en_aire = False

            # Verifica colisión con enemigos
            if pygame.sprite.spritecollide(self, grupo_blobs, False):
                fin_juego = -1
                fx_fin_juego.play()

            # Verifica colisión con lava
            if pygame.sprite.spritecollide(self, grupo_lava, False):
                fin_juego = -1
                fx_fin_juego.play()

            # Verifica colisión con la salida
            if pygame.sprite.spritecollide(self, grupo_salida, False):
                fin_juego = 1

            # Verifica colisión con plataformas
            for plataforma in grupo_plataformas:
                # Colisión en dirección x
                if plataforma.rect.colliderect(self.rect.x + dx, self.rect.y, self.ancho, self.alto):
                    dx = 0
                # Colisión en dirección y
                if plataforma.rect.colliderect(self.rect.x, self.rect.y + dy, self.ancho, self.alto):
                    # Verifica si está debajo de la plataforma
                    if abs((self.rect.top + dy) - plataforma.rect.bottom) < umbral_colision:
                        self.vel_y = 0
                        dy = plataforma.rect.bottom - self.rect.top
                    # Verifica si está encima de la plataforma
                    elif abs((self.rect.bottom + dy) - plataforma.rect.top) < umbral_colision:
                        self.rect.bottom = plataforma.rect.top - 1
                        self.en_aire = False
                        dy = 0
                    # Se mueve lateralmente con la plataforma
                    if plataforma.mover_x != 0:
                        self.rect.x += plataforma.direccion_movimiento

            # Actualiza las coordenadas del jugador
            self.rect.x += dx
            self.rect.y += dy

        elif fin_juego == -1:
            self.imagen = self.imagen_muerto
            dibujar_texto('¡FIN DEL JUEGO!', fuente, azul, (ancho_pantalla // 2) - 200, alto_pantalla // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        # Dibuja al jugador en la pantalla
        pantalla.blit(self.imagen, self.rect)

        return fin_juego

    def reiniciar(self, x, y):
        self.imagenes_derecha = []
        self.imagenes_izquierda = []
        self.indice = 0
        self.contador = 0
        for num in range(1, 5):
            img_derecha = pygame.image.load(f'img/guy{num}.png')
            img_derecha = pygame.transform.scale(img_derecha, (40, 80))
            img_izquierda = pygame.transform.flip(img_derecha, True, False)
            self.imagenes_derecha.append(img_derecha)
            self.imagenes_izquierda.append(img_izquierda)
        self.imagen_muerto = pygame.image.load('img/ghost.png')
        self.imagen = self.imagenes_derecha[self.indice]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()
        self.vel_y = 0
        self.saltando = False
        self.direccion = 0
        self.en_aire = True
