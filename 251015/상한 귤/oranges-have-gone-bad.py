from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
answer = [[-1 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

queue = deque([])
for y in range(n):
    for x in range(n):
        if grid[y][x] == 2:
            visited[y][x] = True
            queue.append((x, y, 0))

while queue:
    x, y, sec = queue.popleft()
    answer[y][x] = sec

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and not visited[ny][nx] and grid[ny][nx] == 1:
            visited[ny][nx] = True
            queue.append((nx, ny, sec + 1))

for y in range(n):
    for x in range(n):
        if answer[y][x] == -1 and grid[y][x] == 1:
            print(-2, end=' ')
        else:
            print(answer[y][x], end=' ')
    print()
