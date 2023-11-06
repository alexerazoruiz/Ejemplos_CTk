from customtkinter import *

app = CTk()

app.geometry("500x400")

set_appearance_mode("light")

Entrada = CTkEntry(
    master=app,
    placeholder_text="Empieza a escribir...",
    width=300,
    text_color="#727273",
)

Entrada.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
