import numpy as np


class Particle:
    def __init__(self, position: np.array, velocity: np.array, position_value: float):
        self.position = position
        self.velocity = velocity
        self.best_value = position_value
        self.best_pos = position.copy()
