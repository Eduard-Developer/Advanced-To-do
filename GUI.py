from tkinter import * 
import tkinter as tk
from turtle import window_width

window = Tk()
window_width = "1080"


window.title("To do liste")
documents = Text(window, fg="black")

def textFileOpen():
    file = open("app.txt", "r")
    _tasks = file.read()
    documents.insert(tk.END, _tasksTodo)

textFileOpen()


documents.pack()



window.mainloop()