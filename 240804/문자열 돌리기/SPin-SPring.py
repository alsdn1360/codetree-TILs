word = input()
L = len(word)

for i in range(L + 1):
    print(word)

    word = word[-1] + word[:-1]