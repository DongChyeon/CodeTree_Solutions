n, m = map(int, input().split())
grid = [[''] * m for _ in range(n)]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

x, y = 0, 0
alphabet_index = 0

# 동 남 서 북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction_index = 0

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n and grid[y][x] == ''

grid[y][x] = alphabets[alphabet_index]

for _ in range(n * m - 1):
    while True:
        nx, ny = x + dx[direction_index], y + dy[direction_index]

        if in_range(nx, ny):
            x, y = nx, ny
            alphabet_index = (alphabet_index + 1) % 26
            grid[y][x] = alphabets[alphabet_index]
            break
        else:
            direction_index = (direction_index + 1) % 4

for row in grid:
    for col in row:
        print(col, end=' ')
    print()