def to_digit(n, a):
    num = 0

    for i in range(len(n)):
        num = num * a + n[i]

    return num

def to_b(target, num, b):
    while True:
        if num < b:
            target.append(num)
            break

        target.append(num % b)
        num //= b

    return target.reverse()

a, b = tuple(map(int, input().split()))
n = list(map(int, input()))
target = []

to_b(target, to_digit(n, a), b)

for num in target:
    print(num, end = '')