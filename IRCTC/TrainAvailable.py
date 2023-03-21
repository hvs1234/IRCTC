#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

#Application Setup
root = Tk()
root.geometry("600x400+450+220")
root.resizable(False,False)
root.title("Train Available (Only for Dehradun To Dehli trains)")
root.configure(bg="light green")

#Functions
def select():
    global t1,t2,t3,t4,Atime1,Atime2,Atime3,Atime4,Dt1,Dt2,Dt3,Dt4,t5,t6,Atime5,Atime6,Dt5,Dt6
    if(cb1.get()=="DDN" and cb2.get()=="NDLS"):
        t1 = Label(root,text="Jansatbadi Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t1.place(x=70,y=230)
        t2 = Label(root,text="Satabadi Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t2.place(x=70,y=270)
        t3 = Label(root,text="Musoorie Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t3.place(x=70,y=310)
        t4 = Label(root,text="Nanda Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t4.place(x=70,y=350)
        #####################################################################################
        Atime1 = Label(root,text="5:00 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime1.place(x=230,y=230)
        Atime2 = Label(root,text="5:00 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime2.place(x=230,y=270)
        Atime3 = Label(root,text="9:30 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime3.place(x=230,y=310)
        Atime4 = Label(root,text="11:00 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime4.place(x=230,y=350)
        ###################################################################################
        Dt1 = Label(root,text="11:05 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt1.place(x=381,y=230)
        Dt2 = Label(root,text="11:20 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt2.place(x=381,y=270)
        Dt3 = Label(root,text="6:30 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt3.place(x=381,y=310)
        Dt4 = Label(root,text="7:30 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt4.place(x=381,y=350)

    if((cb1.get()=="Roorkee" or cb1.get()=="Harawala" or cb1.get()=="Haridwar") and
       cb2.get()=="NDLS"):
        t5 = Label(root,text="Jansatbadi Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t5.place(x=70,y=230)
        t6 = Label(root,text="Satabadi Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t6.place(x=70,y=270)
        ####################################################################################
        Atime5 = Label(root,text="5:00 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime5.place(x=230,y=230)
        Atime6 = Label(root,text="5:00 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Atime6.place(x=230,y=270)
        #####################################################################################
        Dt5 = Label(root,text="11:05 AM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt5.place(x=381,y=230)
        Dt6 = Label(root,text="11:20 PM",bg="light green",fg="black",font="Halvatica 10 bold") 
        Dt6.place(x=381,y=270)

def delete(event):
    if(cb1.get()=="DDN" and cb2.get()=="NDLS"):
       t1.config(text='')
       t2.config(text='')
       t3.config(text='')
       t4.config(text='')
       Atime1.config(text='')
       Atime2.config(text='')
       Atime3.config(text='')
       Atime4.config(text='')
       Dt1.config(text='')
       Dt2.config(text='')
       Dt3.config(text='')
       Dt4.config(text='')
    if((cb1.get()=="Roorkee" or cb1.get()=="Harawala" or cb1.get()=="Haridwar") and
       cb2.get()=="NDLS"):
        t5.config(text='')
        t6.config(text='')
        Atime5.config(text='')
        Atime6.config(text='')
        Dt5.config(text='')
        Dt6.config(text='')

def book_now():
    import BookHere 

#Application Creation
values1=['DDN','Roorkee','Haridwar','Harawala','NDLS','Hazrat Nizamuddin','Dehli Cantonment','Dehli Sarai Rohilia']
values1.sort()

values2=['DDN','Roorkee','Haridwar','Harawala','NDLS','Hazrat Nizamuddin','Dehli Cantonment','Dehli Sarai Rohilia']
values2.sort()

img1 = PhotoImage(file="E:\\build app with python\\IRCTC\\train.png")
root.iconphoto(False,img1)
f1 = Frame(root,width=270,height=350,bg="light green")
f1.place(x=20,y=20)
l1 = Label(f1,text="From Station",bg="light green",fg="black",font="Gabriola 25 bold")
l1.place(x=50,y=20)
cb1 = Combobox(f1,values=values1,state="readonly",background="light green",width=17,font="Arial 10 bold")
cb1.place(x=55,y=80); cb1.set('Select Source')

f2 = Frame(root,width=270,height=350,bg="light green")
f2.place(x=320,y=20)
l2 = Label(f2,text="To Station",bg="light green",fg="black",font="Gabriola 25 bold")
l2.place(x=50,y=20)

line = Frame(root,width=800,height=2,bg="black")
line.place(x=0,y=160)

l3 = Label(root,text="Train Name",bg="light green",fg="black",font="Gabriola 18 bold underline")
l3.place(x=70,y=170)

l4 = Label(root,text="Arrival Time",bg="light green",fg="black",font="Gabriola 18 bold underline")
l4.place(x=230,y=170)

l5 = Label(root,text="Destination Time",bg="light green",fg="black",font="Gabriola 18 bold underline")
l5.place(x=380,y=170)

cb2 = Combobox(f2,values=values2,state="readonly",background="light green",width=17,font="Arial 10 bold")
cb2.place(x=55,y=80); cb2.set('Select Destination');
btn1 = Button(root,text="Book Now",bg="light green",fg="dark blue",
bd=0,activebackground="light green",activeforeground="dark blue")
btn1.place(x=260,y=100)
btn2 = Button(root,text="Show",bg="light green",fg="dark blue",
bd=0,activebackground="light green",activeforeground="dark blue",
command=select)
btn2.place(x=270,y=65)

root.bind('<Control-d>',delete)
root.mainloop()