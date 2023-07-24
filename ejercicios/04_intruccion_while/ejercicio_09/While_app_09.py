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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera
hasta que presione el botón Cancelar (en el prompt).
Luego determinar el máximo y el mínimo
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
        master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
        master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
        master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
        columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):


        bandera_primero = 1
        bandera_segundo = 1
        while bandera_segundo == 1:
            numero = prompt("ej_9","ingrese un numero")
            if numero == None:
                bandera_segundo = 0
            if numero != None:
                numero = int(numero)
                if (bandera_primero == 1):
                    maximo = numero
                    minimo = numero
                    bandera_primero = 0
                elif numero < minimo:
                        minimo = numero
                elif numero > maximo:
                        maximo = numero


        self.txt_maximo.delete(0, "end")
        self.txt_minimo.delete(0, "end")

        if bandera_primero == 0: #si bandera_primero pasa a ser 0 singnifica que logro pasar por el tercar if, dandole a las variables validacion
            self.txt_minimo.insert(0, minimo) #si bandera_primero sigue siendo 1, if no va a mostrar lo que tiene adentro
            self.txt_maximo.insert(0, maximo)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
