from tkinter import *
from tkinter import ttk

# создание графического окна
root = Tk()
# заголовок окна
root.title('Application using Tkinter')
# размеры окна
root.geometry('500x510')
root.resizable(False, False)

btn1 = Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13")
btn1.place(x=350, y=70)

btn2 = Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13")
btn2.place(x=270, y=350)

btn3 = Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13")
btn3.place(x=350, y=350)

btn4 = Button(text="function change graph", background="#B4B4B4", foreground="#232323", font="Roboto 13")
btn4.place(x=165, y=400)

# метод, вызывающий цикл обработки событий окна для взаимодействия с пользователем
root.mainloop()