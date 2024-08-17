n = int(input())
block = [0] * 200

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))

    x1 += 100
    x2 += 100

    for i in range(x1, x2):
        block[i] += 1

max = 0
for num in block:
    if num > max:
        max = num

print(max)