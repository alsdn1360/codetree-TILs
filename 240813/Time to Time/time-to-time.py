def cal_elapse(hour, time):
    return 60 * hour + time

a, b, c, d = tuple(map(int, input().split()))

print(cal_elapse(c, d) - cal_elapse(a, b))