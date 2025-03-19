n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = int(10e9)

for skip_check in range(1, n - 1):
    user_x, user_y = x[0], y[0]
    current = 0
    for i in range(1, n):
        if i == skip_check:
            continue
        current += (abs(user_x - x[i]) + abs(user_y - y[i]))
        user_x, user_y = x[i], y[i]
    answer = min(answer, current)

print(answer)
