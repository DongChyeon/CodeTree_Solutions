m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

answer = 0

for month in range(m1, m2 + 1):
    if (month == m2):
        answer = answer + d2
    elif (month == m1):
        answer = answer + num_of_days[month] - d1 + 1
    else:
        answer = answer + num_of_days[month]

print(answer)