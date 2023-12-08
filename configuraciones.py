
import random
import pygame

def numero_random (lista:list):
    largo = len(lista)
    numero = random.randint(0,largo-1)
    return numero

def aplicar_bandera(lista:list):
    for dic in lista:
        bandera = False
        dic["bandera"] = bandera

def reescalar_imagenes(lista_animaciones,ancho,alto):
    for i in range(len(lista_animaciones)):
        imagen = lista_animaciones[i]
        lista_animaciones[i] = pygame.transform.scale(imagen,(ancho,alto))

BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
ROJO = (255, 0, 0)
AZUL = (0,0,255)




