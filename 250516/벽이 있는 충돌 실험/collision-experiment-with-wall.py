t = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}

for _ in range(t):
    n, m = map(int, input().split())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    directions = [[-1 for _ in range(n)] for _ in range(n)]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def change_direction(dir_idx):
        return (dir_idx + 2) % 4
        
    for _ in range(m):
        xi, yi, di = input().split()
        x, y = int(xi) - 1, int(yi) - 1
        grid[x][y] = 1
        directions[x][y] = mapper[di]

    for _ in range(n * 2):
        new_grid = [[0 for _ in range(n)] for _ in range(n)]
        new_directions = [[-1 for _ in range(n)] for _ in range(n)]

        for y in range(n):
            for x in range(n):
                if grid[y][x] > 0:
                    dir_idx = directions[y][x]
                    nx, ny = x + dx[dir_idx], y + dy[dir_idx]

                    if not in_range(nx, ny):
                        new_grid[y][x] += 1
                        new_directions[y][x] = change_direction(dir_idx)
                    else:
                        new_grid[ny][nx] += 1
                        new_directions[ny][nx] = directions[y][x]

        for y in range(n):
            for x in range(n):
                if new_grid[y][x] > 1:
                    new_grid[y][x] = 0
                    new_directions[y][x] = -1
                grid[y][x] = new_grid[y][x]
                directions[y][x] = new_directions[y][x]

    answer = 0
    for row in grid:
        for col in row:
            if col > 0:
                answer += 1

    print(answer)    