n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

num = grid[r - 1][c - 1]
for x in range(c - num, c + num - 1):
    if in_range(x, r - 1):
        grid[r - 1][x] = 0

for y in range(r - num, r + num - 1):
    if in_range(c - 1, y):
        grid[y][c - 1] = 0

for col in range(n):
    temp = []
    for row in range(n):
        if grid[row][col] != 0:
            temp.append(grid[row][col])

    for row in range(n - len(temp)):
        grid[row][col] = 0

    for row in range(n - len(temp), n):
        grid[row][col] = temp[row - (n - len(temp))]

for row in grid:
    for col in row:
        print(col, end=' ')
    print()