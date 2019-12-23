import sys
import tkinter as tk

root = tk.Tk()

root.title(u"window title")

root.geometry("400x300")

static1 = tk.Label(text=u"test", foreground="#ff69b4", background="#e0ffff")
static1.place(x=20,y=270)

root.mainloop()