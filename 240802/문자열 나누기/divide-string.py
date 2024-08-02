n = int(input())

word = input().split()

cnt = 0
sumWord = ''

for i in word:
    sumWord += i

for i in sumWord:
    cnt += 1
    print(i, end = '')

    if cnt == 5:
        print()
        cnt = 0