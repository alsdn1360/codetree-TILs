n = int(input())
arr = list(map(int, input().split()))

def GCD(a, b):
    if b == 0:
        return a
    else:   
        return GCD(b, a % b)

def LCM(a, b):
    return a * b // GCD(a, b)

def find_n_LCM(index):
    if index == 0:
        return arr[0]
    
    return LCM(arr[index], find_n_LCM(index - 1))

print(find_n_LCM(n - 1))