n = int(input())

arr = [
    input()
    for _ in range(n)
]

sum = 0
cnt = 0

for word in arr:
    if word[0] == 'a':
        cnt += 1
    
    sum += len(word)

print(f'{sum} {cnt}')