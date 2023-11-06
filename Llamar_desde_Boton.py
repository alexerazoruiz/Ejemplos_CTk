from customtkinter import *

app = CTk()

app.geometry("500x400")
set_appearance_mode("light")


def Click_Boton():
    print("Boton presionado")


Boton = CTkButton(
    master=app,
    text="Aceptar",
    corner_radius=32,
    fg_color="#727273",
    hover_color="#ef7721",
    command=Click_Boton,  # Comando para dirigirme a la funcion Click_Boton
)

Boton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
