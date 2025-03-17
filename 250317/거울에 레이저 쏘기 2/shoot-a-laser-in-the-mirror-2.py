n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return n > x >= 0 and n > y >= 0

def init_location(k):
    dir_idx = 3
    count = 0
    x, y = 0, 0

    while True:
        count += 1
        if count == k:
            return (dir_idx + 1) % 4, x, y

        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        if in_range(nx, ny):
            x, y = nx, ny
        else:
            dir_idx = (dir_idx + 1) % 4

dir_idx, x, y = init_location(k)

def is_exit(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return True
    else:
        return False

def turn_left(dir_idx):
    return (dir_idx - 1 + 4) % 4

def turn_right(dir_idx):
    return (dir_idx + 1) % 4

answer = 0
while True:
    answer += 1

    if grid[y][x] == '/':
        if dir_idx == 3 or dir_idx == 1:
            dir_idx = turn_left(dir_idx)
        else:
            dir_idx = turn_right(dir_idx)
    elif grid[y][x] == "\\":
        if dir_idx == 0 or dir_idx == 2:
            dir_idx = turn_left(dir_idx)
        else:
            dir_idx = turn_right(dir_idx)

    x += dx[dir_idx]
    y += dy[dir_idx]

    if is_exit(x, y):
        break

print(answer)