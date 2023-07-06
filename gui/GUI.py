import tkinter as tk
from tkinter import ttk
from algorithm.System import System
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import cm
from math import *


# TODO refactoring
class GUI:
    def __init__(self):
        self.main_ax = None
        self.canvas = None
        self.system = None
        self.main_scatter = None
        self.f = ""

        # создание графического окна
        self.root = tk.Tk()
        # заголовок окна
        self.root.title('Application using Tkinter')
        # размеры окна, смещение от левого верхнего угла
        self.root.geometry('700x710+500+250')
        self.root.resizable(False, False)

        self.function_label = tk.Label(text="Function", font="Roboto 13")
        self.function_label.place(x=200, y=20)

        self.function_entry = tk.Entry(font="Roboto 13")
        self.function_entry.place(x=200, y=40)

        self.reset_btn = tk.Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                   command=self.reset)
        self.reset_btn.place(x=450, y=40)

        self.inertia_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Inertia", resolution=0.05)
        self.inertia_scale.place(x=200, y=67)
        self.inertia_scale.set(0.75)

        self.local_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Local", resolution=0.05)
        self.local_scale.place(x=400, y=67)
        self.local_scale.set(2.0)

        self.global_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Global", resolution=0.05)
        self.global_scale.place(x=200, y=125)
        self.global_scale.set(1.5)

        self.stop_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Stop ratio", resolution=0.05)
        self.stop_scale.place(x=400, y=125)
        self.stop_scale.set(0.75)

        self.min_label = tk.Label(text="Start to minimize your function", font="Roboto 13")
        self.min_label.place(x=150, y=590)

        self.iterator_label = tk.Label(text="iterator", font="Roboto 13")
        self.iterator_label.place(x=200, y=610)

        self.step_entry = tk.Entry(font="Roboto 13", width=10)
        self.step_entry.place(x=200, y=630)

        self.step_btn = tk.Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                  width=7, command=self.step)
        self.step_btn.place(x=320, y=630)

        self.final_btn = tk.Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                   width=7, command=self.final)
        self.final_btn.place(x=430, y=630)

        self.plot_btn = tk.Button(text="function change plot", background="#B4B4B4", foreground="#232323",
                                   font="Roboto 13",
                                   command=self.plot_window, width=25)
        self.plot_btn.place(x=235, y=670)

    def function(self, X, Y):
        if hasattr(X, '__iter__'):
            assert len(X) == len(Y)
            res = []
            for i in range(len(X)):
                x, y = X[i], Y[i]
                res.append(eval(self.f))
            return res
        else:
            x, y = X, Y
            return eval(self.f)

    def reset(self):
        self.f, bound_x, bound_y = self.function_entry.get().split(';')
        bound_y = np.array(list(map(float, bound_y.split(','))))
        bound_x = np.array(list(map(float, bound_x.split(','))))

        self.min_label.config(text="Start to minimize your function")
        inertia = float(self.inertia_scale.get())
        local_weight = float(self.local_scale.get())
        global_weight = float(self.global_scale.get())
        stop_ratio = float(self.stop_scale.get())
        particles = int(sqrt((bound_x[1] - bound_x[0] - 1) * (bound_y[1] - bound_y[0] - 1)))
        if particles < 4:
            particles = 4

        self.system = System(self.function, [bound_x, bound_y], num_of_particles=particles, inertia=inertia,
                             local_weight=local_weight, global_weight=global_weight, stop_ratio=stop_ratio)
        self.draw_plot(bound_x, bound_y)

    def update_scatter(self):
        p_x = []
        p_y = []
        p_z = []
        for particle in self.system.get_particles():
            p_x.append(particle.position[0])
            p_y.append(particle.position[1])
            p_z.append(self.function(particle.position[0], particle.position[1]))
        if self.main_scatter:
            self.main_scatter.remove()
        self.main_scatter = self.main_ax.scatter(p_x, p_y, p_z, c='#000000', alpha=1, s=20, zorder=1)
        self.canvas.draw()

    def draw_plot(self, bound_x, bound_y):
        X = np.linspace(bound_x[0], bound_x[1], int(bound_x[1] - bound_x[0]) * 10)
        Y = np.linspace(bound_y[0], bound_y[1], int(bound_y[1] - bound_y[0]) * 10)
        X, Y = np.meshgrid(X, Y)
        Z = np.array([self.function(X[i], Y[i]) for i in range(len(X))])
        fig = Figure()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.main_ax = fig.add_subplot(projection='3d')
        self.main_ax.plot_surface(X, Y, Z, cmap=cm.plasma, alpha=0.7)
        self.update_scatter()

        toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        toolbar.update()

        toolbar.place(x=150, y=190)
        self.canvas.get_tk_widget().place(x=150, y=190, height=400, width=400)

    def step(self):
        iterations = int(self.step_entry.get())
        self.proceed(iterations)

    def proceed(self, iterations, change_input=True):
        remain_iters = self.system.proceed(iterations)
        position, value = self.system.get_min()
        min_txt = f"Minimum is {round(value, 2)} at ({round(position[0], 2)}, {round(position[1], 2)})"
        if remain_iters > 0 and change_input:
            self.step_entry.delete(0, tk.END)
            self.step_entry.insert(0, remain_iters)
        if self.system.stopped:
            min_txt += ". The stop criterion has been triggered"
        self.min_label.config(text=min_txt)
        self.update_scatter()

    def final(self):
        if self.system.stopped:
            return
        self.proceed(1000000000, False)

    def plot_window(self):
        win = tk.Tk()
        win.geometry("500x400+1000+250")
        win.resizable(False, False)
        fig = Figure()
        canvas = FigureCanvasTkAgg(fig, master=win)  # A tk.DrawingArea.
        ax = fig.add_subplot()
        minimums = self.system.get_all_minimums()
        ax.plot([i+1 for i in range(len(minimums))], [m[1] for m in minimums], c='red')
        ax.set_xlim(1, len(minimums)+1)

        toolbar = NavigationToolbar2Tk(canvas, win, pack_toolbar=False)
        toolbar.update()

        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return win

    def loop(self):
        self.root.mainloop()
