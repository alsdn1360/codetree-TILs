N = int(input())

offset = 100
area = [
    [0] * 2 * offset
    for _ in range(2 * offset)
]

for _ in range(N):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1

total_width = 0

for i in range(2 * offset):
    for j in range(2 * offset):
        if area[i][j] == 1:
            total_width += 1

print(total_width)