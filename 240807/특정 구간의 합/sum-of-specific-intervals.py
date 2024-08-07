n, m = map(int, input().split())
A = list(map(int, input().split()))

def sum_range(a1, a2):
    sum_val = 0
    a1 -= 1

    for i in range(a1, a2):
        sum_val += A[i]

    return sum_val

for i in range(m):
    a1, a2 = map(int, input().split())

    result = sum_range(a1, a2)
    print(result)