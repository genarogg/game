import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

reloj = pygame.time.Clock()
fps = 60

ancho_pantalla = 1000
alto_pantalla = 1000

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Plataformas')


# Define la fuente
fuente = pygame.font.SysFont('Bauhaus 93', 70)
fuente_puntaje = pygame.font.SysFont('Bauhaus 93', 30)


# Define las variables del juego
tamano_bloque = 50
fin_juego = 0
menu_principal = True
nivel = 3
max_niveles = 7
puntaje = 0


# Define los colores
blanco = (255, 255, 255)
azul = (0, 0, 255)


# Carga las imágenes
img_sol = pygame.image.load('img/sun.png')
img_fondo = pygame.image.load('img/sky.png')
img_reiniciar = pygame.image.load('img/restart_btn.png')
img_inicio = pygame.image.load('img/start_btn.png')
img_salir = pygame.image.load('img/exit_btn.png')

# Carga los sonidos
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
fx_moneda = pygame.mixer.Sound('img/coin.wav')
fx_moneda.set_volume(0.5)
fx_salto = pygame.mixer.Sound('img/jump.wav')
fx_salto.set_volume(0.5)
fx_fin_juego = pygame.mixer.Sound('img/game_over.wav')
fx_fin_juego.set_volume(0.5)


def dibujar_texto(texto, fuente, color_texto, x, y):
    img = fuente.render(texto, True, color_texto)
    pantalla.blit(img, (x, y))


# Función para reiniciar el nivel
def reiniciar_nivel(nivel):
    jugador.reiniciar(100, alto_pantalla - 130)
    grupo_blobs.empty()
    grupo_plataformas.empty()
    grupo_monedas.empty()
    grupo_lava.empty()
    grupo_salida.empty()

    # Carga los datos del nivel y crea el mundo
    if path.exists(f'level{nivel}_data'):
        pickle_in = open(f'level{nivel}_data', 'rb')
        datos_mundo = pickle.load(pickle_in)
    mundo = Mundo(datos_mundo)
    # Crea una moneda ficticia para mostrar el puntaje
    moneda_puntaje = Moneda(tamano_bloque // 2, tamano_bloque // 2)
    grupo_monedas.add(moneda_puntaje)
    return mundo


class Boton():
    def __init__(self, x, y, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clickeado = False

    def dibujar(self):
        accion = False

        # Obtiene la posición del ratón
        pos = pygame.mouse.get_pos()

        # Verifica las condiciones de paso del ratón y clickeo
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clickeado:
                accion = True
                self.clickeado = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clickeado = False

        # Dibuja el botón
        pantalla.blit(self.imagen, self.rect)

        return accion




import pygame

from src.Enemigo import Enemigo
from src.Salida import Salida
from src.Moneda import Moneda
from src.Plataforma import Plataforma
from src.Lava import Lava
from src.config import tamano_bloque
from src.config import grupo_blobs
from src.config import grupo_plataformas
from src.config import grupo_lava
from src.config import grupo_monedas
from src.config import grupo_salida
from src.config import pantalla

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





jugador = Jugador(100, alto_pantalla - 130)

grupo_blobs = pygame.sprite.Group()
grupo_plataformas = pygame.sprite.Group()
grupo_lava = pygame.sprite.Group()
grupo_monedas = pygame.sprite.Group()
grupo_salida = pygame.sprite.Group()

# Crea una moneda ficticia para mostrar el puntaje
moneda_puntaje = Moneda(tamano_bloque // 2, tamano_bloque // 2)
grupo_monedas.add(moneda_puntaje)

# Carga los datos del nivel y crea el mundo
if path.exists(f'level{nivel}_data'):
    pickle_in = open(f'level{nivel}_data', 'rb')
    datos_mundo = pickle.load(pickle_in)
mundo = Mundo(datos_mundo)


# Crea los botones
boton_reiniciar = Boton(ancho_pantalla // 2 - 50, alto_pantalla // 2 + 100, img_reiniciar)
boton_inicio = Boton(ancho_pantalla // 2 - 350, alto_pantalla // 2, img_inicio)
boton_salir = Boton(ancho_pantalla // 2 + 150, alto_pantalla // 2, img_salir)


corriendo = True
while corriendo:

    reloj.tick(fps)

    pantalla.blit(img_fondo, (0, 0))
    pantalla.blit(img_sol, (100, 100))

    if menu_principal:
        if boton_salir.dibujar():
            corriendo = False
        if boton_inicio.dibujar():
            menu_principal = False
    else:
        mundo.dibujar()

        if fin_juego == 0:
            grupo_blobs.update()
            grupo_plataformas.update()
            # Actualiza el puntaje
            # Verifica si se ha recogido una moneda
            if pygame.sprite.spritecollide(jugador, grupo_monedas, True):
                puntaje += 1
                fx_moneda.play()
            dibujar_texto('X ' + str(puntaje), fuente_puntaje, blanco, tamano_bloque - 10, 10)
        
        grupo_blobs.draw(pantalla)
        grupo_plataformas.draw(pantalla)
        grupo_lava.draw(pantalla)
        grupo_monedas.draw(pantalla)
        grupo_salida.draw(pantalla)

        fin_juego = jugador.actualizar(fin_juego)

        # Si el jugador ha muerto
        if fin_juego == -1:
            if boton_reiniciar.dibujar():
                datos_mundo = []
                mundo = reiniciar_nivel(nivel)
                fin_juego = 0
                puntaje = 0

        # Si el jugador ha completado el nivel
        if fin_juego == 1:
            # Reinicia el juego y pasa al siguiente nivel
            nivel += 1
            if nivel <= max_niveles:
                # Reinicia el nivel
                datos_mundo = []
                mundo = reiniciar_nivel(nivel)
                fin_juego = 0
            else:
                dibujar_texto('¡GANASTE!', fuente, azul, (ancho_pantalla // 2) - 140, alto_pantalla // 2)
                if boton_reiniciar.dibujar():
                    nivel = 1
                    # Reinicia el nivel
                    datos_mundo = []
                    mundo = reiniciar_nivel(nivel)
                    fin_juego = 0
                    puntaje = 0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pygame.display.update()

pygame.quit()
