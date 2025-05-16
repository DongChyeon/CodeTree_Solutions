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

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def change_direction(dir_idx):
        return (dir_idx + 2) % 4

    for _ in range(m):
        xi, yi, di = input().split()
        x, y = int(xi) - 1, int(yi) - 1
        grid[y][x] = 1 + mapper[di]

    for _ in range(n * 2):
        new_grid = [[0 for _ in range(n)] for _ in range(n)]

        for y in range(n):
            for x in range(n):
                if grid[y][x] > 0:
                    dir_idx = grid[y][x] - 1
                    nx, ny = x + dx[dir_idx], y + dy[dir_idx]
                    if not in_range(nx, ny):
                        new_grid[y][x] = change_direction(dir_idx) + 1
                    else:
                        if new_grid[ny][nx] > 0:
                            # 2개 이상 충돌할 시 -1로 마킹
                            new_grid[ny][nx] = -1
                        else:
                            new_grid[ny][nx] = grid[y][x]


        for y in range(n):
            for x in range(n):
                if new_grid[y][x] == -1:
                    new_grid[y][x] = 0
                grid[y][x] = new_grid[y][x]

    answer = 0
    for row in grid:
        for col in row:
            if col > 0:
                answer += 1

    print(answer)    