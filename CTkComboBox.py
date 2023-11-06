from customtkinter import *

app = CTk()

app.geometry("500x400")

set_appearance_mode("light")

combobox = CTkComboBox(
    master=app,
    values=["opcion 1", "opcion 2", "opcion 3"],
    fg_color="#FBAB7E",
    border_color="#FBAB7E",
)

combobox.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
