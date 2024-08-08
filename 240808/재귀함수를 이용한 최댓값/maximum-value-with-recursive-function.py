n = int(input())
arr = list(map(int, input().split()))

max_num = 0
result = 0

def find_max_num(max_num, index):
    if index == n:
        return max_num

    if arr[index] > max_num:
        max_num = arr[index]

    return find_max_num(max_num, index + 1)

result = find_max_num(max_num, 0)

print(result)