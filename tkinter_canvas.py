import sys
import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()

root.title(u"hoge")

root.geometry("400x300")


canvas = tk.Canvas(root, width=400, height=300)
canvas.place(x=0, y=0)


root.mainloop()