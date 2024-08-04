word = input()

remove_index = word.find('e')

arr_word = list(word)
arr_word.pop(remove_index)

word = ''.join(arr_word)

print(word)