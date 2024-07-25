arr = list(map(int, input().split()))

less = []
greater = []

for i in arr:
    if i < 500:
        less.append(i)
    else:
        greater.append(i)

print(f'{max(less)} {min(greater)}')