from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    print(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(message="Please don´t leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title=website, message=(f'Email :{data[website]["email"]}\n'
                                                            f'Password: {data[website]["password"]}'))

            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
# Creation of window tab
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="light blue")

#
canvas = Canvas(width=200, height=200, bg="lightblue", highlightthickness=0)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:", bg="light blue", fg="black", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg="light blue", fg="black", font=("Arial", 12, "bold"))
user_label.grid(column=0, row=2
                )
password_label = Label(text="Password:",bg="light blue", fg="black", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()


user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "danivicalvaro@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# BUTTONS
generate_password_button = Button(text="Generate Password", bg="light blue", fg="black", font=("Arial", 12, "bold"),
                                  highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, bg="light blue", fg="black", font=("Arial", 12, "bold"), highlightthickness=0,
                    command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", bg="light blue", fg="black", font=("Arial", 12, "bold"), highlightthickness=0,
                       command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
