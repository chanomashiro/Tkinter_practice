import sys
import tkinter as tk

root = tk.Tk()

root.title(u"window title")

root.geometry("400x300")

static1 = tk.Label(text=u"entry")
static1.pack()

entry1 = tk.Entry()
entry1.insert(tk.END, u"hoge")
entry1.pack()

root.mainloop()