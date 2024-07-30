str = input()
findWord = input()

cnt = 0

for i in range(len(str)):
    if str[i] == findWord:
        cnt += 1

print(cnt)