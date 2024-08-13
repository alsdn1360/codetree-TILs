num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_elapse_day(month, day):
    elapse_days = 0
    for i in range(1, month + 1):
        elapse_days += num_of_days[i]
    elapse_days += day

    return elapse_days

m1, d1, m2, d2 = tuple(map(int, input().split()))

result = cal_elapse_day(m2, d2) - cal_elapse_day(m1, d1)

if result == 0:
    print('1')
else:
    print(result)