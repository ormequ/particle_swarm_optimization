import numpy as np


class Particle:
    def __init__(self, position: np.array, velocity: np.array):
        self.position = position
        self.velocity = velocity
        self.best_value = None
        self.best_pos = position.copy()
