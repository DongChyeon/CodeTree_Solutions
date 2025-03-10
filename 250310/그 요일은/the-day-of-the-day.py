import math

m1, d1, m2, d2 = map(int, input().split())
A = input()

days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def get_total_days(m, d):
    days = 0

    for month in range(1, m + 1):
        if month == m:
            days = days + d
        else:
            days = days + days_of_month[month]

    return days

diff = get_total_days(m2, d2) - get_total_days(m1, d1)

target_day_index = weeks.index(A)

if target_day_index > diff:
    print(0)
else:
    print(1 + (math.floor((diff- target_day_index) / 7)))
