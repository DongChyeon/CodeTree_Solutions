n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

def dfs(x, y):
    dxs = [1, 0]
    dys = [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[ny][nx] = True
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)