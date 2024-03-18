from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.minsize(width=200, height=100)

# Labels
miles_label = Label(text="Millas", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="es igual a", font=("Arial", 10, "bold"))
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km", font=("Arial", 10, "bold"))
kilometer_label.grid(column=2, row=1)

# Entry
miles_input = Entry()
miles_input.grid(column=1, row=0)

kilometer_result_label = Label()
kilometer_result_label.grid(column=1, row=1)


def calculate():
    miles = float(miles_input.get())
    km = (miles * 1.609).__round__()
    kilometer_result_label.config(text=f"{km}", font=("Arial", 10, "bold"))

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



windows.mainloop()
