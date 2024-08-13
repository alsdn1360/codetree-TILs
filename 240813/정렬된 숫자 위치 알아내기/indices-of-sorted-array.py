class Number():
    def __init__(self, num, sorted_idx = 0):
        self.num = num
        self.sorted_idx = sorted_idx

n = int(input())
numbers_input = list(map(int, input().split()))

numbers = []
for num in numbers_input:
    numbers.append(Number(num))

sorted_numbers = sorted(numbers, key = lambda x : x.num)
for idx, num in enumerate(sorted_numbers, 1):
    num.sorted_idx = idx

for num in numbers:
    print(num.sorted_idx, end = ' ')