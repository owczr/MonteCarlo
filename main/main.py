import click
import random

import numpy as np
import matplotlib.pyplot as plt

from pi import pi
from pi import plot


POINTS_COUNT = 1000
SEED = 123


def run():
    random.seed(SEED)

    pi_list = [pi.Pi(count) for count in range(POINTS_COUNT)]

    # Plot results
    fig, axs = plt.subplots(2, 3, figsize=(10, 10))
    gs = axs[0, 1].get_gridspec()
    axs[0, 2].remove()
    axbig = fig.add_subplot(gs[0, 1:])

    fig.tight_layout()

    plot.points_circle(axs[0, 0], pi_list[99])

    p1 = int(np.percentile(np.array(range(POINTS_COUNT)), 25))
    p2 = int(np.percentile(np.array(range(POINTS_COUNT)), 75))

    plot.boxplot(axs[1, 0], pi_list[:p1])
    plot.boxplot(axs[1, 1], pi_list[p1:p2])
    plot.boxplot(axs[1, 2], pi_list[p2:])

    plt.show()


if __name__ == '__main__':
    run()
