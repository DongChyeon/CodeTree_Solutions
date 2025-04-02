n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def check(target_row, current_row):
    for i in range(m):
        if a[current_row][i] == a[target_row][i]:
            return True
    return False

def blow_wind(row, direction):
    if direction == 'L':
        temp = a[row][-1]
        for i in range(m - 1, 0, -1):
            a[row][i] = a[row][i - 1]
        a[row][0] = temp
    elif direction == 'R':
        temp = a[row][0]
        for i in range(0, m - 1):
            a[row][i] = a[row][i + 1]
        a[row][-1] = temp

for row, direction in winds:
    blow_wind(row - 1, direction)

    target_row = row - 1
    opposite_direction = 'L' if direction == 'R' else 'R'
    while target_row - 1 >= 0 and check(target_row - 1, target_row):
        target_row -= 1
        blow_wind(target_row, opposite_direction)
        opposite_direction = 'L' if opposite_direction == 'R' else 'R'

    target_row = row - 1
    opposite_direction = 'L' if direction == 'R' else 'R'
    while target_row + 1 <= n - 1 and check(target_row + 1, target_row):
        target_row += 1
        blow_wind(target_row, opposite_direction)
        opposite_direction = 'L' if opposite_direction == 'R' else 'R'
    
for row in a:
    for col in row:
        print(col, end=' ')
    print()