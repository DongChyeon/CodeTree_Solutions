n, m = map(int, input().split())
grid = [[False] * (n) for _ in range(n)]

def check(x, y):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 and n > ny >= 0 and grid[ny][nx]:
            count += 1
    
    if count == 3:
        return True
    else:
        return False

for _ in range(m):
    r, c = map(int, input().split())

    grid[r - 1][c - 1] = True

    if check(c - 1, r - 1):
        print(1)
    else:
        print(0)