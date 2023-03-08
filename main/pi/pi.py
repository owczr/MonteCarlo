import random

import numpy as np


X_LIM = (0, 1)
Y_LIM = (0, 1)
RADIUS = 1


class Pi:
    def __init__(self, count):
        self.count = count
        self.x_list = [random.uniform(*X_LIM) for x in range(self.count)]
        self.y_list = [random.uniform(*Y_LIM) for y in range(self.count)]

    def __len__(self):
        return self.count

    def get_points(self):
        return self.x_list, self.y_list

    def get_x(self):
        return self.x_list

    def get_y(self):
        return self.y_list

    def get_points_inside(self):
        return is_below_arch(self.x_list, self.y_list)

    def get_points_outside(self):
        return ~is_below_arch(self.x_list, self.y_list)

    def get_pi(self):
        return 4 * np.sum(self.get_points_inside() / self.__len__())


def is_below_arch(x, y):
    y_theor = np.sqrt(RADIUS ** 2 - np.square(x))
    return y < y_theor
