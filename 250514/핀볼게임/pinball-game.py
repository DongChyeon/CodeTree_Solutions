n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def turn_left(dir_idx):
    return (dir_idx + 3) % 4

def turn_right(dir_idx):
    return (dir_idx + 1) % 4 

def simulate(x, y, dir_idx):
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
        if dir_idx == 0:
            x, y = i, n - 1
        elif dir_idx == 1:
            x, y = 0, i
        elif dir_idx == 2:
            x, y = i, 0
        else:
            x, y = n - 1, i

        answer = max(simulate(x, y, dir_idx), answer)

print(answer)