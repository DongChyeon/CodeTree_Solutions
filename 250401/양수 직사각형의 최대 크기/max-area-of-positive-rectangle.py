n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = -1

def calculate(x, y, w, h):
    area = 0

    for y_pos in range(y, y + h):
        for x_pos in range(x, x + w):
            if grid[y_pos][x_pos] < 0:
                return -1
            else:
                area += 1

    return area

for y in range(n):
    for x in range(m):
        for w in range(1, m - x + 1):
            for h in range(1, n - y + 1):
                answer = max(answer, calculate(x, y, w, h))

print(answer)