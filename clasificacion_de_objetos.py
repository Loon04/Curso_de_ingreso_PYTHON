from Informacion import Informacion
from Tabla import Tabla
from Objeto_movimiento import Dedo
from Personas import Personas
from colores import *
from imagenes_cargadas import *
from Objeto import *


boton_azul = Informacion(550,800,250,60,boton_azul,NEGRO,traer_datos(),"azul")
boton_rojo = Informacion(1000,800,250,60,boton_rojo,NEGRO,traer_datos(),"rojo")
mostrar_preguntas = Informacion(500,600,800,100,cuadro_de_texto,NEGRO,traer_datos(),"question")

dedo_señala = Dedo(1500,918,60,40,dedo)

lista_con_botones = [boton_rojo,boton_azul]

tabla_de_puntos1 = Tabla(1580,900,200,60,tabla_de_puntos_imagen,ROJO,"$100")
tabla_de_puntos2 = Tabla(1580,860,200,60,tabla_de_puntos_imagen,ROJO,"$200")
tabla_de_puntos3 = Tabla(1580,820,200,60,tabla_de_puntos_imagen,ROJO,"$300")
tabla_de_puntos4 = Tabla(1580,780,200,60,tabla_de_puntos_imagen,ROJO,"$400")
tabla_de_puntos5 = Tabla(1580,740,200,60,tabla_de_puntos_imagen,ROJO,"$500")
tabla_de_puntos6 = Tabla(1580,700,200,60,tabla_de_puntos_imagen,ROJO,"$600")
tabla_de_puntos7 = Tabla(1580,660,200,60,tabla_de_puntos_imagen,ROJO,"$700")
tabla_de_puntos8 = Tabla(1580,620,200,60,tabla_de_puntos_imagen,ROJO,"$800")
tabla_de_puntos9 = Tabla(1580,580,200,60,tabla_de_puntos_imagen,ROJO,"$900")
tabla_de_puntos10 = Tabla(1580,540,200,60,tabla_de_puntos_imagen,ROJO,"$1000")
tabla_de_puntos11 = Tabla(1580,500,200,60,tabla_de_puntos_imagen,ROJO,"$1100")
tabla_de_puntos12 = Tabla(1580,460,200,60,tabla_de_puntos_imagen,ROJO,"$1200")
tabla_de_puntos13 = Tabla(1580,420,200,60,tabla_de_puntos_imagen,ROJO,"$1300")
tabla_de_puntos14 = Tabla(1580,380,200,60,tabla_de_puntos_imagen,ROJO,"$1400")
tabla_de_puntos15 = Tabla(1580,340,200,60,tabla_de_puntos_imagen,ROJO,"$1500")
tabla_de_puntos16 = Tabla(1580,300,200,60,tabla_de_puntos_imagen,ROJO,"$1600")
tabla_de_puntos17 = Tabla(1580,260,200,60,tabla_de_puntos_imagen,ROJO,"$1700")
tabla_de_puntos18 = Tabla(1580,220,200,60,tabla_de_puntos_imagen,ROJO,"$1800")
tabla_de_puntos19 = Tabla(1580,180,200,60,tabla_de_puntos_imagen,ROJO,"$1900")
tabla_de_puntos20 = Tabla(1580,140,200,60,tabla_de_puntos_imagen,ROJO,"$2000")

lista_tabla_puntos = [tabla_de_puntos1,tabla_de_puntos2,tabla_de_puntos3,tabla_de_puntos4,tabla_de_puntos5,
                    tabla_de_puntos6,tabla_de_puntos7,tabla_de_puntos8,tabla_de_puntos9,tabla_de_puntos10,
                    tabla_de_puntos11,tabla_de_puntos12,tabla_de_puntos13,tabla_de_puntos14,tabla_de_puntos15,
                    tabla_de_puntos16,tabla_de_puntos17,tabla_de_puntos18,tabla_de_puntos19,tabla_de_puntos20]

Boton_next = Tabla(1580,140,200,60,tabla_de_puntos_imagen,ROJO,"Next")
Boton_half = Tabla(1580,140,200,60,tabla_de_puntos_imagen,ROJO,"Half")
Boton_reload = Tabla(1580,140,200,60,tabla_de_puntos_imagen,ROJO,"Reload")

Persona1 = Personas(300,300,90,140,personas_imagen,traer_datos(),"votante_1",BLANCO)
Persona2 = Personas(560,300,90,140,personas_imagen,traer_datos(),"votante_2",BLANCO)
Persona3 = Personas(850,300,90,140,personas_imagen,traer_datos(),"votante_3",BLANCO)
Persona4 = Personas(1100,300,90,140,personas_imagen,traer_datos(),"votante_4",BLANCO)
Persona5 = Personas(1350,300,90,140,personas_imagen,traer_datos(),"votante_5",BLANCO)

lista_de_votantes = [Persona1,Persona2,Persona3,Persona4,Persona5]

