import numpy as np

class Plane_Function:
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
    def __init__(self, num_of_particles, inertion, weight1, weight2, boundaries_x, boundaries_y, function):
        self.function = function
        self.num_of_particles = num_of_particles
        self.inertion = inertion
        self.weight1 = weight1
        self.weight2 = weight2
        self.boundaries_x = boundaries_x
        self.boundaries_y = boundaries_y
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
        присваение минимального значения для каждой частицы
        поиск минимального значения среди них
        '''
        self.particles = list()

        for i in range(self.num_of_particles):
            tmp_pos = self.gen_rand_vector(self.boundaries_x, self.boundaries_y)
            cur_position_value = self.function(tmp_pos[0], tmp_pos[1])
            velocity_boundaries = lambda boundaries: [- (boundaries[1] - boundaries[0]), boundaries[1] - boundaries[0]]
            tmp_vel = self.gen_rand_vector(velocity_boundaries(self.boundaries_x), velocity_boundaries(self.boundaries_y))
            self.particles.append(Particle(tmp_pos, tmp_vel))
            self.particles[-1].best_value = cur_position_value

            if i == 0 or cur_position_value < self.best_global_val:
                self.best_global_pos = tmp_pos.copy()
                self.best_global_val = cur_position_value

    def update_particle_state(self, index):
        '''
        обновление значений одной частицы с индексом index
        передвижение частицы, если позволяет диапазон
        '''
        cur_particle = self.particles[index]
        self.particles[index].velocity = self.inertion * cur_particle.velocity + weight1 * np.random.rand(2) * (cur_particle.best_pos - cur_particle.position) + weight2 * np.random.rand(2) * (self.best_global_pos - cur_particle.position)

        new_position = cur_particle.position + self.particles[index].velocity
        if self.boundaries_x[0] <= new_position[0] and new_position[0] <= self.boundaries_x[1]: # проверка: координаты частицы не вылезли за значение по Х
            if self.boundaries_y[0] <= new_position[1] and new_position[1] <= self.boundaries_y[1]: # проверка: координаты частицы не вылезли за значение по Y
                self.particles[index].position = new_position
                new_value = self.function(self.particles[index].position[0], self.particles[index].position[1])
                if new_value < cur_particle.best_value:
                    self.particles[index].best_value = new_value
                    self.particles[index].best_pos = self.particles[index].position.copy()
                # тут, если скорость слишком большая/маленькая, чтобы двигаться дальше, можно точку просто на границу, наверное, ставить

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
weight1 = float(input("Введите первый параметр: "))
weight2 = float(input("Введите второй параметр: "))
boundary_x_lower = float(input("Введите ограничение по Х снизу: "))
boundary_x_upper = float(input("Введите ограничение по Х сверху: "))
boundary_y_lower = float(input("Введите ограничение по Y снизу: "))
boundary_y_upper = float(input("Введите ограничение по Y сверху: "))

function = Plane_Function(1, 2, 3)
swarm = Swarm(num_of_particles, inertion, weight1, weight2, [boundary_x_lower, boundary_x_upper], [boundary_y_lower, boundary_y_upper], function)
swarm.create_particles()

for i in range(num_of_iterations):
    cur_min = swarm.next_iteration()
    print("MIN VALUE: ", cur_min[1], "MIN VALUE POSITION: ", cur_min[0])


