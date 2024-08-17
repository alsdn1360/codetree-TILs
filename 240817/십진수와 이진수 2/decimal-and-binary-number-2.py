def to_digit(N):
    num = 0

    for i in range(len(N)):
        num = num * 2 + N[i]

    return num

def to_binary(target, N):
    while True:
        if N < 2:
            target.append(N)
            break

        target.append(N % 2)
        N //= 2

    return target.reverse()

N = list(map(int, input()))
target = []

to_binary(target, 17 * to_digit(N))

for num in target:
    print(num, end = '')