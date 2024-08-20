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
                matrix[x][y] += 1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                matrix[x][y] += 2
            
area = 0

for x in range(max_range):
    for y in range(max_range):
        if matrix[x][y] == 1 or matrix[x][y] == 3:
            area += 1

print(area)