N, K = tuple(map(int, input().split()))
block = [0] * (N + 1)

for _ in range(K):
    A, B = tuple(map(int, input().split()))

    for i in range(A, B + 1):
        block[i] += 1

max = 0

for num in block[1:]:
    if num > max:
        max = num

print(max)