from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

INF = int(10e9)
answer = INF

walls = [
    (x, y)
    for y in range(n)
    for x in range(n)
    if grid[y][x] == 1
]

def solution(curr_depth, curr_walls, curr_start, goal_depth):
    global answer

    if curr_depth == goal_depth:
        bfs(curr_walls)
        return
    for i in range(curr_start, len(walls)):
        curr_walls.append(walls[i])
        solution(curr_depth + 1, curr_walls, i + 1, goal_depth)
        curr_walls.pop()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(destroyed_walls):
    global answer

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False] * n for _ in range(n)]

    queue = deque([(0, c1, r1)])
    visited[r1][c1] = True

    while queue:
        second, x, y = queue.popleft()
        if x == c2 and y == r2:
            answer = min(second, answer)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny) and (grid[ny][nx] == 0 or (nx, ny) in destroyed_walls) and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((second + 1, nx, ny))

for i in range(k + 1):
    solution(0, [], 0, i)

if answer == INF:
    print(-1)
else:
    print(answer)