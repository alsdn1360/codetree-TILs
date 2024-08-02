word = input()
target = input()

cnt = 0

for i in range(len(word)):
    if word[i:i+2] == target:
        cnt += 1

print(cnt)