import pygame
from Objeto import Objeto
from colores import ROJO,AZUL,BLANCO,NEGRO

iteracion = 0
desplazar_dedo = False

class Informacion(Objeto):
    def __init__(self, x, y, width, height, imagen, color_texto, lista_info, que_quiero:str):
        super().__init__(x, y, width, height, imagen)
        self.color_texto = color_texto
        self.lista = lista_info
        self.que_quiero = que_quiero
        self.mostrar_colores = False

    def render_lista(self,pantalla,font,iteracion):
        texto = font.render(self.lista[iteracion][self.que_quiero],True,self.color_texto)
        pantalla.blit(texto, ((self.x )+(self.width-texto.get_width())/2, self.y+(self.height-texto.get_height())/2))


    def update(self,pantalla,lista_eventos,lista_con_botones,font,dedo,lista_votantes):
        if self.estado_del_juego(font,pantalla) == True:
            for evento in lista_eventos:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if lista_con_botones[1].rectangulo_principal.collidepoint(evento.pos):
                            lista_con_botones[1].validacion_respuesta("azul")

                        elif lista_con_botones[0].rectangulo_principal.collidepoint(evento.pos):
                            lista_con_botones[0].validacion_respuesta("rojo")
            try:
                self.mover_dedo(dedo,pantalla)
                self.cambiar_color(lista_votantes)
                self.prueba(pantalla,lista_con_botones,font)
                self.blitear_imagen(pantalla)
                self.render_lista(pantalla,font,iteracion)
            except IndexError:
                self.fin_del_juego(pantalla)
                self.guardar_puntos()
        else:
            self.fin_del_juego(pantalla)
            self.guardar_puntos()

    def prueba(self,pantalla,lista_de_objetos,font):
        for boton in lista_de_objetos:
            try:
                boton.blitear_imagen(pantalla)
                boton.render_lista(pantalla,font,iteracion)
                boton.activar_posicion_boton()
            except:
                pass

    def activar_posicion_boton(self):
        if self.rectangulo_principal.collidepoint(pygame.mouse.get_pos()):
            self.color_texto = BLANCO
        else:
            self.color_texto = NEGRO

    def validacion_respuesta(self,que_quiero):
        global desplazar_dedo
        global iteracion
        if self.lista[iteracion]["correct_answer"] == self.lista[iteracion][que_quiero]:
            iteracion += 1
            desplazar_dedo = True
            self.puntos += 100 #problema
        else:
            self.estado_juego = False
        return self.estado_juego
    #externo

    def mover_dedo(self,dedo,pantalla):
        global desplazar_dedo
        try:
            dedo.desplazamiento_y(pantalla,desplazar_dedo)
            desplazar_dedo = False
        except AttributeError:
            print("nofu")

    def obtener_data(self,lista_votantes):
        global iteracion

        for votante in lista_votantes:
            if votante.lista[iteracion][votante.que_quiero] == 1 :
                votante.color_cuadrado = ROJO
            elif votante.lista[iteracion][votante.que_quiero] == 0:
                votante.color_cuadrado = AZUL

    def cambiar_color(self,lista_votantes):
        if self.true() == True:
            self.obtener_data(lista_votantes)
        else:
            pass

    def true(self):
        return True

    def obtener_puntos(self):
        return self.puntos

    def guardar_puntos(self):
        if self.estado_juego == False:
            pass
            #print(self.obtener_puntos())
