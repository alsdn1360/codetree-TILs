num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def cal_elapse_day(month, day):
    elapse_days = 0
    for i in range(1, month):
        elapse_days += num_of_days[i]
    elapse_days += day

    return elapse_days

def cal_day_of_week(month1, day1, month2, day2):
    elapse_days = cal_elapse_day(month2, day2) - cal_elapse_day(month1, day1)

    if elapse_days < 0:
        return day_of_week[-(abs(elapse_days) % 7)]
    else:
        return day_of_week[(abs(elapse_days) % 7)]

m1, d1, m2, d2 = tuple(map(int, input().split()))

print(cal_day_of_week(m1, d1, m2, d2))