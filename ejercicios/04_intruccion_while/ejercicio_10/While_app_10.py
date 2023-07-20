import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario
quiera hasta que presione el botón Cancelar (en el prompt).
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        suma_acumulada_negativo = 0
        suma_acumulada_positivo = 0
        contador_negativo = 0
        contador_positivo = 0
        contador_cero = 0
        bandera = True

        while bandera:
            numero = prompt("ej_10","ingrese un número")
            if numero == None:
                bandera = False
            if numero != None:
                numero = int(numero)
                if numero < 0:
                    suma_acumulada_negativo = suma_acumulada_negativo + numero
                    contador_negativo += 1
                elif numero > 0:
                    suma_acumulada_positivo = suma_acumulada_positivo + numero
                    contador_positivo += 1
                else:
                    contador_cero += 1

        if contador_positivo < contador_negativo:
            cantidad_diferencia = contador_negativo - contador_positivo
        else:
            cantidad_diferencia = contador_positivo - contador_negativo
        alert("ej_10", """La suma acumulada de los negativos: {0}
Suma acumulada de los positivos: {1}
Contador de negativos: {2}
Contador de positivos: {3}
Contador de ceros: {4}
Diferencia {5} """.format(suma_acumulada_negativo,suma_acumulada_positivo,contador_negativo,contador_positivo,contador_cero,cantidad_diferencia ))




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
