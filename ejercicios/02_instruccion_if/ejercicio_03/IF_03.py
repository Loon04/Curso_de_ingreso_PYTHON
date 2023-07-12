import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anahí Julieta
apellido: González Pineda
---
Ejercicio: instrucion_if_03
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, transformarlo en número
y calcular si es o no mayor de edad, si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR” en
ambos casos utilizando el Dialog Alert.
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
        if edad > 18:
            mensaje = "MAYOR"
        else:
            mensaje = "MENOR"
        alert("Edad",mensaje)
        pass


        #pais = "china"

        #if pais == "china":
        #    mensaje = "debera pagar un 10% de impuestos"
        #else:
        #    if pais == "eeuu":
        #        mensaje = "debera pagar un 20% de impuestos"
        #    else:
        #        #que no es de china y tampoco de eeuu
        #        if pais == "brasil":
        #            mensaje = "debera pagar el 5% de impuestos"
        #        else:
        #            mensaje = "no trabajamos con ese pais"


        #if pais == "china":
        #    mensaje = "debera pagar un 10% de impuestos"
        #elif pais == "eeuu":
        #        mensaje = "debera pagar un 20% de impuestos"
        #        #que no es de china y tampoco de eeuu
        #elif pais == "brasil":
        #            mensaje = "debera pagar el 5% de impuestos"
        #else:
        #    mensaje = "no trabajamos con ese pais"






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
