n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

count = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    count[r - 1][c - 1] = 1

for _ in range(t):
    new_count = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if count[y][x] == 1:
                next_dir = 0
                max_val = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if in_range(nx, ny) and grid[ny][nx] > max_val:
                        next_dir = i
                        max_val = grid[ny][nx]

                new_count[y + dy[next_dir]][x + dx[next_dir]] += 1

    for y in range(n):
        for x in range(n):
            if new_count[y][x] > 1:
                new_count[y][x] = 0

    for y in range(n):
        for x in range(n):
            count[y][x] = new_count[y][x]

answer = 0
for y in range(n):
    for x in range(n):
        if count[y][x] == 1:
            answer += 1

print(answer)