import math
import random

random.seed(42)

points = []

for i in range(20):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    z = math.sin(x) * math.cos(y) + 0.1 * x
    points.append((x, y, z))

def idw(x, y, points, power=2):
    numerator = 0.0
    denominator = 0.0

    for px, py, pz in points:
        distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)

        if distance == 0:
            return pz

        weight = 1.0 / (distance ** power)
        numerator += weight * pz
        denominator += weight

    return numerator / denominator

grid_size = 10

print("Spatial Interpolation using IDW")
print()

for y in range(grid_size + 1):
    row = []

    for x in range(grid_size + 1):
        value = idw(x, y, points)
        row.append(f"{value:.3f}")

    print(" ".join(row))

