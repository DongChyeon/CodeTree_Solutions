x, y = 0, 0

dir_num = 3
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for direction in input():
    if direction == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif direction == 'R':
        dir_num = (dir_num + 1) % 4
    elif direction == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
