#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

#Application Setup
root = Toplevel()
root.geometry("600x400+450+220")
root.resizable(False,False)
root.title("Train Available (Only for Dehradun To Dehli trains)")
root.configure(bg="light green")

#Functions
def select():
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25
    global Sl1,Sl2,Sl3,Sl4,Sl5,Sl6,Sl7,Sl8,Sl9,Sl10,Sl11,Sl12,Sl13,Sl14,Sl15,Sl16,Sl17,Sl18,Sl19,Sl20,Sl21,Sl22,Sl23,Sl24,Sl25
    global Ac1,Ac2,Ac3,Ac4,Ac5,Ac6,Ac7,Ac8,Ac9,Ac10,Ac11,Ac12,Ac13,Ac14,Ac15,Ac16,Ac17,Ac18,Ac19,Ac20,Ac21,Ac22,Ac23,Ac24,Ac25

    if(cb1.get()=="Select Source" and cb2.get()=="Select Destination"):
        messagebox.showwarning("Invalid Option","Please select your source and destination")

    if((cb1.get()=="DDN" and cb2.get()=="NDLS") or (cb1.get()=="NDLS" and cb2.get()=='DDN')):
        t1 = Label(root,text="Jansatbadi Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t1.place(x=70,y=230)
        t2 = Label(root,text="Satabadi Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t2.place(x=70,y=270)
        t3 = Label(root,text="Musoorie Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t3.place(x=70,y=310)
        t4 = Label(root,text="Nanda Express",bg="light green",fg="black",font="Halvatica 10 bold") 
        t4.place(x=70,y=350)
        #####################################################################################
        Sl1 = Label(root,text="Rs 165",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl1.place(x=230,y=230)
        Sl2 = Label(root,text="Rs 980",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl2.place(x=230,y=270)
        Sl3 = Label(root,text="Rs 340",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl3.place(x=230,y=310)
        Sl4 = Label(root,text="Rs 1140",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl4.place(x=230,y=350)
        ###################################################################################
        Ac1 = Label(root,text="Rs 420",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac1.place(x=400,y=230)
        Ac2 = Label(root,text="Rs 1290",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac2.place(x=400,y=270)
        Ac3 = Label(root,text="Rs 670",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac3.place(x=400,y=310)
        Ac4 = Label(root,text="Rs 1548",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac4.place(x=400,y=350)

    if((cb1.get()=="Roorkee" or cb1.get()=="Harawala" or cb1.get()=="Haridwar") and
       cb2.get()=="NDLS" or (cb1.get()=="NDLS" and (cb2.get()=="Roorkee" or 
       cb2.get()=="Haridwar" or cb2.get()=="Harawala"))):
        t5 = Label(root,text="Jansatbadi Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t5.place(x=70,y=230)
        t6 = Label(root,text="Satabadi Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t6.place(x=70,y=270)
        ####################################################################################
        Sl5 = Label(root,text="Rs 165",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl5.place(x=230,y=230)
        Sl6 = Label(root,text="Rs 980",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl6.place(x=230,y=270)
        #####################################################################################
        Ac5 = Label(root,text="Rs 420",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac5.place(x=400,y=230)
        Ac6 = Label(root,text="Rs 1290",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac6.place(x=400,y=270)

    if((cb1.get()=="DDN" or cb1.get()=="Roorkee" or cb1.get()=="Haridwar" or 
        cb1.get()=="Harawala") and cb2.get()=="Hazrat Nizamuddin"):
        t7 = Label(root,text="Hizrat Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t7.place(x=70,y=230)
        Sl7 = Label(root,text="Rs 510",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl7.place(x=230,y=230)
        Ac7 = Label(root,text="Rs 740",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac7.place(x=400,y=230)
        #####################################################################################
        t8 = Label(root,text="Kota Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t8.place(x=70,y=270)
        Sl8 = Label(root,text="Rs 1210",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl8.place(x=230,y=270)
        Ac8 = Label(root,text="Rs 2160",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac8.place(x=400,y=270)

    if(cb1.get()=="Hazrat Nizamuddin" and (cb2.get()=="DDN" or cb2.get()=="Roorkee" or cb2.get()=="Haridwar" or cb2.get()=="Harawala")):
        t9 = Label(root,text="Dehradun Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t9.place(x=70,y=230)
        Sl9 = Label(root,text="Rs 210",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl9.place(x=230,y=230)
        Ac9 = Label(root,text="Rs 490",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac9.place(x=400,y=230)
        #####################################################################################
        t10 = Label(root,text="Kota Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t10.place(x=70,y=270)
        Sl10 = Label(root,text="Rs 1210",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl10.place(x=230,y=270)
        Ac10 = Label(root,text="Rs 2160",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac10.place(x=400,y=270)

    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Roorkee" or 
    cb1.get()=="Harawala") and cb2.get()=="Dehli Cantonment"):  
        t11 = Label(root,text="Dehli Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t11.place(x=70,y=230)
        Sl11 = Label(root,text="Rs 870",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl11.place(x=230,y=230)
        Ac11 = Label(root,text="Rs 1278",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac11.place(x=400,y=230)
        #####################################################################################
        t12 = Label(root,text="Janti Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t12.place(x=70,y=270)
        Sl12 = Label(root,text="Rs 550",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl12.place(x=230,y=270)
        Ac12 = Label(root,text="Rs 1120",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac12.place(x=400,y=270)
    if((cb1.get()=="Dehli Cantonment") and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or
    cb2.get()=="Roorkee" or cb2.get()=="Harawala")):
        t13 = Label(root,text="Dehli Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t13.place(x=70,y=230)
        Sl13 = Label(root,text="Rs 870",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl13.place(x=230,y=230)
        Ac13 = Label(root,text="Rs 1278",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac13.place(x=400,y=230)
        #####################################################################################
        t14 = Label(root,text="Janti Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t14.place(x=70,y=270)
        Sl14 = Label(root,text="Rs 550",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl14.place(x=230,y=270)
        Ac14 = Label(root,text="Rs 1120",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac14.place(x=400,y=270)
        #####################################################################################
        t15 = Label(root,text="Moto Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t15.place(x=70,y=310)
        Sl15 = Label(root,text="Rs 345",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl15.place(x=230,y=310)
        Ac15 = Label(root,text="Rs 668",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac15.place(x=400,y=310)

    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Harawala" or 
    cb1.get()=="Roorkee") and cb2.get()=="Dehli Sarai Rohilia" or ((cb1.get()=="Dehli Sarai Rohilia") and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or cb2.get()=="Roorkee" or 
    cb2.get()=="Harawala"))):
        t16 = Label(root,text="Rohilia Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t16.place(x=70,y=230)
        Sl16 = Label(root,text="Rs 765",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl16.place(x=230,y=230)
        Ac16 = Label(root,text="Rs 911",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac16.place(x=400,y=230)
        #####################################################################################
        t17 = Label(root,text="Haridwar Express",bg="light green",fg="black",font="Halvatica 10 bold")
        t17.place(x=70,y=270)
        Sl17 = Label(root,text="Rs 225",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl17.place(x=230,y=270)
        Ac17 = Label(root,text="Rs 617",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac17.place(x=400,y=270)
    
    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Harawala") and 
    (cb2.get()=="Roorkee" or cb2.get()=="Haridwar")):
        t18 = Label(root,text="Train Local-D1",bg="light green",fg="black",font="Halvatica 10 bold")
        t18.place(x=70,y=230)
        Sl18 = Label(root,text="Rs 110",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl18.place(x=230,y=230)
        Ac18 = Label(root,text="Rs 135",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac18.place(x=400,y=230)
        #####################################################################################
        t19 = Label(root,text="Train Local-D2",bg="light green",fg="black",font="Halvatica 10 bold")
        t19.place(x=70,y=270)
        Sl19 = Label(root,text="Rs 115",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl19.place(x=230,y=270)
        Ac19 = Label(root,text="Rs 155",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac19.place(x=400,y=270)

    if(cb1.get()=="Roorkee" and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or 
    cb2.get()=="Harawala")):
        t20 = Label(root,text="Train Local-R1",bg="light green",fg="black",font="Halvatica 10 bold")
        t20.place(x=70,y=230)
        Sl20 = Label(root,text="Rs 120",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl20.place(x=230,y=230)
        Ac20 = Label(root,text="Rs 142",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac20.place(x=400,y=230)
        #####################################################################################
        t21 = Label(root,text="Train Local-R2",bg="light green",fg="black",font="Halvatica 10 bold")
        t21.place(x=70,y=270)
        Sl21 = Label(root,text="Rs 90",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl21.place(x=230,y=270)
        Ac21 = Label(root,text="Rs 128",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac21.place(x=400,y=270)

    if(cb1.get()=="NDLS" and (cb2.get()=="Dehli Cantonment" or cb2.get()=="Dehli Sarai Rohilia")):
        t22 = Label(root,text="Train NDLS-D1",bg="light green",fg="black",font="Halvatica 10 bold")
        t22.place(x=70,y=230)
        Sl22 = Label(root,text="Rs 50",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl22.place(x=230,y=230)
        Ac22 = Label(root,text="Rs 112",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac22.place(x=400,y=230)
        #####################################################################################
        t23 = Label(root,text="Train NDLS-D2",bg="light green",fg="black",font="Halvatica 10 bold")
        t23.place(x=70,y=270)
        Sl23 = Label(root,text="Rs 80",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl23.place(x=230,y=270)
        Ac23 = Label(root,text="Rs 115",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac23.place(x=400,y=270)

    if((cb1.get()=="Dehli Cantonment" or cb1.get()=="Dehli Sarai Rohilia") and
       (cb2.get()=="NDLS")):
        t24 = Label(root,text="Train Dehli-R1",bg="light green",fg="black",font="Halvatica 10 bold")
        t24.place(x=70,y=230)
        Sl24 = Label(root,text="Rs 75",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl24.place(x=230,y=230)
        Ac24 = Label(root,text="Rs 148",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac24.place(x=400,y=230)
        #####################################################################################
        t25 = Label(root,text="Train Dehli-R2",bg="light green",fg="black",font="Halvatica 10 bold")
        t25.place(x=70,y=270)
        Sl25 = Label(root,text="Rs 60",bg="light green",fg="black",font="Halvatica 10 bold") 
        Sl25.place(x=230,y=270)
        Ac25 = Label(root,text="Rs 152",bg="light green",fg="black",font="Halvatica 10 bold") 
        Ac25.place(x=400,y=270)


def delete():
    if((cb1.get()=="DDN" and cb2.get()=="NDLS") or (cb1.get()=="NDLS" and cb2.get()=="DDN")):
       t1.config(text='')
       t2.config(text='')
       t3.config(text='')
       t4.config(text='')
       Sl1.config(text='')
       Sl2.config(text='')
       Sl3.config(text='')
       Sl4.config(text='')
       Ac1.config(text='')
       Ac2.config(text='')
       Ac3.config(text='')
       Ac4.config(text='')
    if((cb1.get()=="Roorkee" or cb1.get()=="Harawala" or cb1.get()=="Haridwar") and
    cb2.get()=="NDLS" or (cb1.get()=="NDLS" and (cb2.get()=="Roorkee" or 
    cb2.get()=="Haridwar" or cb2.get()=="Harawala"))):
        t5.config(text='')
        t6.config(text='')
        Sl5.config(text='')
        Sl6.config(text='')
        Ac5.config(text='')
        Ac6.config(text='')
    if((cb1.get()=="DDN" or cb1.get()=="Roorkee" or cb1.get()=="Haridwar" or 
        cb1.get()=="Harawala") and cb2.get()=="Hazrat Nizamuddin"):
        t7.config(text='')
        Sl7.config(text='')
        Ac7.config(text='')
        t8.config(text='')
        Sl8.config(text='')
        Ac8.config(text='')
    if(cb1.get()=="Hazrat Nizamuddin" and (cb2.get()=="DDN" or cb2.get()=="Roorkee" or cb2.get()=="Haridwar" or cb2.get()=="Harawala")):
        t9.config(text='')
        Sl9.config(text='')
        Ac9.config(text='')
        t10.config(text='')
        Sl10.config(text='')
        Ac10.config(text='')
    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Roorkee" or 
    cb1.get()=="Harawala") and cb2.get()=="Dehli Cantonment"):
        t11.config(text='')
        Sl11.config(text='')
        Ac11.config(text='')
        t12.config(text='')
        Sl12.config(text='')
        Ac12.config(text='')
    if((cb1.get()=="Dehli Cantonment") and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or
    cb2.get()=="Roorkee" or cb2.get()=="Harawala")):
        t13.config(text='')
        Sl13.config(text='')
        Ac13.config(text='')
        t14.config(text='')
        Sl14.config(text='')
        Ac14.config(text='')
        t15.config(text='')
        Sl15.config(text='')
        Ac15.config(text='')

    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Harawala" or 
    cb1.get()=="Roorkee") and cb2.get()=="Dehli Sarai Rohilia" or ((cb1.get()=="Dehli Sarai Rohilia") and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or cb2.get()=="Roorkee" or 
    cb2.get()=="Harawala"))):
        t16.config(text='')
        Sl16.config(text='')
        Ac16.config(text='')
        t17.config(text='')
        Sl17.config(text='')
        Ac17.config(text='')
    
    if((cb1.get()=="DDN" or cb1.get()=="Haridwar" or cb1.get()=="Harawala") and 
    (cb2.get()=="Roorkee" or cb2.get()=="Haridwar")):
        t18.config(text='')
        Sl18.config(text='')
        Ac18.config(text='')
        t19.config(text='')
        Sl19.config(text='')
        Ac19.config(text='')

    if(cb1.get()=="Roorkee" and (cb2.get()=="DDN" or cb2.get()=="Haridwar" or 
    cb2.get()=="Harawala")):
        t20.config(text='')
        Sl20.config(text='')
        Ac20.config(text='')
        t21.config(text='')
        Sl21.config(text='')
        Ac21.config(text='')

    if(cb1.get()=="NDLS" and (cb2.get()=="Dehli Cantonment" or cb2.get()=="Dehli Sarai Rohilia")):
        t22.config(text='')
        Sl22.config(text='')
        Ac22.config(text='')
        t23.config(text='')
        Sl23.config(text='')
        Ac23.config(text='')
    
    if((cb1.get()=="Dehli Cantonment" or cb1.get()=="Dehli Sarai Rohilia") and
       (cb2.get()=="NDLS")):
        t24.config(text='')
        Sl24.config(text='')
        Ac24.config(text='')
        t25.config(text='')
        Sl25.config(text='')
        Ac25.config(text='')
        

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

l4 = Label(root,text="Sleeper Quater",bg="light green",fg="black",font="Gabriola 18 bold underline")
l4.place(x=230,y=170)

l5 = Label(root,text="AC Quater",bg="light green",fg="black",font="Gabriola 18 bold underline")
l5.place(x=400,y=170)

cb2 = Combobox(f2,values=values2,state="readonly",background="light green",width=17,font="Arial 10 bold")
cb2.place(x=55,y=80); cb2.set('Select Destination');
btn1 = Button(root,text="Book Now",bg="light green",fg="dark blue",
bd=0,activebackground="light green",activeforeground="dark blue",command=book_now,cursor="hand2")
btn1.place(x=260,y=93)
btn2 = Button(root,text="Show",bg="light green",fg="dark blue",
bd=0,activebackground="light green",activeforeground="dark blue",
command=select,cursor="hand2")
btn2.place(x=270,y=60)
btn3 = Button(root,text="Delete",bg="light green",fg="dark blue",
bd=0,activebackground="light green",activeforeground="dark blue",
command=delete,cursor="hand2")
btn3.place(x=270,y=127)

root.mainloop()