import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anahí Julieta
apellido: González Pineda
---
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        numero = int(prompt("ej_8","ingrese un numero"))
        for i in range(1,numero):
            if numero%i == 0:
                mensaje = "es primo"
        print(i)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
