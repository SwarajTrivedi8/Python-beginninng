import tkinter as tk
from tkinter import filedialog

m=[]

dirpath=filedialog.askdirectory()
m.append(str(dirpath))
k=m[0]
print(k)