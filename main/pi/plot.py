import matplotlib.pyplot as plt

from .pi import RADIUS, X_LIM, Y_LIM


def points_circle(ax, pi):
    circle = plt.Circle((X_LIM[0], Y_LIM[0]), RADIUS, color='black', fill=False)
    color_list = ['b' if bool(point) is True else 'r' for point in pi.get_points_inside()]

    ax.scatter(pi.get_y(), pi.get_x(), c=color_list)
    ax.set_xlim(*X_LIM)
    ax.set_ylim(*Y_LIM)
    ax.add_patch(circle)
    ax.set_title(f'Points: {len(pi)}, Estimated pi: {pi.get_pi():.2f}')
