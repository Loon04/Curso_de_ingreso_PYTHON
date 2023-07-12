import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: instrucion_if_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        numero = random.randrange(1,11)

        if numero >= 6 and numero <= 10:
            mensaje = "Promoción directa, la nota es "
        elif numero ==4 or numero == 5:
            mensaje = "Aprobado la nota es "
        elif numero <= 3 and numero >= 1:
            mensaje = "Desaprobado, la nota es "


        #alert("Notas", mensaje + str(numero))

        print(mensaje + str(numero))




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
