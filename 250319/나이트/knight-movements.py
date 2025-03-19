from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    queue = deque([(0, c1 - 1, r1 - 1)])
    visited = [[False] * n for _ in range(n)]
    visited[r1 - 1][c1- 1] = True

    while queue:
        count, x, y = queue.popleft()
        if x == c2 - 1 and y == r2 - 1:
            return count

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[ny][nx]:
                queue.append((count + 1, nx, ny))
                visited[ny][nx] = True

    return -1

print(bfs())
