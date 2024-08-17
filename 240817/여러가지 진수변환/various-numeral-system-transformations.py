def to_4_or_8(target, N, B):
    while True:
        if N < B:
            target.append(N)
            break

        target.append(N % B)
        N //= B

    return target.reverse()

N, B = tuple(map(int, input().split()))
target = []

to_4_or_8(target, N, B)

for num in target:
    print(num, end = '')