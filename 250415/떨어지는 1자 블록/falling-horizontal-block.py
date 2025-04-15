n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_all_blank(row, start_col, end_col):
    return all([
        not grid[row][col]
        for col in range(start_col, end_col + 1)
    ])

def get_target_row():
    for row in range(n):
        if not is_all_blank(row, k - 1, k + m - 2):
            return row - 1

    return n - 1

block_row = get_target_row()
for col in range(k - 1, k - 1 + m):
    grid[block_row][col] = 1

for row in grid:
    for col in row:
        print(col, end=' ')
    print()