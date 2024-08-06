A = input()

order = list(input())

for elem in order:
    if elem == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]

print(A)