import numpy as np
from gui.GUI import GUI


np.random.seed(42)

gui = GUI()
gui.loop()

"""
20 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y));-5.12,5.12;-5.12,5.12
"""
