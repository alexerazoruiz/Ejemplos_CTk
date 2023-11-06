from customtkinter import *

app = CTk()
app.geometry("500x400")


texto = CTkLabel(
    master=app,
    text="Aqui escribe cualquier texto",
    font=("Arial", 20),
    text_color="#727273",
)


texto.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()
