import math

points = [
    [1, 1],
    [2, 1],
    [1, 2],
    [2, 2]
]

tx = 3
ty = 2
sx = 2
sy = 2
angle = math.radians(30)

a = sx * math.cos(angle)
b = -sy * math.sin(angle)
c = sy * math.sin(angle)
d = sy * math.cos(angle)

print("Original Points:")
for point in points:
    print(point)

print("\nAffine Transformation Matrix:")
print("[", round(a, 3), round(b, 3), tx, "]")
print("[", round(c, 3), round(d, 3), ty, "]")
print("[  0      0       1 ]")

print("\nTransformed Points:")

for x, y in points:
    new_x = a * x + b * y + tx
    new_y = c * x + d * y + ty
    print("[", round(new_x,
