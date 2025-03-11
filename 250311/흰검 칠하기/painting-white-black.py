n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# 1: 흰색 / 2: 검은색 / 3: 회색
tiles = [[] for _ in range(200001)]
cur_idx = 5000

for i in range(n):
    direction = dir[i]
    dx = x[i]
    for j in range(dx):
        if direction == 'L':
            tiles[cur_idx].append('W')
            if j != dx - 1:
                cur_idx -= 1
        else:
            tiles[cur_idx].append('B')
            if j != dx - 1:
                cur_idx += 1

white = 0
black = 0
grey = 0

for tile in tiles:
    if len(tile) == 0:
        continue

    white_count = 0
    black_count = 0
    last_tile_color = tile[-1]

    for color in tile[::-1]:
        if color == 'W':
            white_count += 1
        else:
            black_count += 1

    if white_count >= 2 and black_count >= 2:
        grey += 1
    else:
        if last_tile_color == 'W':
            white += 1
        else:
            black += 1

print(white, black, grey)