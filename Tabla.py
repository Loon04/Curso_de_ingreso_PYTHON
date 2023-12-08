import pygame
from Objeto import Objeto

class Tabla(Objeto):
    def __init__(self, x, y, width, height, imagen,color_texto, texto):
        self.color_texto = color_texto
        self.texto = texto
        super().__init__(x, y, width, height, imagen)

    def blitear_tabla(self, pantalla, lista_plataformas):
        for plataforma in lista_plataformas:
            plataforma_rec = pygame.Rect(plataforma.x, plataforma.y, plataforma.width, plataforma.height)
            plataforma_ima = pygame.transform.scale(plataforma.imagen,(plataforma.width,plataforma.height))
            pantalla.blit(plataforma_ima,plataforma_rec)

    def render_texto_lista(self, font, pantalla,lista_plataforma):
        for platafroma in lista_plataforma:
            texto = font.render(platafroma.texto,True,self.color_texto)
            pantalla.blit(texto, ((platafroma.x )+(platafroma.width-texto.get_width())/2, platafroma.y+(platafroma.height-texto.get_height())/2))

