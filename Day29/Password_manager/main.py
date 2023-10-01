from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for x in range(randint(8, 10))]
    password_symbols = [choice(symbols) for y in range(randint(2, 4))]
    password_numbers = [choice(numbers) for z in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    if "" in (website, login, password):
        messagebox.showerror(title="OOps", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nLogin: {login}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {login} | {password}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
login_entry = Entry(width=52)
login_entry.grid(column=1, row=2, columnspan=2)
login_entry.insert(0, "matiberx@gmail.com")
password_entry = Entry(width=52)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
