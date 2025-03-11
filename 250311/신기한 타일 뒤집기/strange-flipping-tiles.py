n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# 1: 흰색 / 2: 검은색
tiles = [0] * 200001
cur_idx = 100001

for i in range(n):
    direction = dir[i]
    dx = x[i]
    for j in range(dx):
        if direction == 'L':
            tiles[cur_idx] = 1
            if j != dx - 1:
                cur_idx -= 1
        else:
            tiles[cur_idx] = 2
            if j != dx - 1:
                cur_idx += 1

print(tiles.count(1), tiles.count(2))
