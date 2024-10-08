n = int(input())
area = [0] * 200000
area_black = [0] * 200000
area_white = [0] * 200000
area_color = ['Null'] * 200000
last_index = 100000

for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == 'R':
        x = last_index + x

        for i in range(last_index, x):
            area[i] += 1
            area_black[i] += 1

            if area[i] >= 4 and area_white[i] >= 2 and area_black[i] >= 2:
                area_color[i] = 'G'
            else:
                area_color[i] = 'B'
            
        last_index = x - 1
    elif direction == 'L':
        x = last_index - x + 1

        for i in range(x, last_index + 1):
            area[i] += 1
            area_white[i] += 1

            if area[i] >= 4 and area_white[i] >= 2 and area_black[i] >= 2:
                area_color[i] = 'G'
            else:
                area_color[i] = 'W'

        last_index = x

cnt_white = 0
cnt_black = 0
cnt_grey = 0

for color in area_color:
    if color == 'W':
        cnt_white += 1
    elif color == 'B':
        cnt_black += 1
    elif color == 'G':
        cnt_grey += 1

print(cnt_white, cnt_black, cnt_grey)