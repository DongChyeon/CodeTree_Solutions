n, m, t, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]

direction = ['None']
velocity = [0]

direction_mapper = {
    'U': 0,
    'L': 1,
    'D': 2,
    'R': 3
}

def print_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
    print()

for num in range(1, m + 1):
    r, c, d, v = input().split()
    r = int(r) - 1
    c = int(c) - 1

    grid[r][c].append(num)

    direction.append(direction_mapper[d])
    velocity.append(int(v))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def change_direction(d):
    return (d + 2) % 4

def move(r, c, num):
    # U, L, D, R
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    x, y = c, r
    for _ in range(velocity[num]):
        nx, ny = x + dx[direction[num]], y + dy[direction[num]]

        if in_range(nx, ny):
            x, y = nx, ny
        else:
            direction[num] = change_direction(direction[num])
            x, y = x + dx[direction[num]], y + dy[direction[num]]

    return x, y

def simulate():
    new_grid = [[[] for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            for ball in grid[r][c]:           
                x, y = move(r, c, ball)
                new_grid[y][x].append(ball)

    for r in range(n):
        for c in range(n):
            sorted_marbles = sorted(
                new_grid[r][c],
                key=lambda idx: (-velocity[idx], -idx)
            )

            for idx in sorted_marbles[k:]:
                direction[idx] = 'None'
                velocity[idx] = 0
                new_grid[r][c].remove(idx)

    for r in range(n):
        for c in range(n):
            grid[r][c] = new_grid[r][c]

for _ in range(t):
    simulate()

answer = 0
for y in range(n):
    for x in range(n):
        answer += len(grid[y][x])

print(answer)