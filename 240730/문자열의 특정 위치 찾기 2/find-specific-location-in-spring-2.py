arr = ["apple", "banana", "grape", "blueberry", "orange"]

word = input()

cnt = 0

for i in range(len(arr)):
    if arr[i][2] == word or arr[i][3] == word:
        print(arr[i])
        cnt += 1

print(cnt)