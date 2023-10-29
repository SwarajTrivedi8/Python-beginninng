import os
import tkinter as tk
from tkinter import filedialog

scr=tk.Tk()
scr.geometry("400x200")

def openfile():
    dirpath=filedialog.askdirectory()
    
    print(dirpath)


bot1=tk.Button(scr,text="directory",command=openfile)
bot1.pack()

scr.mainloop()