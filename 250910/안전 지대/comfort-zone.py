n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

max_safe_area_depth = 0
max_safe_area_count = -1

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[y][x]:
        return False
    if grid[y][x] <= k:
        return False
    
    return True

def dfs(x, y, k):
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            visited[ny][nx] = True
            dfs(nx, ny, k)

max_height = 0
for y in range(n):
    for x in range(m):
        max_height = max(max_height, grid[y][x])

for k in range(1, max_height + 1):
    safe_area_count = 0
    visited = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if can_go(x, y, k):
                visited[y][x] = True
                dfs(x, y, k)
                safe_area_count += 1

    if (safe_area_count > max_safe_area_count):
        max_safe_area_count = safe_area_count
        max_safe_area_depth = k

print(max_safe_area_depth, max_safe_area_count)
