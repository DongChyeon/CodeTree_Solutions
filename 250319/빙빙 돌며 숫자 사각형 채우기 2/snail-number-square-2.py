n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

x, y = 0, 0

# 남, 동, 북, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_idx = 0
count = 1

def is_end(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] == 0:
            return False

    return True

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n and grid[y][x] == 0

while True:
    grid[y][x] = count

    if is_end(x, y):
        break

    nx, ny = x + dx[dir_idx], y + dy[dir_idx]
    if in_range(nx, ny):
        x, y = nx, ny
        count += 1
    else:
        dir_idx = (dir_idx + 1) % 4

for row in grid:
    for col in row:
        print(col, end=' ')
    print()