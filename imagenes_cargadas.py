import pygame
import json
from colores import *

def traer_datos():
    with open("data_preguntas.json",'r',encoding="UTF-8") as archivo:
        lista_preguntas = json.load(archivo)
        # for diccionario in archivo:
        #     data = {}
        #     data["question"] = diccionario["question"]
        #     data["rojo"] = diccionario["rojo"]
        #     data["azul"] = diccionario["azul"]
        #     data["votante_1"] = diccionario["votante_1"]
        #     data["votante_2"] = diccionario["votante_2"]
        #     data["votante_3"] = diccionario["votante_3"]
        #     data["votante_4"] = diccionario["votante_4"]
        #     data["votante_5"] = diccionario["votante_5"]
        #     data["correct_answer"] = diccionario["correct_answer"]
        #     lista_preguntas.append(data)
        return lista_preguntas



boton_azul = pygame.image.load("imagenes\\boton_azul.png")

boton_rojo = pygame.image.load("imagenes\\boton_rojo.png")

cuadro_de_texto = pygame.image.load("imagenes\cuadro_de_texto.png")

back = pygame.image.load("imagenes\\fondo_nubes.jpg")

tabla_de_puntos_imagen = pygame.image.load("imagenes\\tabla de puntos.png")

dedo = pygame.image.load("imagenes\dedo.png")

personas_imagen = pygame.image.load("imagenes\personaje.png")

game_over =  pygame.image.load("imagenes\game_over.png")
