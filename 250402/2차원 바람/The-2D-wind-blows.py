import copy

n, m, q = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def rotate(start_row, start_col, end_row, end_col):
    temp = a[start_row][start_col]

    for row in range(start_row, end_row):
        a[row][start_col] = a[row + 1][start_col]

    for col in range(start_col, end_col):
        a[end_row][col] = a[end_row][col + 1]

    for row in range(end_row, start_row, -1):
        a[row][end_col] = a[row - 1][end_col]

    for col in range(end_col, start_col, -1):
        a[start_row][col] = a[start_row][col - 1]

    a[start_row][start_col + 1] = temp

def get_average(x, y):
    sum_of_value = a[y][x]
    count = 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            count += 1
            sum_of_value += a[ny][nx]
        
    return sum_of_value // count

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

    rotate(y1, x1, y2, x2)

    updated_a = [[0] * (x2 - x1 + 1) for _ in range(y2 - y1 + 1)]

    for dy in range(y2 - y1 + 1):
        for dx in range(x2 - x1 + 1):
            x, y = x1 + dx, y1 + dy
            updated_a[dy][dx] = get_average(x, y)
    
    for dy in range(y2 - y1 + 1):
        for dx in range(x2 - x1 + 1):
            a[y1 + dy][x1 + dx] = updated_a[dy][dx]

for row in a:
    for col in row:
        print(col, end=' ')
    print()
    