import tkinter as tk
from tkinter import ttk

# создание графического окна
root = tk.Tk()
# заголовок окна
root.title('Application using Tkinter')
# размеры окна, смещение от левого верхнего угла
root.geometry('500x510+500+250')
root.resizable(False, False)


def graph_window():
    win=tk.Tk()
    win.geometry("400x300+1000+250")
    win.resizable(False, False)
    return win


function_label = tk.Label(text="Function", font="Roboto 13")
function_label.place(x=100, y=10)

function_entry = tk.Entry(font="Roboto 13")
function_entry.place(x=100, y=30)

reset_btn = tk.Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13")
reset_btn.place(x=350, y=20)

canvas = tk.Canvas(bg="white", height=300, width=300)
canvas.place(x=100, y=100)

iterator_label = tk.Label(text="iterator", font="Roboto 13")
iterator_label.place(x=100, y=410)

step_entry = tk.Entry(font="Roboto 13", width=10)
step_entry.place(x=100, y=430)

step_btn = tk.Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                     width=7)
step_btn.place(x=220, y=420)

final_btn = tk.Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                      width=7)
final_btn.place(x=330, y=420)

graph_btn = tk.Button(text="function change graph", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                      command=graph_window, width=25)
graph_btn.place(x=135, y=460)


# метод, вызывающий цикл обработки событий окна для взаимодействия с пользователем
root.mainloop()