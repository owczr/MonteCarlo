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


def plot_points_cirlce(ax, x_list, y_list, points_inside):
    circle = plt.Circle((X_LIM[0], Y_LIM[0]), RADIUS, color='black', fill=False)
    color_list = ['b' if bool(point) is True else 'r' for point in points_inside]

    ax.scatter(x_list, y_list, c=color_list)
    ax.set_xlim(*X_LIM)
    ax.set_ylim(*Y_LIM)
    ax.add_patch(circle)


def run(point_count=10000):
    random.seed(123)
    x_list, y_list = gen_points(point_count)
    points_inside = check_arch(x_list, y_list)
    fig, axs = plt.subplots(1, 1, figsize=(10, 10))
    plot_points_cirlce(axs, x_list, y_list, points_inside)
    plt.show()


if __name__ == '__main__':
    run()
