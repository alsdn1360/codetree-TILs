query = list(input().split())
n = int(query[0])
k = int(query[1]) - 1
T = query[2]

result = []

for _ in range(n):
    word = input()

    if T in word:
        if word.find(T) == 0:
            result.append(word)

result.sort()

print(result[k])