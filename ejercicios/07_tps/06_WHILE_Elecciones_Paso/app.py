'''
nombre: Anahí Julieta
apellido: González Pineda
---
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = 1
        flag_votos = 1
        maximo = 0
        minimo = 0
        suma_edad = 0
        contador_edad = 0
        suma_votos = 0

        while flag == 1:
            nombre = prompt("TP_6_WHILE","Ingrese el nombre del candidato")
            while nombre == None or nombre == "":
                nombre = prompt("TP_6_WHILE","Ingrese el nombre del candidato")
            edad = prompt("TP_6_WHILE","Ingrese la edad del candidato")
            while edad == None or edad =="" or int(edad) < 25:
                edad = prompt("TP_6_WHILE","Ingrese una edad valida")
            votos = prompt("TP_6_WHILE","Ingrese la cantidad de votos")
            while votos == None or votos == "" or int(votos) < 0:
                votos = prompt("TP_6_WHILE","Ingrese una cantidad de votos valida")

            votos =int(votos)
            suma_edad = suma_edad + int(edad)
            contador_edad += 1
            if votos != None:
                    suma_votos = suma_votos + votos
                    if flag_votos == 1:
                        maximo = votos
                        minimo = votos
                        flag_votos = 0
                    else:
                        if maximo > votos:
                            maximo = votos
                        else:
                            if minimo < votos:
                                maximo = votos
            if maximo == votos:
                nombre_max = nombre
            if minimo == votos:
                nombre_min = nombre
                edad_min = edad
            contador_edad
            if contador_edad > 2:
                flag = 0

        promedio_edad = suma_edad / contador_edad
        print("""Candidato con más votos: {0}
Promedio de edades: {1}
Total de votos emitidos: {2}
Nombre del canditado con menos votos: {3}  edad: {4}""".format(nombre_max,promedio_edad,suma_votos,nombre_min,edad_min))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
