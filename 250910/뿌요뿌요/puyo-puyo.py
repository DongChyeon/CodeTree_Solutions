n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

block_count = 0
max_block_size = 0
explode_block_count = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, color):
    return in_range(x, y) and not visited[y][x] and grid[y][x] == color

def dfs(x, y, color):
    global block_count

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, color):
            visited[ny][nx] = True
            block_count += 1
            dfs(nx, ny, color)

for y in range(n):
    for x in range(n):
        if in_range(x, y) and not visited[y][x]:
            block_count = 1
            visited[y][x] = True
            dfs(x, y, grid[y][x])

            if block_count > max_block_size:
                max_block_size = block_count

            if block_count >= 4:
                explode_block_count += 1

print(explode_block_count, max_block_size)