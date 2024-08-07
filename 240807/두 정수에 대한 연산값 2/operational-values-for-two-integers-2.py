a, b = map(int, input().split())

def func(a, b):
    a = a + 10
    b = b * 2
    
    return a, b

if a > b:
    a, b = func(b, a)
    print(a, b)
else:
    a, b = func(a, b)
    print(a, b)