import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def road_accident(size):
    side = np.sqrt(2 * np.e + 0.5)

    X0, X1 = side / 3, 2 * side / 3

    fig = plt.figure(figsize = (5.0,5.0), frameon = False)

    probability_figure = fig.add_axes((0, 0, 2, 2))

    probability_figure.set_xlim(0, 5)
    probability_figure.set_ylim(0, 5)

    probability_figure.add_patch(Rectangle((0, 0), side, side, facecolor = "darkblue"))

    probability_figure.add_patch(Rectangle((side / 3, 0), side / 3, side, facecolor = "grey"))

    X = np.random.uniform(low = 0, high = side, size = size)
    Y = np.random.uniform(low = 0, high = side, size = size)
    plt.scatter(X, Y, marker = "x", color="Black")

    inside_mask = (X0 <= X) & (X <= X1)
    inside = len(X[inside_mask])

    prob = inside / size

    print(f'Из {size} людей, нарушивших правила дорожного движений, {inside} врезалось в фонарный столб. Доля пострадавших составляет {prob}')

    plt.show()

road_accident(100)