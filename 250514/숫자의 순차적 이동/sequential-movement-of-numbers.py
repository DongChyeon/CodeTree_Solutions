n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max_val_pos(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    max_val = 0
    max_val_pos = (0, 0)

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            if grid[ny][nx] > max_val:
                max_val = grid[ny][nx]
                max_val_pos = (nx, ny)

    return max_val_pos

def swap_number(num):
    for y in range(n):
        for x in range(n):
            if grid[y][x] == num:
                max_val_x, max_val_y = find_max_val_pos(x, y)
                grid[y][x], grid[max_val_y][max_val_x] = grid[max_val_y][max_val_x], grid[y][x]
                return

def simulate():
    for num in range(1, (n * n) + 2):
        swap_number(num)

for _ in range(m):
    simulate()

for row in grid:
    for col in row:
        print(col, end=' ')
    print()