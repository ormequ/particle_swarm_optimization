import numpy as np
from algorithm.Swarm import Swarm
from algorithm.System import System
from functions.Rasting import Rastring

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np
from gui.GUI import GUI


# np.sin(x)*np.cos(y)+1;-1,1;-1,1

np.random.seed(42)

gui = GUI()
gui.loop()

exit()

def rastrigin(*X, **kwargs):
    print(X)
    A = kwargs.get('A', 10)
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])



# num_of_iterations = int(input("Введите количество итераций: "))
# num_of_particles = int(input("Введите количество частиц: "))
# inertia = float(input("Введите инерцию: "))
# local_weight = float(input("Введите локальный параметр: "))
# global_weight = float(input("Введите глобальный параметр: "))
# boundary_x_lower = float(input("Введите ограничение по Х снизу: "))
# boundary_x_upper = float(input("Введите ограничение по Х сверху: "))
# boundary_y_lower = float(input("Введите ограничение по Y снизу: "))
# boundary_y_upper = float(input("Введите ограничение по Y сверху: "))

num_of_iterations = 20
num_of_particles = 15
inertia = 0.3
local_weight = 1.4
global_weight = 1.5
bounds = [-5.12, 5.12]

"""
20 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y));-5.12,5.12;-5.12,5.12
"""

function = Rastring(bounds, 10)

boundaries = np.array([bounds, bounds])
system = System(function, boundaries, num_of_particles, inertia, local_weight, global_weight)
system.proceed(num_of_iterations)
print(system.get_min())


X = np.linspace(-5.12, 5.12, 200)
Y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(X, Y)
Z = np.array([function(X[i], Y[i]) for i in range(len(X))])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
plt.show()
