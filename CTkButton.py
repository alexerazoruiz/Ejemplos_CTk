from customtkinter import *

app = CTk()

app.geometry("500x400")

set_appearance_mode("light")

Boton = CTkButton(
    master=app,
    text="Aceptar",
    corner_radius=32,
    fg_color="#727273",
    hover_color="#ef7721",
)

Boton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
