'''
정방향인지 역방향인지 판단해야 한다
'''
m1, d1, m2, d2 = map(int, input().split())
is_forward = m2 > m1 or (m1 == m2 and d2 >= d1)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_month = m1
current_day = d1
duration = 0

if is_forward:
    if m1 == m2:
        duration = d2 - d1
    else:
        for month in range(m1, m2 + 1):
            if month == m1:
                duration = duration + num_of_days[month] - d1
            elif month == m2:
                duration = duration + d2
            else:
                duration = duration + num_of_days[month]
else:
    if m1 == m2:
        duration = d1 - d2
    else:
        for month in range(m1, m2 - 1, -1):
            if month == m2:
                duration = duration + num_of_days[month] - d2
            elif month == m1:
                duration = duration + d1
            else:
                duration = duration + num_of_days[month]

if is_forward:
    print(days[duration % 7])
else:
    print(days[-duration % 7])