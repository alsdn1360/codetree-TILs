def to_digit(digit):
    num = 0

    for i in range(len(digit)):
        num = num * 2 + digit[i]

    return num

digit = list(map(int, input()))

print(to_digit(digit))