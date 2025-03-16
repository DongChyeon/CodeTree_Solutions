def is_in_range(x, y, n):
    if x > n - 1 or x < 0:
        return False
    if y > n - 1 or y < 0:
        return False

    return True

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0

for y in range(n):
    for x in range(n):
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_in_range(nx, ny, n) and grid[ny][nx] == 1:
                count += 1
        if count >= 3:
            answer += 1

print(answer)