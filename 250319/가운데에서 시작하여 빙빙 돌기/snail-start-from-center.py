n = int(input())
grid = [[0] * n for _ in range(n)]

x, y = (n - 1) // 2, (n - 1) // 2

# 동 북 서 남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_idx = 0

grid[y][x] = 1
radius = 1
count = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while count < n * n:
    for _ in range(2):
        for _ in range(radius):
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]
            if in_range(nx, ny) and grid[ny][nx] == 0:
                x, y = nx, ny
                count += 1
                grid[y][x] = count
        dir_idx = (dir_idx + 1) % 4
    radius += 1

for row in grid:
    for col in row:
        print(col, end=' ')
    print()