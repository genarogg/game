import pygame

from .Enemigo import Enemigo
from .Salida import Salida
from .Moneda import Moneda
from .Plataforma import Plataforma
from .Lava import Lava
from .config import tamano_bloque
from .config import grupo_blobs
from .config import grupo_plataformas
from .config import grupo_lava
from .config import grupo_monedas
from .config import grupo_salida
from .config import pantalla

class Mundo():
    def __init__(self, data):
        self.lista_bloques = []

        # Carga las imágenes
        img_suelo = pygame.image.load('./img/dirt.png')
        img_pasto = pygame.image.load('./img/grass.png')

        contador_fila = 0
        for fila in data:
            contador_columna = 0
            for bloque in fila:
                if bloque == 1:
                    img = pygame.transform.scale(img_suelo, (tamano_bloque, tamano_bloque))
                    rect_img = img.get_rect()
                    rect_img.x = contador_columna * tamano_bloque
                    rect_img.y = contador_fila * tamano_bloque
                    bloque = (img, rect_img)
                    self.lista_bloques.append(bloque)
                if bloque == 2:
                    img = pygame.transform.scale(img_pasto, (tamano_bloque, tamano_bloque))
                    rect_img = img.get_rect()
                    rect_img.x = contador_columna * tamano_bloque
                    rect_img.y = contador_fila * tamano_bloque
                    bloque = (img, rect_img)
                    self.lista_bloques.append(bloque)
                if bloque == 3:
                    blob = Enemigo(contador_columna * tamano_bloque, contador_fila * tamano_bloque + 15)
                    grupo_blobs.add(blob)
                if bloque == 4:
                    plataforma = Plataforma(contador_columna * tamano_bloque, contador_fila * tamano_bloque, 1, 0)
                    grupo_plataformas.add(plataforma)
                if bloque == 5:
                    plataforma = Plataforma(contador_columna * tamano_bloque, contador_fila * tamano_bloque, 0, 1)
                    grupo_plataformas.add(plataforma)
                if bloque == 6:
                    lava = Lava(contador_columna * tamano_bloque, contador_fila * tamano_bloque + (tamano_bloque // 2))
                    grupo_lava.add(lava)
                if bloque == 7:
                    moneda = Moneda(contador_columna * tamano_bloque + (tamano_bloque // 2), contador_fila * tamano_bloque + (tamano_bloque // 2))
                    grupo_monedas.add(moneda)
                if bloque == 8:
                    salida = Salida(contador_columna * tamano_bloque, contador_fila * tamano_bloque - (tamano_bloque // 2))
                    grupo_salida.add(salida)
                contador_columna += 1
            contador_fila += 1

    def dibujar(self):
        for bloque in self.lista_bloques:
            pantalla.blit(bloque[0], bloque[1])

