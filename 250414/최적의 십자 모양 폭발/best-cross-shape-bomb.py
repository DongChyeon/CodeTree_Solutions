n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
new_grid = [[0] * n for _ in range(n)]

answer = 0

def print_grid():
    for row in new_grid:
        for col in row:
            print(col, end=' ')
        print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def copy_grid():
    for y in range(n):
        for x in range(n):
            new_grid[y][x] = grid[y][x]

def explosion(x, y, bomb_range):
    for col in range(x - bomb_range + 1, x + bomb_range):
        if in_range(col, y):
            new_grid[y][col] = 0
    for row in range(y - bomb_range + 1, y + bomb_range):
        if in_range(x, row):
            new_grid[row][x] = 0

def drop():
    for col in range(n):
        temp = [
            new_grid[row][col]
            for row in range(n)
            if new_grid[row][col] != 0
        ]

        for row in range(n - len(temp)):
            new_grid[row][col] = 0
        for row in range(n - len(temp), n):
            new_grid[row][col] = temp[row - (n - len(temp))]

def check():
    global answer

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    count = 0

    for y in range(n):
        for x in range(n):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not in_range(nx, ny) or new_grid[y][x] == 0 or new_grid[ny][nx] == 0:
                    continue

                if new_grid[y][x] == new_grid[ny][nx]:
                    count += 1

    answer = max(answer, count // 2)

for y in range(n):
    for x in range(n):
        copy_grid()
        explosion(x, y, new_grid[y][x])
        drop()
        check()

print(answer)