import click
import random

import numpy as np
import matplotlib.pyplot as plt


X_LIM = (0, 1)
Y_LIM = (0, 1)
RADIUS = 1


def gen_points(points_count):
    x_list = [random.uniform(*X_LIM) for x in range(points_count)]
    y_list = [random.uniform(*Y_LIM) for y in range(points_count)]
    return x_list, y_list


def check_arch(x, y):
    y_theor = np.sqrt(RADIUS ** 2 - np.square(x))
    return y < y_theor


def get_pi(points_inside, point_count):
    return 4 * np.sum(points_inside) / point_count


def plot_points_cirlce(x_list, y_list, points_inside):
    circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)



def run(point_count=10000):
    random.seed(123)
    x_list, y_list = gen_points(point_count)
    points_inside = check_arch(x_list, y_list)
    plt.show()

if __name__ == '__main__':
    run()
