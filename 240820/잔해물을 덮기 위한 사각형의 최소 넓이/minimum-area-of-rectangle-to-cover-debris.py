offset = 1000
max_range = 2 * offset + 1

matrix = [
    [0] * max_range
    for _ in range(max_range)
]

for i in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    if i == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                matrix[x][y] = 1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                matrix[x][y] = 0
            
min_x = 2001
min_y = 2001
max_x = 0
max_y = 0

is_zero = True

for x in range(max_range):
    for y in range(max_range):
        if matrix[x][y] == 1:
            is_zero = False

            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y

for x in range(max_range):
    for y in range(max_range):
        if matrix[x][y] == 1:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

if is_zero:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)