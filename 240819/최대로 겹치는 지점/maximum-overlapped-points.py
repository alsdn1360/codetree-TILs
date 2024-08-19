n = int(input())
block = [0] * 100

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))

    for i in range(x1, x2 + 1):
        block[i] += 1

max_cnt = 0

for cnt in block:
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)