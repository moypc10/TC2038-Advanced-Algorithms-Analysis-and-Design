from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np

# Lista de puntos proporcionada
points = np.array([
    [9, 7], (1, 3), (7, 2), (1, 9), (5, 4)
])

hull = ConvexHull(points)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))

for ax in (ax1, ax2):
    ax.plot(points[:, 0], points[:, 1], ".", color="k")
    if ax == ax1:
        ax.set_title("Given points")
    else:
        ax.set_title("Convex hull")
        for simplex in hull.simplices:
            ax.plot(points[simplex, 0], points[simplex, 1], "c")
        ax.plot(
            points[hull.vertices, 0],
            points[hull.vertices, 1],
            "o",
            mec="r",
            color="none",
            lw=1,
            markersize=10,
        )
    ax.set_xticks(range(-20, 21, 5))
    ax.set_yticks(range(-20, 21, 5))
plt.show()