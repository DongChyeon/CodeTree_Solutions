n, m, r, c = map(int, input().split())
r, c = r - 1, c - 1
grid = [[0 for _ in range(n)] for _ in range(n)]
grid[r][c] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for sec in range(1, m + 1):
    bomb_pos = [
        (x, y)
        for y in range(n)
        for x in range(n)
        if grid[y][x] == 1
    ]

    for pos in bomb_pos:
        x, y = pos
        if grid[y][x] == 1:
            for i in range(4):
                nx, ny = x + (2 ** (sec - 1) * dx[i]), y + (2 ** (sec - 1) * dy[i])
                if in_range(nx, ny) and grid[ny][nx] != 1:
                    grid[ny][nx] = 1

answer = 0
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            answer += 1

print(answer)