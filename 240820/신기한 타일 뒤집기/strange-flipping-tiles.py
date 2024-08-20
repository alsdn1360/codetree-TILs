n = int(input())

last_index = 100000
tile = ['G'] * 2 * last_index

for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == 'R':
        x = last_index + x

        for i in range(last_index, x):
            tile[i] = 'B'

        last_index = x - 1
    elif direction == 'L':
        x = last_index - x + 1

        for i in range(x, last_index + 1):
            tile[i] = 'W'

        last_index = x

cnt_white = 0
cnt_black = 0

for color in tile:
    if color == 'W':
        cnt_white += 1
    elif color == 'B':
        cnt_black += 1

print(cnt_white, cnt_black)