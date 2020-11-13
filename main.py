from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import Checkbutton
top= Tk()
top.title("choose name")
top.geometry("500x500")
top.configure(background="purple")
def submit_command():
    info=""
    if dog_var.get():
        info+= "You have selected a dog!\n"
    if cat_var.get():
        info += "You have selected a cat!\n"
    if bird_var.get():
        info += "You have selected a bird!\n"
    if info =="":
        info= "You didnt choose anything"
    messagebox.showinfo("chosen pet", info)

submit_button = Button(top, text="submit",command=submit_command)

dog_var= BooleanVar()
cat_var= BooleanVar()
bird_var= BooleanVar()

dog_cb = Checkbutton(top, text="Dog", variable=dog_var,onvalue=True,offvalue=False,height=2,width=20)
cat_cb = Checkbutton(top, text="Cat", variable=cat_var,onvalue=True,offvalue=False,height=2,width=20)
bird_cb = Checkbutton(top, text="Bird", variable=bird_var,onvalue=True,offvalue=False,height=2,width=20)
dog_cb.pack()
cat_cb.pack()
bird_cb.pack()
submit_button.pack()






top.mainloop()