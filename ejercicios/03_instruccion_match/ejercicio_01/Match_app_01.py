import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener el valor del mes seleccionado en el combobox_mes y
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’

En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_informar_on_click(self):
        meses = self.combobox_mes.get()
        mensaje = None #importante para que no me aparezca error cuando pido un valor en alert

        match meses:
            case "Enero":
                mensaje = "que comiences bien el año!!!"
            case "Marzo":
                mensaje = "a clases!!"
            case "Julio":
                mensaje = "se vienen las clases!!"
            case "Diciembre":
                mensaje = "Felices vacaciones!!!"

        if mensaje != None:
            alert("MENSAJE",mensaje)
        """
        pais = prompt("ingrese","Ingrese el pais de origen")
        informar_flag = False
        impuesto = False

        match pais:
            case "Argentina"    |   "Uruguay"   |   "Paraguay":
                impuesto = "el impuesto es 5"
                informar_flag = True
            case "Brasil":
                impuesto = 20
                informar_flag = True
            case "Chile":
                impuesto = 15
                informar_flag = True
            case "Uruguay":
                impuesto = 10
                informar_flag = True
            case "Peru":
                impuesto = 25
                informar_flag = True
            case _:
                impuesto = "no trabajamos con este pais" #esta mal preacticado la variable, pero el case _: se usa como caso por defecto

        if informar_flag:
            print(impuesto)
        """

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
