from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno,showerror, showwarning, showinfo
win = Tk()
passd = StringVar()
def admin():
    label = ttk.Label(win,text="пароль для admin:").pack()
    passworda = ttk.Entry(textvariable=passd,foreground="green").pack()
    pot = ttk.Button(win,text="Enter",command=passp).pack()
def passp():
    if passd.get() == "0968":
        wos = Tk()
        labs = ttk.Label(wos,text="password user[08567]").pack()
    elif passd.get() != "0968":
        showerror(message="неверный пароль!")
age = ["user","admin"]
combobox = ttk.Combobox(values=age).pack(padx=100,pady=100)
next = ttk.Button(text="next",command=admin).pack()
win.mainloop()