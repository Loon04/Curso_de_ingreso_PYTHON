import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: instrucion_if_06
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad,
transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente
(edad entre 10 y 12 años) o adolescente (edad entre 13 y 17 años inclusive) de edad,
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad = int(self.txt_edad.get())

        if edad < 9:
            mensaje = "Es menor de edad"
        elif edad >= 10 and edad <= 12:
            mensaje = "Es pre-adolescente"
        elif edad >= 13 and edad <= 17:
            mensaje = "Es adolescente"

        alert("informacion",mensaje)






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
