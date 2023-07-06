import tkinter as tk
from tkinter import ttk

# создание графического окна
root = tk.Tk()
# заголовок окна
root.title('Application using Tkinter')
# размеры окна, смещение от левого верхнего угла
root.geometry('500x510+500+250')
root.resizable(False, False)

function_entry = tk.Entry(font="Roboto 13")
function_entry.place(x=100, y=50)

reset_btn = tk.Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13")
reset_btn.place(x=350, y=40)

canvas = tk.Canvas(bg="white", height=300, width=300)
canvas.place(x=100, y=100)

step_btn = tk.Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13")
step_btn.place(x=270, y=410)

final_btn = tk.Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13")
final_btn.place(x=350, y=410)

graph_btn = tk.Button(text="function change graph", background="#B4B4B4", foreground="#232323", font="Roboto 13")
graph_btn.place(x=165, y=450)

step_entry = tk.Entry(font="Roboto 13")
step_entry.place(x=60, y=415)

# метод, вызывающий цикл обработки событий окна для взаимодействия с пользователем
root.mainloop()