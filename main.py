import pygame
import sys
from configuraciones import *
from clasificacion_de_objetos import *



pygame.font.get_fonts()

TAMAÑO_PANTALLA = (1800,1000)

pygame.init()

#FONDO
fondo = pygame.image.load("imagenes\\fondo_nubes.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#dimensiones de la pantalla
VENTANA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("¿Esto o aquello?")


#TIPOGRAFIA
myfont = pygame.font.SysFont("Calibri", 25)



clock = pygame.time.Clock()


bandera = True

while bandera:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            sys.exit(0)

    VENTANA.blit(fondo, (0, 0))

    mostrar_preguntas.update(VENTANA,eventos,lista_con_botones,myfont,dedo_señala,lista_de_votantes)
    tabla_de_puntos1.blitear_tabla(VENTANA,lista_tabla_puntos)
    tabla_de_puntos1.render_texto_lista(myfont,VENTANA,lista_tabla_puntos)
    Persona1.blit_cuadrado(VENTANA,lista_de_votantes)


    pygame.display.update()
    clock.tick(60)



