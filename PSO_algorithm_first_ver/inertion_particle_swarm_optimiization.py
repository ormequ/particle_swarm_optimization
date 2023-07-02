import numpy as np

class PlaneFunction:
    # test
    # z = Ax + By + C
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def __call__(self, x, y):
        return self.A * x + self.B * y + self.C


class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_value = None
        self.best_pos = position.copy()


class Swarm:
    def __init__(self, num_of_particles, inertion, local_weight, global_weight, boundaries, function):
        self.function = function
        self.num_of_particles = num_of_particles
        self.inertion = inertion
        self.local_weight = local_weight
        self.global_weight = global_weight
        self.boundaries = boundaries
        self.best_global_pos = None
        self.best_global_val = None

    def gen_rand_vector(self, boundaries_x, boundaries_y):
        vector = np.random.rand(2)
        vector[0] = boundaries_x[0] + vector[0] * (boundaries_x[1] - boundaries_x[0])
        vector[1] = boundaries_y[0] + vector[1] * (boundaries_y[1] - boundaries_y[0])
        return vector

    def create_particles(self):
        '''
        равномерное распределение частиц
        присваивание минимального значения для каждой частицы
        поиск минимального значения среди них
        '''
        self.particles = list()

        for i in range(self.num_of_particles):
            start_pos = self.gen_rand_vector(self.boundaries[0], boundaries[1])
            cur_position_value = self.function(start_pos[0], start_pos[1])
            velocity_boundaries = lambda boundaries: [- (boundaries[1] - boundaries[0]), boundaries[1] - boundaries[0]]
            start_vel = self.gen_rand_vector(velocity_boundaries(self.boundaries[0]), velocity_boundaries(self.boundaries[1]))
            self.particles.append(Particle(start_pos, start_vel))
            self.particles[-1].best_value = cur_position_value

            if i == 0 or cur_position_value < self.best_global_val:
                self.best_global_pos = start_pos.copy()
                self.best_global_val = cur_position_value

    def update_particle_state(self, index):
        '''
        обновление значений одной частицы с индексом index
        передвижение частицы, если позволяет диапазон
        '''
        cur_particle = self.particles[index]
        velocity_component = self.inertion * cur_particle.velocity
        local_component = local_weight * np.random.rand(2) * (cur_particle.best_pos - cur_particle.position)
        global_component = global_weight * np.random.rand(2) * (self.best_global_pos - cur_particle.position)
        self.particles[index].velocity = velocity_component + local_component + global_component

        new_position = cur_particle.position + self.particles[index].velocity
        for i in range(len(self.boundaries)):
            if self.boundaries[i][0] >= new_position[i]: # проверка: координаты частицы не меньше значения левой границы по Х либо Y
                new_position[i] = self.boundaries[i][0]
            if new_position[i] >= self.boundaries[i][1]: # проверка: координаты частицы не больше значения правой границы по Х либо Y
                new_position[i] = self.boundaries[i][1]

        self.particles[index].position = new_position

        new_value = self.function(self.particles[index].position[0], self.particles[index].position[1])
        if new_value < cur_particle.best_value:
            self.particles[index].best_value = new_value
            self.particles[index].best_pos = self.particles[index].position.copy()

    def next_iteration(self):
        '''
        цикл по всем частицам
        '''
        for i in range(num_of_particles):
            self.update_particle_state(i)
            if self.particles[i].best_value < self.best_global_val:
                self.best_global_val = self.particles[i].best_value
                self.best_global_pos = self.particles[i].best_pos.copy()
        return [self.best_global_pos, self.best_global_val] # возвращает позицию при мин. знчаении и мин. значение
        
        



num_of_iterations = int(input("Введите количество итераций: "))
num_of_particles = int(input("Введите количество частиц: "))
inertion = float(input("Введите инерцию: "))
local_weight = float(input("Введите локальный параметр: "))
global_weight = float(input("Введите глобальный параметр: "))
boundary_x_lower = float(input("Введите ограничение по Х снизу: "))
boundary_x_upper = float(input("Введите ограничение по Х сверху: "))
boundary_y_lower = float(input("Введите ограничение по Y снизу: "))
boundary_y_upper = float(input("Введите ограничение по Y сверху: "))

function = PlaneFunction(1, 2, 3)
boundaries = np.array([[boundary_x_lower, boundary_x_upper], [boundary_y_lower, boundary_y_upper]])
swarm = Swarm(num_of_particles, inertion, local_weight, global_weight, boundaries, function)
swarm.create_particles()

for i in range(num_of_iterations):
    cur_min = swarm.next_iteration()
    print("MIN VALUE: ", cur_min[1], "MIN VALUE POSITION: ", cur_min[0])


