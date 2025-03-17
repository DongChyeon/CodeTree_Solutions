n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

grid = [[0] * n for _ in range(n)]

def is_range(x, y):
    if x > n - 1 or x < 0:
        return False
    elif y > n - 1 or y < 0:
        return False

    return True

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

directions = ['U', 'R', 'L', 'D']

x, y = c - 1, r - 1

for i in range(t):
    nx, ny = x + dx[directions.index(d)], y + dy[directions.index(d)]
    if is_range(nx, ny):
        x, y = nx, ny
    else:
        d = directions[3 - directions.index(d)]

print(y + 1, x + 1)