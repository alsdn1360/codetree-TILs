word = input()
remove = input()

while(1):
    if remove in word:
        remove_index = word.find(remove)

        arr_word = list(word)

        for j in range(len(remove)):
            arr_word.pop(remove_index)

        word = ''.join(arr_word)
    else:
        break

print(word)