offset = 100
max_range = 2 * offset + 1

matrix = [
    [0] * max_range
    for _ in range(max_range)
]

N = int(input())

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    x += offset
    y += offset

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            matrix[i][j] = 1

area = 0

for i in range(max_range):
    for j in range(max_range):
        if matrix[i][j] == 1:
            area += 1

print(area)