import pygame
from imagenes_cargadas import game_over

class Objeto():
    def __init__(self, x, y, width, height, imagen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imagen = imagen
        self.imagen_reescalda = pygame.transform.scale(self.imagen,(self.width,self.height))
        self.rectangulo_principal = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clock = pygame.time.Clock()
        self.click = pygame.time.get_ticks()
        self.contador_inicial = 15
        self.estado_juego = True
        self.desplazar_dedo = False
        self.puntos = 0

    def blitear_imagen(self,pantalla):
        pantalla.blit(self.imagen_reescalda,self.rectangulo_principal)

    def render_texto(self,font,pantalla):
        texto = font.render(self.texto,True,self.color_texto)
        pantalla.blit(texto, ((self.x )+(self.width-texto.get_width())/2, self.y+(self.height-texto.get_height())/2))

    def tiempo(self):
        self.seconds= (pygame.time.get_ticks())/1000
        self.seconds_ahora = self.contador_inicial - int(self.seconds)
        return self.seconds_ahora

    def comprovacion_tiempo(self,font,pantalla):
        self.seconds_ahora = self.tiempo()
        if self.seconds_ahora <= 0:

            self.estado_juego = False
            self.seconds_ahora = 0
        else:
            self.estado_juego = True

        tiempo = font.render(str(self.seconds_ahora),True,self.color_texto)
        pantalla.blit(tiempo,(1670,70))

        return self.estado_juego

    def estado_del_juego(self,font,pantalla):
        if self.comprovacion_tiempo(font,pantalla) == False:
            self.fin_del_juego(pantalla)
            return False
        else:
            return True

    def fin_del_juego(self,pantalla):
        game_over_ob = Objeto(500,450,700,500,game_over)
        pantalla.blit(game_over_ob.imagen_reescalda,game_over_ob.rectangulo_principal)

