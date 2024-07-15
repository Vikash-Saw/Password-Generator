from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.insert(0, random.sample(small_alphabets, password_length))

    if choice.get() == 2:
        passwordField.insert(0, random.sample(small_alphabets + capital_alphabets, password_length))

    if choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.title("Password Generator")
root.geometry("350x350")
root.resizable(False, False)
root.config(bg='steel blue')
choice = IntVar()
Font = ('arial', 16, 'bold')

# Icon
image_icon = PhotoImage(file="lock.png")
root.iconphoto(False, image_icon)

name_label = Label(root, text="Password Generator", font=("impact", 30),bg='black', fg='white')
name_label.place(x=0, y=0, height=60, width=350)

weak_radioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weak_radioButton.place(x=10, y=80)

medium_radioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
medium_radioButton.place(x=115, y=80)

strong_radioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strong_radioButton.place(x=240, y=80)

lengthLabel = Label(root, text='Password Length', font=('arial', 15, 'bold'), bg='steel blue',fg='black')
lengthLabel.place(x=40, y=140)

length_Box = Spinbox(root, from_=5, to=15, width=4, font=Font)
length_Box.place(x=220, y=140)

generateButton = Button(root, text='Generate', font=Font, bg="red3", command=generator)
generateButton.place(x=110, y=200)

passwordField = Entry(root, width=25, bd=5, font=Font)
passwordField.place(x=15, y=255)

copyButton = Button(root, text=' Copy', width=10, height=1, font=("arial 10 bold"), bg="#1f6c68", fg="white", command=copy)
copyButton.place(x=120, y=300)

root.mainloop()
