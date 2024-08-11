class forecast():
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

forecasts = []
for _ in range(n):
    date, day, weather = tuple(input().split())
    forecasts.append(forecast(date, day, weather))

min_idx = 0
for i in range(1, n):
    if forecasts[i].weather == 'Rain':
        if int(forecasts[min_idx].date[:4]) < int(forecasts[i].date[:4]):
            min_idx = i
            break

print(f'{forecasts[min_idx].date} {forecasts[min_idx].day} {forecasts[min_idx].weather}')