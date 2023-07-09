import tkinter as tk
from tkinter import ttk
from algorithm.System import System
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import cm
from math import *


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
        self.root.geometry('1280x680+100+150')
        self.root.resizable(False, False)

        self.function_label = tk.Label(text="Function", font="Roboto 13")
        self.function_label.place(x=20, y=20)
        self.function_entry = tk.Entry(font="Roboto 13", width=39)
        self.function_entry.place(x=130, y=20)

        self.bound_x_label = tk.Label(text="X boundaries", font="Roboto 13")
        self.bound_x_label.place(x=20, y=50)
        self.bound_xl_entry = tk.Entry(font="Roboto 13", width=8)
        self.bound_xl_entry.place(x=20, y=75)
        self.bound_xr_entry = tk.Entry(font="Roboto 13", width=8)
        self.bound_xr_entry.place(x=120, y=75)

        self.bound_y_label = tk.Label(text="Y boundaries", font="Roboto 13")
        self.bound_y_label.place(x=280, y=50)
        self.bound_yl_entry = tk.Entry(font="Roboto 13", width=8)
        self.bound_yl_entry.place(x=280, y=75)
        self.bound_yr_entry = tk.Entry(font="Roboto 13", width=8)
        self.bound_yr_entry.place(x=380, y=75)

        self.inertia_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Inertia",
                                      resolution=0.05)
        self.inertia_scale.place(x=20, y=100)
        self.inertia_scale.set(0.75)

        self.local_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Local", resolution=0.05)
        self.local_scale.place(x=140, y=100)
        self.local_scale.set(2.0)

        self.global_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=1.0, to=3.0, label="Global",
                                     resolution=0.05)
        self.global_scale.place(x=260, y=100)
        self.global_scale.set(1.5)

        self.stop_scale = tk.Scale(length=100, orient=tk.HORIZONTAL, from_=0.0, to=1.0, label="Stop ratio",
                                   resolution=0.05)
        self.stop_scale.place(x=380, y=100)
        self.stop_scale.set(0.75)

        self.reset_btn = tk.Button(text="reset", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                   command=self.reset, width=51)
        self.reset_btn.place(x=20, y=170)

        self.min_label = tk.Label(text="Start to minimize your function", font="Roboto 13")
        self.min_label.place(x=20, y=600)

        self.iterator_label = tk.Label(text="Iterator", font="Roboto 13")
        self.iterator_label.place(x=20, y=635)

        self.step_entry = tk.Entry(font="Roboto 13", width=10)
        self.step_entry.place(x=90, y=635)

        self.step_btn = tk.Button(text="step", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                  width=7, command=self.step)
        self.step_btn.place(x=230, y=630)

        self.final_btn = tk.Button(text="final", background="#B4B4B4", foreground="#232323", font="Roboto 13",
                                   width=7, command=self.final)
        self.final_btn.place(x=320, y=630)

        # self.plot_btn = tk.Button(text="function change plot", background="#B4B4B4", foreground="#232323",
        #                           font="Roboto 13",
        #                           command=self.plot_window, width=25)
        # self.plot_btn.place(x=235, y=670)

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
        self.f = self.function_entry.get()

        bound_y = np.array([float(self.bound_yl_entry.get()), float(self.bound_yr_entry.get())])
        bound_x = np.array([float(self.bound_xl_entry.get()), float(self.bound_xr_entry.get())])

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
        self.main_scatter = self.main_ax.scatter(p_x, p_y, p_z, c='#000000', alpha=1, s=20, zorder=1, label='Minimum at iteration')
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

        toolbar.place(x=540, y=20)
        self.canvas.get_tk_widget().place(x=540, y=20, height=640, width=700)
        fn_label = tk.Label(text="Function plot - gradient", font="Roboto 13")
        fn_label.place(x=1066, y=20)
        point_label = tk.Label(text="Point - black dot", font="Roboto 13")
        point_label.place(x=1118, y=60)

    def step(self):
        iterations = int(self.step_entry.get())
        self.proceed(iterations)
        self.display_min_plot()

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

    def display_min_plot(self):
        fig = Figure()
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        ax = fig.add_subplot()
        minimums = self.system.get_all_minimums()
        ax.plot([i + 1 for i in range(len(minimums))], [m[1] for m in minimums], c='red', label='Minimum at iteration')
        ax.set_xlim(1, len(minimums) + 1)

        canvas.get_tk_widget().place(x=20, y=230, height=360, width=480)
        min_label = tk.Label(text="Changing of minimum (metric) - red", font="Roboto 13")
        min_label.place(x=150, y=230)

    def loop(self):
        self.root.mainloop()
