word = input()
target = input()

def location_str():
    index_num = 0

    if target in word:
        index_num = word.index(target)
    else:
        index_num = -1

    return index_num

result = location_str()
print(result)