import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

root.title(u"window title")

root.geometry("400x300")


def delete_entry(event):
    entry1.delete(0, tk.END)


def showMessege(text):
    tkm.showinfo("info", text)


static1 = tk.Label(text=u"entry")
static1.pack()

entry1 = tk.Entry(width=50)
entry1.insert(tk.END, u"hoge")
entry1.pack()

button1 = tk.Button(text=u"hoge button", width=50, command=lambda: showMessege(entry1.get()))
#button1.bind("<Button-1>", delete_entry)
button1.pack()


root.mainloop()