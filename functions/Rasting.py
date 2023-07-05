import numpy as np


class Rastring:

    # z = Ax + By + C
    def __init__(self, boundaries, A):
        self.boundaries = boundaries
        self.A = A

    def __call__(self, x: float, y: float) -> float:
        return self.A*2 + (x ** 2 - self.A * np.cos(2 * np.pi * x)) + (y ** 2 - self.A * np.cos(2 * np.pi * y))
