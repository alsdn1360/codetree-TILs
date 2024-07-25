n = int(input())
prices = list(map(int, input().split()))

min_price = float('inf')
max_profit = 0
min_price_index = 0

for i in range(n):
    if prices[i] < min_price:
        min_price = prices[i]
        min_price_index = i
    
    if i > min_price_index and prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price

print(max(max_profit, 0))