import click
import random

import numpy as np
import matplotlib.pyplot as plt

X_LIM = (0, 1)
Y_LIM = (0, 1)
RADIUS = 1
POINTS_COUNT = (100, 1000, 10000, 100000)
SEED = 123

def gen_points(points_count):
    x_list = [random.uniform(*X_LIM) for x in range(points_count)]
    y_list = [random.uniform(*Y_LIM) for y in range(points_count)]
    return x_list, y_list


def is_below_arch(x, y):
    y_theor = np.sqrt(RADIUS ** 2 - np.square(x))
    return y < y_theor


def get_pi(points_inside, point_count):
    return 4 * np.sum(points_inside) / point_count


def plot_points_cirlce(ax, x_list, y_list, points_inside, title):
    circle = plt.Circle((X_LIM[0], Y_LIM[0]), RADIUS, color='black', fill=False)
    color_list = ['b' if bool(point) is True else 'r' for point in points_inside]

    ax.scatter(x_list, y_list, c=color_list)
    ax.set_xlim(*X_LIM)
    ax.set_ylim(*Y_LIM)
    ax.add_patch(circle)
    ax.set_title(title)


def run():
    random.seed(SEED)

    # Generate 4 sets of points
    x_0_list, y_0_list = gen_points(POINTS_COUNT[0])
    x_1_list, y_1_list = gen_points(POINTS_COUNT[1])
    x_2_list, y_2_list = gen_points(POINTS_COUNT[2])
    x_3_list, y_3_list = gen_points(POINTS_COUNT[3])

    # Check which points are below and above
    points_inside_0 = is_below_arch(x_0_list, y_0_list)
    points_inside_1 = is_below_arch(x_1_list, y_1_list)
    points_inside_2 = is_below_arch(x_2_list, y_2_list)
    points_inside_3 = is_below_arch(x_3_list, y_3_list)

    # Calculate PI
    pi_0 = 4 * sum(points_inside_0) / POINTS_COUNT[0]
    pi_1 = 4 * sum(points_inside_1) / POINTS_COUNT[1]
    pi_2 = 4 * sum(points_inside_2) / POINTS_COUNT[2]
    pi_3 = 4 * sum(points_inside_3) / POINTS_COUNT[3]

    # Plot results
    fig, axs = plt.subplots(2, 4, figsize=(10, 10))
    plot_points_cirlce(axs[0, 0], x_0_list, y_0_list, points_inside_0, f'Points: {POINTS_COUNT[0]}'
                                                                       f'\nPI: {pi_0}')
    plot_points_cirlce(axs[0, 1], x_1_list, y_1_list, points_inside_1, f'Points: {POINTS_COUNT[1]}'
                                                                       f'\nPI: {pi_1}')
    plot_points_cirlce(axs[0, 2], x_2_list, y_2_list, points_inside_2, f'Points: {POINTS_COUNT[2]}'
                                                                       f'\nPI: {pi_2}')
    plot_points_cirlce(axs[0, 3], x_3_list, y_3_list, points_inside_3, f'Points: {POINTS_COUNT[3]}'
                                                                       f'\nPI: {pi_3}')

    plt.show()
    # TODO: Wizualizacja
    # TODO: Wyswietlanie wyniku


if __name__ == '__main__':
    run()
