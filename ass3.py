import math

def bilinear_interpolation(image, new_width, new_height):
height = len(image)
width = len(image[0])

result = [[0 for _ in range(new_width)] for _ in range(new_height)]

x_ratio = (width - 1) / (new_width - 1) if new_width > 1 else 0
y_ratio = (height - 1) / (new_height - 1) if new_height > 1 else 0

for y in range(new_height):
for x in range(new_width):
src_x = x * x_ratio
src_y = y * y_ratio

x1 = int(math.floor(src_x))
y1 = int(math.floor(src_y))
x2 = min(x1 + 1, width - 1)
y2 = min(y1 + 1, height - 1)

dx = src_x - x1
dy = src_y - y1

value = (
image[y1][x1] * (1 - dx) * (1 - dy)
+ image[y1][x2] * dx * (1 - dy)
+ image[y2][x1] * (1 - dx) * dy
+ image[y2][x2] * dx * dy
)

result[y][x] = round(value)

return result

image = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

new_width = 6
new_height = 6

result = bilinear_interpolation(image, new_width, new_height)

print("Original Image:")
for row in image:
print(row)

print("\nInterpolated Image:")
for row in result:
print(row)
