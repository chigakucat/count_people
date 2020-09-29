# _*_ coding: utf-8 _*_
import tkinter as tk

root = tk.Tk()
root.title(u"People Count")
root.geometry('400x300')
counter = 0


button = tk.Button(text="インクリメント", height = 5, width = 20)
resetButton = tk.Button(text="reset")

def clicked():
    global counter, button
    counter = counter + 1

def reset():
    global counter,resetButton
    counter = 0
    button.config(text=str(counter))

button.config(command=clicked)
resetButton.config(command=reset)

button.pack()
resetButton.pack()
button.mainloop()
resetButton.mainloop()
