#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

#Applcation Setup
root = Toplevel()
root.title("Book Now")
root.resizable(False,False)
root.geometry("600x400+380+180")
root.configure(bg="light green")

#Functions
values1 = ['Jansatabdi Express','Satabadi Express','Kota Express','Janti Express','Dehli Express','Rohilia Express','Haridwar Express','Moto Express','Dehradun Express','Hizrat Express','Musoorie Express','Nanda Express','--------------','Train Local-D1','Train Local-D2','Train Local-R1','Train Local-R2','Train NDLS-D1','Train NDLS-D2']

values4 = ['Sleeper Quater','AC Quater']

def details(): 
    import PassengerDetails

def confirm():
    from PassengerDetails import name_entry,age_entry,gender_entry,phone_entry,book_date_entry
    x1 = name_entry.get()
    x2 = age_entry.get()
    x3 = phone_entry.get()
    x4 = gender_entry.get()
    x5 = book_date_entry.get()

    if(x1=='' and (x2=='0' or x2=='') and (x3=='0' or x3=='') and x4=='' and 
    (x5=='dd/mm/yyyy' or x5=='')):
        messagebox.showwarning("Blank Detail","First to fill your details")
    if(x1=='' or (x2=='0' or x2=='') or (x3=='0' or x3=='') or x4=='' or 
    (x5=='dd/mm/yyyy' or x5=='')):
        messagebox.showwarning("Blank Detail","First to fill your details")
    else: 
        messagebox.showinfo("Confirmation","Now you can enjoy your jounrey")

#Application Creation
img1 = PhotoImage(file="E:\\build app with python\\IRCTC\\booktrain.png")
root.iconphoto(False,img1)

header = Label(root,text="🚇 IRCTC BOOKING 🚇",font="Algerian 20 bold",fg="white",bg="black",
width=100,height=2) ; header.pack()

details = Button(root,text="Before Confirmation, Please make sure that you have entered passengers detail.",bg="light green",fg="dark blue",bd=0,activebackground="light green",activeforeground="dark blue",command=details,cursor="hand2")
details.place(x=105,y=90)

name = Label(root,text="👉   Train Name:",font="Gabriola 25 bold",bg="light green",
fg="black") ; name.place(x=30,y=120)
source = Label(root,text="👉   Select Source:",font="Gabriola 25 bold",bg="light green",
fg="black") ; source.place(x=30,y=180)
destination = Label(root,text="👉   Select Destination:",font="Gabriola 25 bold",bg="light green",
fg="black") ; destination.place(x=30,y=240)
train_type = Label(root,text="👉   Select Train Type:",font="Gabriola 25 bold",bg="light green",
fg="black") ; train_type.place(x=30,y=300)

cb1 = Combobox(root,values=values1,width=42,height=10,state="readonly"); cb1.place(x=260,y=145) ; cb1.set("Select Train")
cb2 = Combobox(root,values=values1,width=40,height=10,state="readonly"); cb2.place(x=275,y=205) ; cb2.set("Source")
cb3 = Combobox(root,values=values1,width=31,height=8,state="readonly"); cb3.place(x=330,y=265) ; cb3.set("Destination")
cb4 = Combobox(root,values=values4,width=31,state="readonly"); cb4.place(x=330,y=325)
cb4.set("Train Type")

confirm = Button(root,text="Confirmation",bg="light green",fg="dark blue",bd=0,
command=confirm,activebackground="light green",activeforeground="dark blue")
confirm.place(x=400,y=362)

root.mainloop()