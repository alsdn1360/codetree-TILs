A = list(input())
B = list(input())

A.sort()
B.sort()

A_str = ''.join(A)
B_str = ''.join(B)

if A_str == B_str:
    print('Yes')
else:
    print('No')