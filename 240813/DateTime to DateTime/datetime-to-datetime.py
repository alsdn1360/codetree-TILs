def cal_elapse_time(day, hour, minute):
    if day == 11 and hour < 11:
        return -1
    elif hour == 11 and minute < 11:
        return -1
    else:
        day -= 11
        hour -= 11
        minute -= 11

        return (1440 * day) + (60 * hour) + minute

a, b, c = tuple(map(int, input().split()))

print(cal_elapse_time(a, b, c))