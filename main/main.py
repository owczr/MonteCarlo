import click
import random

import numpy as np
import matplotlib.pyplot as plt

from pi import pi
from pi import plot


@click.command()
@click.option('--points-count', type=click.INT, help='Amount of random points')
@click.option('--seed', type=click.INT, default=123, help='Random seed')
@click.option('--height', type=click.INT, default=10, help='Random seed')
@click.option('--width', type=click.INT, default=15, help='Random seed')
@click.option('--p1', type=click.INT, default=25, help='First percentile, used in boxplots')
@click.option('--p2', type=click.INT, default=75, help='Second percentile, used in boxplots')
@click.option('--save-plot', type=click.BOOL, default=False, help='Save figure')
def run(points_count, seed, height, width, p1, p2, save_plot):
    random.seed(seed)

    # Create list of pi estimates
    pi_list = [pi.Pi(count) for count in range(points_count)]

    # Create figure and axes
    fig, axs = plt.subplots(2, 3, figsize=(width, height))
    gs = axs[0, 1].get_gridspec()
    axs[0, 2].remove()
    axbig = fig.add_subplot(gs[0, 1:])
    fig.tight_layout()

    # Prepare data for plots
    points_count_list = np.array(range(points_count + 1))
    med = int(np.median(points_count_list))
    p_1 = int(np.percentile(points_count_list, p1))
    p_2 = int(np.percentile(points_count_list, p2))

    # Plot
    plot.points_circle(axs[0, 0], pi_list[med])
    plot.boxplot(axs[1, 0], pi_list[:p_1], f'0 and {p1} percentile')
    plot.boxplot(axs[1, 1], pi_list[p_1:p_2], f'{p1} and {p2} percentiles')
    plot.boxplot(axs[1, 2], pi_list[p_2:], f'{p2} percentile and last value')
    plot.all_estimates(axbig, pi_list)

    plt.show()

    if save_plot:
        plt.savefig('montecarlo.png')


if __name__ == '__main__':
    run()
