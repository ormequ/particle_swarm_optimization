from algorithm.Swarm import Swarm
from typing import Callable
import numpy as np


class System:
    def __init__(self, function: Callable, boundaries, num_of_particles: int = 100, inertia: float = 1,
                 local_weight: float = 1.5, global_weight: float = 1.5, stop_ratio: float = 0.75):
        self._swarm = Swarm(num_of_particles, inertia, local_weight, global_weight, boundaries, function)
        self._swarm.create_particles()
        self.stop_ratio = stop_ratio
        self.min_bound = min([boundaries[i][1] - boundaries[i][0] for i in range(2)])
        self.num_of_particles = num_of_particles
        self.stopped = False
        self.minimums = []
        self.particles_snapshots = []

    def proceed(self, iterations: int) -> int:
        """
        :param iterations: количество итераций.
        :return: оставшееся количество итераций после срабатывания критерия останова или 0, если не сработал
        """
        for i in range(iterations):
            self._swarm.next_iteration()
            self.minimums.append(self._swarm.get_current_min())
            self.particles_snapshots.append(self._swarm.particles.copy())

            if self.stopped:
                continue

            count_stopped = 0
            for particle in self._swarm.particles:
                if np.linalg.norm(particle.velocity) < self.min_bound * 1e-3:
                    count_stopped += 1
            if self.num_of_particles * self.stop_ratio <= count_stopped:
                self.stopped = True
                return iterations - i

        return 0

    def get_all_minimums(self):
        return self.minimums

    def get_particles(self):
        return self._swarm.particles

    def get_min(self):
        return self._swarm.get_current_min()
