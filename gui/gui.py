import tkinter as tk
from tkinter import ttk

# создание графического окна
root = tk.Tk()
# заголовок окна
root.title('Application using Tkinter')
# размеры окна, смещение от левого верхнего угла
root.geometry('700x710+500+250')
root.resizable(False, False)


def graph_window():
    win=tk.Tk()
    win.geometry("500x400+1000+250")
    win.resizable(False, False)
    return win


function_label = tk.Label(text="Function", font="Roboto 13")
function_label.place(x=200, y=20)

function_entry = tk.Entry(font="Roboto 13")
function_entry.place(x=200, y=40)

reset_btn = tk.Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13")
reset_btn.place(x=450, y=40)

inertia_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Inertia",
                         resolution=0.1)
inertia_scale.place(x=200, y=67)

local_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Local",
                       resolution=0.1)
local_scale.place(x=400, y=67)

global_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Global",
                        resolution=0.1)
global_scale.place(x=200, y=125)

stop_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Stop ratio",
                      resolution=0.1)
stop_scale.place(x=400, y=125)

canvas = tk.Canvas(bg="white", height=400, width=400)
canvas.place(x=150, y=185)

iterator_label = tk.Label(text="iterator", font="Roboto 13")
iterator_label.place(x=200, y=590)

step_entry = tk.Entry(font="Roboto 13", width=10)
step_entry.place(x=200, y=610)

step_btn = tk.Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                     width=7)
step_btn.place(x=320, y=600)

final_btn = tk.Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                      width=7)
final_btn.place(x=430, y=600)

graph_btn = tk.Button(text="function change graph", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                      command=graph_window, width=25)
graph_btn.place(x=235, y=640)


# метод, вызывающий цикл обработки событий окна для взаимодействия с пользователем
root.mainloop()