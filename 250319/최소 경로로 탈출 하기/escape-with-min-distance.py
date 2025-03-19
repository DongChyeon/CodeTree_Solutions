from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0, 0)])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        dist, x, y = queue.popleft()

        if x == m - 1 and y == n - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[ny][nx] and a[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((dist + 1, nx, ny))  
        
    return -1

print(bfs())
