offset = 100
max_range = 2 * offset

matrix = [
    [0] * max_range
    for _ in range(max_range)
]

N = int(input())

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    x, y = x + offset, y + offset

    for x in range(x, x + 8):
        for y in range(y, y + 8):
            matrix[x][y] = 1

area = 0

for x in range(max_range):
    for y in range(max_range):
        if matrix[x][y] == 1:
            area += 1

print(area)