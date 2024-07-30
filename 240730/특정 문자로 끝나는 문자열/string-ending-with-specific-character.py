arr = [
    input()
    for _ in range(10)
]

alpha = input()
isExist = False

for word in arr:
    if word[len(word) - 1] == alpha:
        print(word)
        isExist = True

if isExist == False:
    print('None')