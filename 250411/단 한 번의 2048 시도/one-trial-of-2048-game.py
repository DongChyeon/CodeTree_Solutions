NONE = -1

n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

def rotate():
    for y in range(n):
        for x in range(n):
            next_grid[y][x] = 0

    for y in range(n):
        for x in range(n):
            next_grid[y][x] = grid[n - x - 1][y]

    for y in range(n):
        for x in range(n):
            grid[y][x] = next_grid[y][x]

def drop():
    for y in range(n):
        for x in range(n):
            next_grid[y][x] = 0

    for x in range(n):
        keep_num, next_row = NONE, n - 1

        for y in range(n - 1, -1, -1):
            if grid[y][x] == 0:
                continue

            if keep_num == NONE:
                keep_num = grid[y][x]
            elif keep_num == grid[y][x]:
                next_grid[next_row][x] = keep_num * 2
                keep_num = NONE

                next_row -= 1
            else:
                next_grid[next_row][x] = keep_num
                keep_num = grid[y][x]

                next_row -= 1

        if keep_num != NONE:
            next_grid[next_row][x] = keep_num
            next_row -= 1

    for y in range(n):
        for x in range(n):
            grid[y][x] = next_grid[y][x]

def tilt(move_direction):
    direction_mapper = {
        'D': 0,
        'R': 1,
        'U': 2,
        'L': 3
    }

    for _ in range(direction_mapper[move_direction]):
        rotate()

    drop()

    for _ in range(4 - direction_mapper[move_direction]):
        rotate()

direction = input()
tilt(direction)

for row in grid:
    for col in row:
        print(col, end=' ')
    print()
