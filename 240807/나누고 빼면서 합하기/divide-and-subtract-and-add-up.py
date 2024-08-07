n, m = map(int, input().split())
A = list(map(int, input().split()))

def func(A, m):
    sum_val = 0

    while(m >= 1):
        sum_val += A[m - 1]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1

    return sum_val

result = func(A, m)

print(result)