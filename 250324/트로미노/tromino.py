n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def in_range(x, y):
    return 0 <= y < n and 0 <= x < m

dxs = [
    [0, -1, 0],
    [0, 0, 1],
    [0, -1, 0],
    [0, 0, -1],
    [0, 1, 2],
    [0, 0, 0]
]
dys = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
    [0, -1, 0],
    [0, 0, 0],
    [0, -1, -2]
]

for y in range(n):
    for x in range(m):
        for i in range(6):
            count = 0
            for j in range(3):
                nx, ny = x + dxs[i][j], y + dys[i][j]

                if in_range(nx, ny):
                    count += grid[ny][nx]
                else:
                    break
            answer = max(answer, count)

print(answer)