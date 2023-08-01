'''
nombre: Anahí Julieta
apellido: González Pineda
---
Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera (se limita a 1 perrito por ingreso), se les pide:
nombre, precio de la consulta (validar entre 500 y 2500$) raza: (validar entre caniche, ovejero, siberiano), edad (validar 0 a 15) y peso (entre 25 y 40 kilos) determinar:

el nombre y el peso del perro con más peso
el porcentaje de razas
la facturación en bruto de la veterinaria
si la facturación en bruto supera los 5000$, hay que restarle un 21% de impuesto por ingresos brutos
'''
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Pedir Datos", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=6, pady=20, columnspan=2, sticky="nsew")
        self.lista_de_raza = []
        self.lista_de_nombre = []
        self.lista_peso = []
        self.lista_precio = []
        self.lista_de_edad = []

    def btn_validar_on_click(self):

        nombre_perro = prompt("TP_V","Ingrese un nombre")
        while nombre_perro == None or nombre_perro == "":
            nombre_perro = prompt("TP_V","Error, ingrese un nombre")
        self.lista_de_nombre.append(nombre_perro)

        precio_consulta = prompt("TP_V","Ingrese el precio de la consulta")
        while precio_consulta == None or int(precio_consulta) < 500 or int(precio_consulta) > 2500:
            precio_consulta = prompt("TP_V","intentelo de nuevo, ingrese el precio de la consulta")
        precio_consulta = int(precio_consulta)
        self.lista_precio.append(precio_consulta)

        raza_perro = prompt("TP_V", "ingrese la raza del perro")
        while raza_perro == None or (raza_perro != "caniche" and raza_perro != "ovejero" and raza_perro != "siberiano"):
            raza_perro = prompt("TP_V", "intentelo de nuevo, ingrese la raza del perro")
        self.lista_de_raza.append(raza_perro)

        edad_perro = prompt("TP_V", "Ingrese edad del perro")
        while edad_perro == None or int(edad_perro) < 0 or int(edad_perro) > 15:
            edad_perro = prompt("TP_V", "intentelo de nuevo, ingrese edad del perro")
        edad_perro = int(edad_perro)
        self.lista_de_edad.append(edad_perro)

        peso_perro = prompt("TP_V", "Ingrese el peso del perro")
        while peso_perro == None or int(peso_perro) < 25 or int(peso_perro) > 40:
            peso_perro = prompt("TP_V", "intentelo de nuevo, ingrese el peso del perro")
        peso_perro = int(peso_perro)
        self.lista_peso.append(peso_perro)

    def btn_mostrar_on_click(self):

        largo = len(self.lista_de_nombre)
        peso_max_perro = 0
        nombre_peso_max_perro = ""
        suma_facturacion = 0
        for i in range(largo):
            if peso_max_perro < self.lista_peso[i]:  #le asignamos un nuevo valor a peso_max_perro pasa por la lista_peso buscando el numero más grande
                peso_max_perro = self.lista_peso[i]
                nombre_peso_max_perro = self.lista_de_nombre[i]

            cantidad_siberiano = self.lista_de_raza.count("siberiano") #The count() method returns the number of elements with the specified value.
            cantidad_caniche = self.lista_de_raza.count("caniche")
            cantidad_ovejero = self.lista_de_raza.count("ovejero")

            suma_facturacion = suma_facturacion + self.lista_precio[i]

        if suma_facturacion > 5000:
            suma_facturacion = suma_facturacion * 0.71

        if cantidad_caniche > 0:
            cantidad_caniche = (cantidad_caniche * 100) / largo
        if cantidad_ovejero > 0:
            cantidad_ovejero = (cantidad_ovejero * 100) / largo
        if cantidad_siberiano > 0:
            cantidad_siberiano = (cantidad_siberiano * 100) / largo


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
