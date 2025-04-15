n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) * n for _ in range(n)]

x, y = c - 1, r - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited_nums = [grid[y][x]]
while True:
    direction_idx = 0
    can_go = False
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if in_range(nx, ny) and grid[ny][nx] > grid[y][x]:
            can_go = True
            visited_nums.append(grid[ny][nx])
            x, y = nx, ny
            break

    if not can_go:
        break

print(' '.join(map(str, visited_nums)))
