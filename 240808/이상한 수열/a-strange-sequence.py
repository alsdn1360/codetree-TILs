N = int(input())
arr = [1]

result = 0

def find_index_N(index):
    if index > N:
        return arr[N - 1]
    else:
        arr.append((arr[(index - 2) // 3]) + arr[index - 1])

        return find_index_N(index + 1)

result = find_index_N(1)

print(result)