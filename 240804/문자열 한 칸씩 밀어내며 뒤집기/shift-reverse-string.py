word, q = input().split()
q = int(q)

temp = ''

for i in range(q):
    query = int(input())

    if query == 1:
        word = word[1:] + word[0]
        print(word)
    elif query == 2:
        word = word[-1] + word[:-1]
        print(word)
    else:
        arr_word = list(word)

        for j in range(int(len(word) / 2)):
            temp = arr_word[j]
            arr_word[j] = arr_word[-1 - j]
            arr_word[-1 - j] = temp

        word = ''.join(arr_word)
        print(word)