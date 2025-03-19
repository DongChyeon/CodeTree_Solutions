from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_pos = [
    (j, i)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 3
]
step = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

queue = deque([])
visited = [[False] * n for _ in range(n)]

for pos in start_pos:
    x, y = pos
    queue.append((0, x, y))
    visited[y][x] = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    second, x, y = queue.popleft()
    
    if grid[y][x] == 2:
        step[y][x] = second

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if in_range(nx, ny) and not visited[ny][nx] and grid[ny][nx] != 1:
            visited[ny][nx] = True
            queue.append((second + 1, nx, ny))

for y in range(n):
    for x in range(n):
        if grid[y][x] == 2 and not visited[y][x]:
            print(-1, end=' ')
        else:
            print(step[y][x], end=' ')
    print()
