from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(0, x, y)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True

    while queue:
        second, x, y = queue.popleft()
        if grid[y][x] == 3:
            return second

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny) and not visited[ny][nx] and grid[y][x] != 1:
                visited[ny][nx] = True
                queue.append((second + 1, nx, ny))

    return -1

for y in range(n):
    for x in range(n):
        if grid[y][x] == 2:
            print(bfs(x, y), end=' ')
        else:
            print(0, end=' ')
    print()