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

first_rain_idx = 0
for i in range(n):
    if forecasts[i].weather == 'Rain':
        first_rain_idx = i
        break

for i in range(first_rain_idx + 1, n):
    if forecasts[i].weather == 'Rain':
        if int(forecasts[first_rain_idx].date[:4]) > int(forecasts[i].date[:4]):
            first_rain_idx = i

print(f'{forecasts[first_rain_idx].date} {forecasts[first_rain_idx].day} {forecasts[first_rain_idx].weather}')