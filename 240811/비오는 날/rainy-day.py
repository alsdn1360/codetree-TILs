from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

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
for i in range(1, n):
    if forecasts[i].weather == 'Rain':
        if first_rain_idx == 0 or parse_date(forecasts[first_rain_idx].date) > parse_date(forecasts[i].date):
            first_rain_idx = i

print(f'{forecasts[first_rain_idx].date} {forecasts[first_rain_idx].day} {forecasts[first_rain_idx].weather}')