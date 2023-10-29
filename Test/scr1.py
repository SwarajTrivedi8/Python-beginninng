import tkinter as tk
import ttkbootstrap as ttk

screen=tk.Tk()
screen.geometry("400x100")
screen.config(bg="White")


labl=tk.Label(master=screen,text="Change Unit From Cm to M",fg="black",font="poppins",bg="white")
labl.pack()

def conv1():
    if len(ent1.get())==0:
        labl1.config(text="ERROR")
    else:
        g=ent1.get()
        k=int(g)
        res=k/100
        labl1.config(text=res)

ent1=tk.Entry(screen)
ent1.pack(side="right",anchor="ne")


bot1=tk.Button(screen,text="OK",command=conv1)
bot1.pack(side="right",anchor="ne")

labl1=tk.Label(screen,fg="black",font="poppins")
labl1.pack()







screen.mainloop()