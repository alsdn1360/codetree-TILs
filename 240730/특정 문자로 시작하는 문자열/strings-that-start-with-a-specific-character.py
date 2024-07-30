n = int(input())

arr = [
    input()
    for _ in range(n)
]

alpha = input()

cnt = 0
sum = 0

for word in arr:
    if word[0] == alpha:
        cnt += 1
        sum += len(word)

print(f'{cnt} {sum / cnt:.2f}')