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

min_x, max_x, min_y, max_y = 2001, 0, 2001, 0
is_first_rect_exist = False

for y in range(y1[0] + offset, y2[0] + offset):
    for x in range(x1[0] + offset, x2[0] + offset):
        if field[y][x] == 1:
            is_first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if is_first_rect_exist:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
else:
    print(0)