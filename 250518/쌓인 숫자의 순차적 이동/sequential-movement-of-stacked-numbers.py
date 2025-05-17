n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for y in range(n):
    for x in range(n):
        grid[y][x] = [grid[y][x]]
move_nums = list(map(int, input().split()))

def print_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
    print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max_val_pos(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    max_val = 0
    dir_idx = 0

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            if len(grid[ny][nx]) > 0 and max(grid[ny][nx]) > max_val:
                dir_idx = i
                max_val = max(grid[ny][nx])

    if max_val == 0:
        return (x, y)

    return (x + dx[dir_idx], y + dy[dir_idx])

def move(num):
    for y in range(n):
        for x in range(n):
            if num in grid[y][x]:
                nx, ny = find_max_val_pos(x, y)

                num_idx = grid[y][x].index(num)
                will_move_nums = grid[y][x][:num_idx + 1]

                for item in will_move_nums:
                    if item in grid[y][x]:
                        grid[y][x].remove(item)
                grid[ny][nx] = will_move_nums + grid[ny][nx]

                return

for num in move_nums:
    move(num)
    #print_grid()

for y in range(n):
    for x in range(n):
        if len(grid[y][x]) == 0:
            print('None')
        else:
            for num in grid[y][x]:
                print(num, end=' ')
            print()