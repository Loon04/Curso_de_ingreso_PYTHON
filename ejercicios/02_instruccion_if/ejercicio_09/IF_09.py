import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Anahí Julieta
apellido: González Pineda
---
Ejercicio: instrucion_if_09
---
Al presionar el botón  'Calcular', se deberá mostrar (utilizando el Dialog alert) un número
aleatorio entre el 1 y el 10 inclusive
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

        print(numero)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
