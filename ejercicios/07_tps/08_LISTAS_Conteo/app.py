import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anahí Julieta
apellido: González Pineda
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt).
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []


    def btn_comenzar_ingreso_on_click(self):
        bandera = 1

        while bandera == 1:
            numero = prompt("TP_8","Ingrese un numero")
            if numero != None:
                numero = int(numero)
                self.lista.append(numero)
            else:
                bandera = 0
    def btn_mostrar_estadisticas_on_click(self):

        suma_negativos = 0
        suma_positivos = 0
        acumulador_nrosPositivo = 0
        contador_nrosNegativo = 0
        contador_ceros = 0
        bandera_2 = 1
        minimo = 0
        maximo = 0

        for elemento in self.lista:
            if bandera_2 == 1:
                minimo = elemento
                maximo = elemento
                bandera_2 = 0
            else:
                if elemento < minimo:
                    minimo = elemento
                else:
                    if elemento > maximo:
                        maximo = elemento

            if elemento < 0:
                suma_negativos = suma_negativos + elemento
                contador_nrosNegativo += 1
            else:
                if elemento > 0:
                    suma_positivos = suma_positivos + elemento
                    acumulador_nrosPositivo += 1
                else:
                    contador_ceros += 1

        promedio_negativos = suma_negativos / contador_nrosNegativo
        print(self.lista)
        alert("TP_8", """La suma acumulada de los negativos: {0}
La suma acumulada de los positivos: {1}
Cantidad de números positivos ingresados: {2}
Cantidad de números negativos ingresados: {3}
Cantidad de ceros: {4}
El minimo de los negativos: {5}
El maximo de los positivos: {6}
El promedio de los negativos: {7}""".format(suma_negativos,suma_positivos,acumulador_nrosPositivo,contador_nrosNegativo,contador_ceros,minimo,maximo,promedio_negativos))



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
