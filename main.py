from tkinter import *
from tkinter import messagebox
import json
# messagebox bukan class, jadinya harus spesifik
# json.dump -> write
# json.load -> read
# json.update -> update

# ---------------------------- SEARCH DATA ---------------------------- #

def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        pass

    else:
        website = website_entry.get()
        if not website in data:
            messagebox.showinfo(title="Oops", message=f"There are no {website} data here")
        else:
            username = data[website]["email/username"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email/Username: {username}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------ #

def generate_pass():
    import random
    import pyperclip

    password_entry.delete(0, END)

    character = str("")
    rand_length = random.randint(8, 16)

    for _ in range(rand_length):
        rand_char = random.randint(32, 126)
        character += chr(rand_char)

    password_entry.insert(0, character)
    pyperclip.copy(character)
    ## modul baru

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email/username": username,
            "password": password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left anyu fields empty.")

    else:
        try:
            with open(file="data.json", mode="r") as file:
                # json.dump(new_data, file, indent=4) #json.dump -> dump data nya ke file tertentu dengan indent (spasi) tertentu
                data = json.load(file) # ini artinya baca dari file json yang diatas
                # print(data)

                # jangan nambahin manual kayak bikin dict baru lagi, mending update
                data.update(new_data)
                # misalnya datanya itu aslinya Amazon, user@gmail.com, 12345678
                # trus kita masukin lagi Amazon, username@gmail.com, 456789012

        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
                # ini kalo misalnya kagak ada file data.json nya

        else:
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
                # ini kalo mau update
                # baru ditulis lagi, di dump lagi yang udah di update

        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #
 
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

#label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entry
## sticky itu maksudnya mau nempel kemana, E itu east, W itu west

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

## focus itu untuk biar kalo launch apk nya, langsung ke entry tersebut, tinggal type aja

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(END, "user@gmail.com")

## END itu tkinter constant, biar paling akhir gitu dari indexnya string, bisa juga pake 0 sih

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

#button
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")

genpass_button = Button(text="Generate Password", command=generate_pass)
genpass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()