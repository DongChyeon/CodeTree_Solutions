import copy

n, m, q = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

    temp1 = a[y1][x2]
    for x in range(x2, x1, -1):
        a[y1][x] = a[y1][x - 1]

    temp2 = temp1
    temp1 = a[y2][x2]
    for y in range(y2, y1, -1):
        a[y][x2] = a[y - 1][x2]
    a[y1 + 1][x2] = temp2

    temp2 = temp1
    temp1 = a[y2][x1]
    for x in range(x1, x2):
        a[y2][x] = a[y2][x + 1]
    a[y2][x2 - 1] = temp2

    temp2 = temp1
    temp1 = a[y1][x1]
    for y in range(y1, y2):
        a[y][x1] = a[y + 1][x1]
    a[y2 - 1][x1] = temp2

    updated_a = [[0] * (x2 - x1 + 1) for _ in range(y2 - y1 + 1)]

    for dy in range(y2 - y1 + 1):
        for dx in range(x2 - x1 + 1):
            x, y = x1 + dx, y1 + dy

            sum_of_value = a[y][x]
            divider = 1
            for i in range(4):
                nx, ny = x + dxs[i], y + dys[i]
                if in_range(nx, ny):
                    divider += 1
                    sum_of_value += a[ny][nx]

            updated_a[dy][dx] = sum_of_value // divider
    
    for dy in range(y2 - y1 + 1):
        for dx in range(x2 - x1 + 1):
            a[y1 + dy][x1 + dx] = updated_a[dy][dx]

for row in a:
    for col in row:
        print(col, end=' ')
    print()
    