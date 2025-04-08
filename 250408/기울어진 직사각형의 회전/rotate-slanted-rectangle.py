from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, direction = map(int, input().split())

rect = deque([])
x, y = c - 1, r - 1
dx = [1, -1, -1, 1]
dy = [-1, -1, 1, 1]

vector = [m1, m2, m3, m4]
for i in range(len(vector)):
    for _ in range(vector[i]):
        x, y = x + dx[i], y + dy[i]
        rect.append(grid[y][x])

if (direction == 1):
    rect.rotate(-1)
else:
    rect.rotate(1)

idx = 0
for i in range(len(vector)):
    for _ in range(vector[i]):
        x, y = x + dx[i], y + dy[i]
        grid[y][x] = rect[idx]
        idx += 1

for row in grid:
    for col in row:
        print(col, end=' ')
    print()