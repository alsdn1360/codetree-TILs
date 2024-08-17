def to_binary(binary, n):
    while True:
        if n < 2:
            binary.append(n)
            break

        binary.append(n % 2)
        n //= 2

    return binary.reverse()

n = int(input())
binary = []

to_binary(binary, n)

for num in binary:
    print(num, end = '')