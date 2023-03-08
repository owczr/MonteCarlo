import matplotlib.pyplot as plt
import numpy as np

from .pi import RADIUS, X_LIM, Y_LIM


def points_circle(ax, pi):
    circle = plt.Circle((X_LIM[0], Y_LIM[0]), RADIUS, color='black', fill=False)
    color_list = ['b' if bool(point) is True else 'r' for point in pi.get_points_inside()]

    ax.scatter(pi.get_y(), pi.get_x(), c=color_list)
    ax.set_xlim(*X_LIM)
    ax.set_ylim(*Y_LIM)
    ax.add_patch(circle)
    ax.set_title(f'Points: {len(pi)}, Estimated pi: {pi.get_pi():.2f}')


def boxplot(ax, pi_list):
    pi_values = [pi.get_pi() for pi in pi_list]
    print(pi_values)
    pi_split = np.array_split(pi_values, 10)
    ax.boxplot(pi_split, list(range(10)))
    ax.set_ylim((2, 4))
    ax.axhline(y=np.pi)


def _split(list_, size):
    for i in range(0, len(list_), size):
        yield list_[i:i + size]
