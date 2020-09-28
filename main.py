import tkinter as tk
import sys
import tkinter.filedialog

class TkinterClass:
    def __init__():
        root = tk.Tk()
        root.option_add("*font", ('', 14))

# variable 用のオブジェクト
action = tk.IntVar()
action.set(0)
level = tk.IntVar()
level.set(1)

# ダミー
def start(): pass

# メニューバー
menubar = tk.Menu(root)
root.configure(menu = menubar)

games = tk.Menu(menubar, tearoff = False)
levels = tk.Menu(menubar, tearoff = False)
menubar.add_cascade(label="ファイル", underline = 0, menu=games)
menubar.add_cascade(label="ヘルプ", underline = 0, menu=levels)

# ファイル
games.add_command(label = "開く", underline = 0, )
games.add_command(label = "保存", underline = 0, )
games.add_command(label = "名前を付けて保存",  underline= 0, )
games.add_command(label = "exit", underline = 0, command = sys.exit)

# ヘルプ
levels.add_radiobutton(label = '使用方法', variable = level, value = 1)

# ラベル
tk.Label(root, text = "***** Menu Test *****").pack()

root.mainloop()
