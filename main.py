import webbrowser
import tkinter as tk
import tkinter.font as tkFont
from contextlib import contextmanager
import sys, os

chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=594
        height=359
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_349=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_349["font"] = ft
        GLabel_349["fg"] = "#333333"
        GLabel_349["justify"] = "center"
        GLabel_349["text"] = "text"
        GLabel_349["relief"] = "raised"
        GLabel_349.place(x=0,y=150,width=600,height=33)

        GButton_83=tk.Button(root)
        GButton_83["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_83["font"] = ft
        GButton_83["fg"] = "#000000"
        GButton_83["justify"] = "center"
        GButton_83["text"] = "Buscar"
        GButton_83.place(x=30,y=230,width=70,height=25)
        GButton_83["command"] = self.GButton_83_command

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "Cerrar"
        GButton_59.place(x=260,y=230,width=70,height=25)
        GButton_59["command"] = root.quit

        GButton_109=tk.Button(root)
        GButton_109["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_109["font"] = ft
        GButton_109["fg"] = "#000000"
        GButton_109["justify"] = "center"
        GButton_109["text"] = "Button"
        GButton_109.place(x=490,y=230,width=70,height=25)
        GButton_109["command"] = self.GButton_109_command

    def GButton_83_command(self):
        """webbrowser.get(chromepath).open('google.com')"""
        webbrowser.open('google.com')

    def GButton_59_command(self):
        root.quit

    def GButton_109_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

