N = int(input())
arr = [0, 1]

index_N = 1
result = 0

def find_index_N(index_N, index):
    if index == N - 1:
        return index_N

    index_N = (arr[(index // 3) + 1]) + arr[index]
    arr.append(index_N)

    return find_index_N(index_N, index + 1)

result = find_index_N(index_N, 1)

print(result)