from threading import get_ident
from tkinter import *

def calculate():
   miles_to_km = round(float(miles_entry.get()) * 1.609344)
   km_measure_label["text"] = f"{miles_to_km}"



window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width= 250, height= 150)
window.config(padx=20, pady=20)


miles_entry = Entry(width=10)
miles_entry.focus()
miles_entry.grid(column= 1, row= 0)


miles_label = Label(text= "Miles")
miles_label.grid(column= 2, row= 0)

equals_label = Label(text= "is equal to")
equals_label.grid(column= 0, row= 1)

km_measure_label = Label()
km_measure_label.grid(column= 1, row= 1)

km_unit_label = Label(text= "Km")
km_unit_label.grid(column= 2, row= 1)

convert_button = Button(text= "Calculate", command= calculate)
convert_button.grid(column= 1, row= 2)


window.mainloop()
