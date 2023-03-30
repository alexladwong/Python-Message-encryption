from tkinter import *
import pybase64
from tkinter import messagebox

master = Tk()

master.title('ladwongcyberdev.dev-Encrypt/Decrypt')
master.geometry("500x400")
p1 = PhotoImage(file = 'encryption.png')

# Setting icon of master window
master.iconphoto(False, p1)




# Function
def clear():
    my_text.delete(1.0, END)
    my_entry.delete(0, END)


def encrypt():
    secret = my_text.get(1.0, END)
    my_text.delete(1.0, END)

    if my_entry.get() == "Alpha":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        my_text.insert(END, secret)
    else:
        messagebox.showwarning("Incorrect", "Incorrect Password, Try Again!!!")


def decrypt():
    secret = my_text.get(1.0, END)
    my_text.delete(1.0, END)

    if my_entry.get() == "Alpha":

        secret = secret.encode("ascii")
        secret = pybase64.b64decode(secret)
        secret = secret.decode("ascii")
        my_text.insert(END, secret)
    else:
        messagebox.showwarning("Incorrect", "Incorrect Password, Try Again!!!")


# Frame
my_frame = Frame(master)
my_frame.pack(pady=20)

# Buttons
enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1, padx=20)

clear_button = Button(my_frame, text="Terminate", font=("Helvetica", 18), command=clear)
clear_button.grid(row=0, column=2)

# Label
enc_label = Label(master, text="Encrypt/Decrypt Text...", font=("Helvetica", 14))
enc_label.pack()

# Text Input Field
my_text = Text(master, width=58, height=12)
my_text.pack(pady=10)

password_label = Label(master, text="Enter Your Password in the box below", font=("Helvetica", 14))
password_label.pack()

my_entry = Entry(master, font=("helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)

master.mainloop()
