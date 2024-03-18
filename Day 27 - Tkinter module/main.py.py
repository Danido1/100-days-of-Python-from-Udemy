from tkinter import *

# Playground
window = Tk()
window.title("My program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="hello", font=("Arial", 24))

my_label["text"] = "New hello"  # OPTION 1
my_label.config(text="New hello")  # OPTION 2 OF DOING THE SAME
my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = input.get()  # OPTION 1
    my_label.config(text=input.get())  # OPTION 2

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1) # In order to make anything appear in screen, it needs to have some sort of layout


# Entry
input = Entry()
print(input.get)
input.grid(column=3, row=3)

new_button = Button(text="New Buttom", command=button_clicked)
new_button.grid(column=2, row=0)


















window.mainloop()