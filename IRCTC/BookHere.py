from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Book Now")
root.resizable(False,False)
root.geometry("600x400+380+180")
root.configure(bg="light green")

img1 = PhotoImage(file="E:\\build app with python\\IRCTC\\booktrain.png")
root.iconphoto(False,img1)
name = Label(root,text="Select Train")

root.mainloop()