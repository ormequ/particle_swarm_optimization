from copy import copy
from typing import Callable
import numpy as np
from algorithm.Particle import Particle


class Swarm:
    def __init__(self, num_of_particles: int, inertia: float, local_weight: float, global_weight: float,
                 boundaries: np.ndarray, function: Callable):
        self.particles = list()
        self.function = function
        self.num_of_particles = num_of_particles
        self.inertia = inertia
        self.local_weight = local_weight
        self.global_weight = global_weight
        self.boundaries = boundaries
        self.best_global_pos = None
        self.best_global_val = None

    @staticmethod
    def gen_rand_vector(boundaries: np.ndarray) -> np.ndarray:
        vector = np.random.rand(len(boundaries))
        for i in range(len(boundaries)):
            vector[i] = boundaries[i][0] + vector[i] * (boundaries[i][1] - boundaries[i][0])
        return vector

    def create_particles(self):
        """
        Равномерное распределение частиц
        присваивание минимального значения для каждой частицы
        поиск минимального значения среди них
        """
        def get_velocity_boundaries(boundaries):
            return [- (boundaries[1] - boundaries[0]), boundaries[1] - boundaries[0]]

        for i in range(self.num_of_particles):
            start_pos = self.gen_rand_vector(self.boundaries)
            cur_position_value = self.function(start_pos[0], start_pos[1])
            start_vel = self.gen_rand_vector(np.array([
                get_velocity_boundaries(self.boundaries[0]),
                get_velocity_boundaries(self.boundaries[1])
            ]))
            self.particles.append(Particle(start_pos, start_vel, cur_position_value))

            if i == 0 or cur_position_value < self.best_global_val:
                self.best_global_pos = start_pos.copy()
                self.best_global_val = cur_position_value

    def update_particle_state(self, index: int):
        """
        Обновление значений одной частицы с индексом index
        передвижение частицы, если позволяет диапазон
        """
        cur_particle = self.particles[index]
        velocity_component = self.inertia * cur_particle.velocity
        local_component = self.local_weight * np.random.rand(2) * (cur_particle.best_pos - cur_particle.position)
        global_component = self.global_weight * np.random.rand(2) * (self.best_global_pos - cur_particle.position)
        self.particles[index].velocity = velocity_component + local_component + global_component

        new_position = cur_particle.position + self.particles[index].velocity
        for i in range(len(self.boundaries)):
            # Проверка: координаты частицы не меньше значения левой границы по Х либо Y
            if self.boundaries[i][0] >= new_position[i]:
                new_position[i] = self.boundaries[i][0]
            # Проверка: координаты частицы не больше значения правой границы по Х либо Y
            if new_position[i] >= self.boundaries[i][1]:
                new_position[i] = self.boundaries[i][1]

        self.particles[index].position = new_position

        new_value = self.function(self.particles[index].position[0], self.particles[index].position[1])
        if new_value < cur_particle.best_value:
            self.particles[index].best_value = new_value
            self.particles[index].best_pos = self.particles[index].position.copy()

    def next_iteration(self):
        """
        Цикл по всем частицам
        возвращает позицию при мин. значении и мин. значение
        """
        for i in range(self.num_of_particles):
            self.update_particle_state(i)
            if self.particles[i].best_value < self.best_global_val:
                self.best_global_val = self.particles[i].best_value
                self.best_global_pos = self.particles[i].best_pos.copy()

    def get_current_min(self) -> tuple:
        return self.best_global_pos, self.best_global_val

    def __copy__(self):
        new = Swarm(self.num_of_particles, self.inertia, self.local_weight, self.global_weight, self.boundaries.copy(), self.function)
        new.particles = [copy(p) for p in self.particles]
        new.best_global_pos = self.best_global_pos.copy()
        new.best_global_val = self.best_global_val
        return new
