import sys
import tkinter as tk

root = tk.Tk()

root.title(u"window title")

root.geometry("400x300")


def delete_entry(event):
    entry1.delete(0, tk.END)


static1 = tk.Label(text=u"entry")
static1.pack()

entry1 = tk.Entry(width=50)
entry1.insert(tk.END, u"hoge")
entry1.pack()

button1 = tk.Button(text=u"hoge button", width=50)
button1.bind("<Button-1>", delete_entry)
button1.pack()


root.mainloop()