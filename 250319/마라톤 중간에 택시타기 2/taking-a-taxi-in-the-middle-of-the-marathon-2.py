n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = int(10e9)
for i in range(1, n - 1):
    current = 0
    current += (abs(x[0] - x[i]) + abs(y[0] - y[i]))
    current += (abs(x[n - 1] - x[i]) + abs(y[n - 1] - y[i]))

    answer = min(answer, current)

print(answer)
