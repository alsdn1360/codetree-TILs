n = int(input())
prices = list(map(int, input().split()))

min_price = 0
max_profit = 0
min_price_index = 0

for i in range(n):
    min_price_index = prices.index(min(prices))
    min_price = prices[min_price_index]

    if i > min_price_index and prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price

print(max(max_profit, 0))