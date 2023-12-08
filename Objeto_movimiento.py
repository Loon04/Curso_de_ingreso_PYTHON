from Objeto import Objeto

class Dedo(Objeto):
    def __init__(self, x, y, width, height, imagen):
        super().__init__(x, y, width, height, imagen)

    def desplazamiento_y(self,pantalla,desplazar_dedo):
        self.blitear_imagen(pantalla)
        if desplazar_dedo == True:
            self.rectangulo_principal.y -= 40
