n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

block_row = 0
for x in range(k - 1, k - 1 + m):
    grid[block_row][x] = 1

def can_go_down(k, m, row):
    if row == n - 1:
        return False

    for x in range(k - 1, k - 1 + m):
        if grid[row + 1][x] == 1:
            return False

    return True

while True:
    if can_go_down(k, m, block_row):
        block_row += 1
        for x in range(k - 1, k - 1 + m):
            grid[block_row - 1][x] = 0
            grid[block_row][x] = 1
    else:
        break

for row in grid:
    for col in row:
        print(col, end=' ')
    print()