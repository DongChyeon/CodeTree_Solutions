n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def turn_left(dir_idx):
    return (dir_idx + 3) % 4

def turn_right(dir_idx):
    return (dir_idx + 1) % 4 

def simulate(x, y, dir_idx):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    sec = 1
    while in_range(x, y):
        if grid[y][x] == 1:
            if dir_idx == 0 or dir_idx == 2:
                dir_idx = turn_right(dir_idx)
            else:
                dir_idx = turn_left(dir_idx)
        elif grid[y][x] == 2:
            if dir_idx == 0 or dir_idx == 2:
                dir_idx = turn_left(dir_idx)
            else:
                dir_idx = turn_right(dir_idx)

        x, y = x + dx[dir_idx], y + dy[dir_idx]

        sec += 1

    return sec

answer = 0

for dir_idx in range(2, 6):
    dir_idx = dir_idx % 4

    for i in range(n):
        answer = max(answer, simulate(i, n - 1, 0))
        answer = max(answer, simulate(0, i, 1))
        answer = max(answer, simulate(i, 0, 2))
        answer = max(answer, simulate(n - 1, i, 3))

print(answer)
