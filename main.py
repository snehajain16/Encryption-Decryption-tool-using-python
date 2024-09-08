from tkinter import*
import base64
from tkinter import messagebox

screen = Tk()
screen.geometry("420x420")
screen.title("Encrption & Decryption")
screen.configure(bg="light grey")

def encrypt():
    password=code.get()
    if password== "1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Code is Encrypted",font="impack 10 bold").place(x=0,y=0)
        text2 = Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","please enter the secret key")
    elif(password=="1234"):
        messagebox.showerror("Oops","Invalid Secret Key")


def decrypt():
    password=code.get()
    if password== "1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg="pink")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Code is Decrypted",font="impack 10 bold").place(x=5,y=6)
        text2 = Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","please enter the secret key")
    elif(password=="1234"):
        messagebox.showerror("Oops","Invalid Secret Key")


def reset():
    text1.delete(1.0,END)
    code.set("")
    


#label
Label(screen,text="Enter the Text for Encrption & Decryption", font="impack 14 bold" ).place(x=15,y=7)

#text
text1 = Text(screen,bd=4,font="20")
text1.place(x=5,y=45,width=410,height=120)

#label
Label(screen,text="Enter Secret Key", font="impack 12 bold" ).place(x=143,y=180)

#entry
code=StringVar()
entry = Entry(textvariable=code,bd=4, font="20" ,show="*").place(x=105,y=210,width=210,height=30)

#button
Button(screen,text="ENCRYPT", font="arial 16 bold",bg="green" ,fg="white", command=encrypt).place(x=15,y=280,width=180)
Button(screen,text="DECRYPT", font="arial 16 bold",bg="green" ,fg="white" , command=decrypt).place(x=230,y=280,width=180)
Button(screen,text="RESET", font="arial 16 bold",bg="red" ,fg="white" , command=reset).place(x=60,y=350,width=280)
mainloop()