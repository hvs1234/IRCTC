#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import ast

#Application Setup
root = Tk()
root.title("IRCTC Login")
root.configure(bg="light blue")
root.geometry("910x480+300+200")
root.resizable(False,False)

#Functions
def on_enter1(event):
    user.delete(0,'end')

def on_enter2(event):
    password.delete(0,'end')
    password.config(show="*")

def on_leave1(event):
    a = user.get()
    if(a==''): 
        user.insert(0,"Username")

def on_leave2(event):
    b = password.get()
    if(b==''):
        password.insert(0,"Password")
        password.config(show='')

def sign_in():
    Username = user.get()
    Password = password.get()

    if((Username=='Username' and Password=='Password') or (Username=='' and password=='')):
        messagebox.showwarning("Blank Input","Please enter username and password")
    elif(Username=='' and Username=='Username'):
        messagebox.showwarning("Blank Username","Enter your username")
    elif(Password=='' and Password=='Password'):
        messagebox.showwarning("Blank Username","Enter your password")
    elif(Username=="IRCTC" and Password=="h1234"):
        messagebox.showinfo("Login Success","You have logged in successfully")
        # root.destroy()
        # import TrainAvailable
    elif(Username!="IRCTC"): messagebox.showerror("Error","Invalid username")
    elif(Password!="h1234"): messagebox.showerror("Error","Invalid password")
    else:
        messagebox.showerror("Invalid Input","Invalid username and password")

def show():
    password.config(show='')

def hide():
    password.config(show="*")

#Application Creation
img1 = PhotoImage(file="E:\\build app with python\\IRCTC\\irctc.png")
img2 = PhotoImage(file="E:\\build app with python\\IRCTC\\login person.png")
root.iconphoto(False,img1)
l1 = Label(root,image=img2,bg="light blue") ; l1.place(x=50,y=50)

f1 = Frame(root,width=350,height=350,bg="light blue") ; f1.place(x=480,y=70)

head = Label(f1,text="Sign In",fg="dark blue",bg="light blue",font=('Microsoft',23,'bold'))
head.place(x=100,y=5) 

user = Entry(f1,width=25,fg="black",bd=0,bg="light blue",font=("Microsoft",12),relief=RAISED) ; user.insert(0,"Username"); user.bind('<FocusIn>',on_enter1);
user.bind('<FocusOut>',on_leave1) ; user.place(x=30,y=80)

password = Entry(f1,width=25,fg="black",bd=0,bg="light blue",
font=("Microsoft",12),relief=RAISED) ; password.insert(0,"Password")
password.bind('<FocusIn>',on_enter2); password.bind('<FocusOut>',on_leave2)
password.place(x=30,y=150);

f2 = Frame(root,width=295,height=2,bg="black").place(x=510,y=180)
f3 = Frame(root,width=295,height=2,bg="black").place(x=510,y=250)

btn1 = Button(f1,text="Sign In",bg="#57a1f8",fg="black",bd=2,cursor="hand2"
,activebackground="#57a1f8",activeforeground="black",
width=39,pady=7,relief=RAISED,command=sign_in)
btn1.place(x=35,y=228)

btn2 = Button(f1,text="Show",bd=0,fg="dark blue",bg="light blue",cursor="hand2",
activebackground="light blue",activeforeground="dark blue",command=show)
btn2.place(x=230,y=150)
btn2 = Button(f1,text="Hide",bd=0,fg="dark blue",bg="light blue",cursor="hand2",
activebackground="light blue",activeforeground="dark blue",command=hide)
btn2.place(x=290,y=150)

root.mainloop()