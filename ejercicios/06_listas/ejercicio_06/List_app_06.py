import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anahí Julieta
apellido: González Pineda
---
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        contador = 0
        for i in self.lista_datos:
            contador = contador + i
            lista = len(self.lista_datos)
        resultado = contador / lista
        alert("ej_6","El promedio es: "+str (resultado))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
