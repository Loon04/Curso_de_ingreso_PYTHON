import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anahí Julieta
apellido: González Pineda
---
A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con
 algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5).
    Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico 1 i
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea
    # 7) - tipo de los pokemones del tipo que menos pokemones posea
    # 8) - el promedio de poder de todos los ingresados i
    # 9) - el promedio de poder de todos los poquemones de Electrico

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []


    def btn_cargar_on_click(self):
        bandera = 1
        contador_vueltas = 0
        while bandera == 1:
            nombre_pokemon = prompt("TP_V","Ingrese un nombre")
            while nombre_pokemon == None or nombre_pokemon == "":
                nombre_pokemon = prompt("TP_V","Error, ingrese un nombre")
            self.lista_nombre.append(nombre_pokemon)

            poder_pokemon = prompt("TP_V","Ingrese el poder numerico del pokemon")
            while poder_pokemon == None or int(poder_pokemon) < 50 or int(poder_pokemon) > 200:
                poder_pokemon = prompt("TP_V","intentelo de nuevo, ingrese el poder numerico del pokemon")
            poder_pokemon = int(poder_pokemon)
            self.lista_poder.append(poder_pokemon)

            elemento_pokemon = prompt("TP_V", "ingrese el elemento del pokemon")
            while elemento_pokemon == None or (elemento_pokemon != "agua" and elemento_pokemon != "tierra" and elemento_pokemon != "Psiquico" and elemento_pokemon != "fuego" and elemento_pokemon !="electrico"):
                elemento_pokemon = prompt("TP_V", "intentelo de nuevo, ingrese el elemento del pokemon")
            self.lista_tipo.append(elemento_pokemon)

            contador_vueltas += 1
            if contador_vueltas > 1:
                bandera = 0
        print(self.lista_tipo)
        print(self.lista_nombre)
        print(self.lista_poder)

    def btn_mostrar_on_click(self):
        largo = len(self.lista_nombre)
        poder_maximo = 0
        for i in range(largo):
            if "fuego" == self.lista_tipo[i] or "agua" == self.lista_tipo[i]:
                if poder_maximo < self.lista_poder[i]:
                    poder_maximo = self.lista_poder[i]
                    tipo_elemento = self.lista_tipo[i]
                    nombre = self.lista_nombre[i]
                    poder = self.lista_poder[i]
            else:
                mensaje = "No hay tipo agua o fuego"

        mensaje = "Nombre del pokemon: {0}\n Poder del pokemon: {1}\n Tipo de pokemon: {2}".format(nombre,poder,tipo_elemento)
        alert("tipo",mensaje)
        #no se como poner un mensaje de "error no hay agua o fuego"

    def btn_informar_on_click(self):
        cantidad_pokemones_electrico = self.lista_tipo.count("electrico")

        largo_dos = len(self.lista_poder)

        poder_total = 0
        for i in self.lista_poder:
            poder_total = poder_total + i
        promedio = poder_total / largo_dos
        alert("e","Promedio del total de poderes: {0}\nCantidad de pokemones electricos: {1}".format(promedio, cantidad_pokemones_electrico))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
