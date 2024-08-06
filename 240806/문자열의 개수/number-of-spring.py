arr = []

while(1):
    word = input()

    if word == '0':
        break

    arr.append(word)

cnt = len(arr)

print(cnt)

for i in range(cnt):
    if i % 2 == 0:
        print(arr[i])