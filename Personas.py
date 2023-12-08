from Objeto import *
from configuraciones import ROJO,AZUL
import pygame

class Personas(Objeto):
    def __init__(self, x, y, width, height, imagen, lista_info,que_quiero,color_cuadrado):
        super().__init__(x, y, width, height, imagen)
        self.que_quiero = que_quiero
        self.lista = lista_info
        self.color_cuadrado = color_cuadrado
        self.rectangulo_color = pygame.Rect(self.x, self.y-120, 90, 90)

    def blit_cuadrado(self,pantalla,lista_votantes):
        for votante in lista_votantes:
            pygame.draw.rect(pantalla,votante.color_cuadrado,votante.rectangulo_color)
            votante.blitear_imagen(pantalla)

