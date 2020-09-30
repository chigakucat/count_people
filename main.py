# _*_ coding: utf-8 _*_
import tkinter as tk

root = tk.Tk()
root.title(u"People Count")
root.geometry('400x300')
counter = 0

buttona = tk.Button(text="デクリメント", height = 5, width = 20)
buttonb = tk.Button(text="インクリメント", height = 5, width = 20)
resetButton = tk.Button(text="reset")

def clicked():
    global counter, buttona, buttonb
    counter = counter + 1

def reset():
    global counter,resetButton
    counter = 0
    buttona.config(text=str(counter))
    buttonb.config(text=str(counter))

buttona.config(command=clicked)
buttonb.config(command=clicked)
resetButton.config(command=reset)

buttona.pack()
buttonb.pack()
resetButton.pack()
buttona.mainloop()
buttonb.mainloop()
resetButton.mainloop()
