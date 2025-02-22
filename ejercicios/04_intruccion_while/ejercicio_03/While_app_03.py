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
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt.
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_pedir_clave_on_click(self):

        contra = prompt("ej",prompt="ingrese una contraseña").lower() #el primer prompt, se ejecuta solo una vez porque esta afuerta del while
        while(contra != "utn750"):
            contra = prompt("ej",prompt="ERROR! ingrese una contraseña").lower() #el segundo prompt, esta adentro





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
