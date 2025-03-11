x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

field = [[0] * 2001 for _ in range(2001)]
offset = 1000

# Please write your code here.
for y in range(y1[0] + offset, y2[0] + offset):
    for x in range(x1[0] + offset, x2[0] + offset):
        field[y][x] = 1

for y in range(y1[1] + offset, y2[1] + offset):
    for x in range(x1[1] + offset, x2[1] + offset):
        field[y][x] = 2

max_x = 0
max_y = 0

for y in range(y1[0] + offset, y2[0] + offset):
    for x in range(x1[0] + offset, x2[0] + offset):
        if field[y][x] == 1:
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print((max_x - offset - 1) * (max_y - offset))