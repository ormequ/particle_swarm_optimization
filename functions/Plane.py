class Plane:

    # z = Ax + By + C
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, x, y):
        return self.A * x + self.B * y + self.C