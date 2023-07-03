import numpy as np
from algorithm.Swarm import Swarm


class PlaneFunction:

    # z = Ax + By + C
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, x, y):
        return self.A * x + self.B * y + self.C


num_of_iterations = int(input("Введите количество итераций: "))
num_of_particles = int(input("Введите количество частиц: "))
inertia = float(input("Введите инерцию: "))
local_weight = float(input("Введите локальный параметр: "))
global_weight = float(input("Введите глобальный параметр: "))
boundary_x_lower = float(input("Введите ограничение по Х снизу: "))
boundary_x_upper = float(input("Введите ограничение по Х сверху: "))
boundary_y_lower = float(input("Введите ограничение по Y снизу: "))
boundary_y_upper = float(input("Введите ограничение по Y сверху: "))

function = PlaneFunction(1, 2, 3)
boundaries = np.array([[boundary_x_lower, boundary_x_upper], [boundary_y_lower, boundary_y_upper]])
swarm = Swarm(num_of_particles, inertia, local_weight, global_weight, boundaries, function)
swarm.create_particles()

for i in range(num_of_iterations):
    cur_min = swarm.next_iteration()
    print("MIN VALUE: ", cur_min[1], "MIN VALUE POSITION: ", cur_min[0])
