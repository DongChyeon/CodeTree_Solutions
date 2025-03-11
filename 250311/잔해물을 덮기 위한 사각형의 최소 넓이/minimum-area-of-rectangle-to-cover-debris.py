x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

field = [[0] * 2001 for _ in range(2001)]
offset = 1000

# Please write your code here.
for y in range(y1[0] + offset, y2[0] + offset + 1):
    for x in range(x1[0] + offset, x2[0] + offset + 1):
        field[y][x] = 1

for y in range(y1[1] + offset, y2[1] + offset + 1):
    for x in range(x1[1] + offset, x2[1] + offset + 1):
        field[y][x] = 2

answer = 0

max_x = 0
min_y = 2001

for y in range(y2[0] + offset, y1[0] + offset - 1, -1):
    for x in range(x1[0] + offset, x2[0] + offset + 1):
        if field[y][x] == 1:
            max_x = max(max_x, x)
            min_y = min(min_y, y)

print((max_x - offset - x1[0]) * (y2[0] - (min_y - offset)))
