offset = 100
max_range = 2 * offset + 1

matrix = [
    ['Null'] * max_range
    for _ in range(max_range)
]

n = int(input())

for i in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset

    if i % 2 == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                matrix[x][y] = 'R'
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                matrix[x][y] = 'B'

area = 0

for x in range(max_range):
    for y in range(max_range):
        if matrix[x][y] == 'B':
            area += 1

print(area)