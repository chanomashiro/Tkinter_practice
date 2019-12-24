import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

root.title(u"window title")

root.geometry("400x300")


def addList(text):
    listbox1.insert(tk.END, text)


static1 = tk.Label(text=u"entry")
static1.pack()


entry1 = tk.Entry(width=50)
entry1.insert(tk.END, u"hoge")
entry1.pack()


button1 = tk.Button(text=u"hoge button", width=50, command=lambda: addList(entry1.get()))
button1.pack()


listbox1 = tk.Listbox(width=50, height=10)
listbox1.pack()



root.mainloop()