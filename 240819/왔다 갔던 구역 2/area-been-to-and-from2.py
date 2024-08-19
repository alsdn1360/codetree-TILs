n = int(input())
area = [0] * 2000
last_index = 1000

for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == 'R':
        x = last_index + x
        for i in range(last_index, x):
            area[i] += 1

        last_index = x
    elif direction == 'L':
        x = last_index - x
        for i in range(x, last_index):
            area[i] += 1

        last_index = x

cnt_over_two = 0

for cnt in area:
    if cnt >= 2:
        cnt_over_two += 1

print(cnt_over_two)