n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
arr[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# Please write your code here.
x, y = 0, 0
count = 1
dir_idx = 0

def in_range(x, y):
    if x < 0 or x > m - 1:
        return False
    if y < 0 or y > n - 1:
        return False
    return True

while True:
    nx, ny = x + dx[dir_idx], y + dy[dir_idx]
    if in_range(nx, ny) and arr[ny][nx] == 0:
        count += 1
        arr[ny][nx] = count
        x, y = nx, ny
    else:
        dir_idx = (dir_idx + 1) % 4
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]

        if not in_range(nx, ny) or arr[ny][nx] != 0:
            break

for row in arr:
    for col in row:
        print(col, end=' ')
    print()
