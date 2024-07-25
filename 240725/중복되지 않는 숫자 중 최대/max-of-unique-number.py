n = int(input())

arr = list(map(int, input().split()))

first = []
duplicate = []
result = []

for i in arr:
    if i not in first:
        first.append(i)
    else:
        if i not in duplicate:
            duplicate.append(i)

for i in arr:
    if i not in duplicate:
        result.append(i)

if len(result) == 0:
    print('-1')
else:
    print(max(result))