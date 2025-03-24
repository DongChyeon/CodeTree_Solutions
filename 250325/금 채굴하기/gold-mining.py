n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dig(x, y, k):
    visited = [[0] * n for _ in range(n)]

    global answer

    reward = 0

    for i in range(k + 1):
        if in_range(x, y - i):
            visited[y - i][x] = 1

        for j in range(1, k - i + 1):
            if in_range(x + j, y - i):
                visited[y - i][x + j] = 1
            if in_range(x - j, y - i):
                visited[y - i][x - j] = 1

    for i in range(1, k + 1):
        if in_range(x, y + i):
            visited[y + i][x] = 1

        for j in range(1, k - i + 1):
            if in_range(x + j, y + i):
                visited[y + i][x + j] = 1
            if in_range(x - j, y + i):
                visited[y + i][x - j] = 1            

    for y in range(n):
        for x in range(n):
            if visited[y][x] == 1 and grid[y][x] == 1:
                reward += m
    
    if reward >= k ** k + (k + 1) ** 2:
        if reward // m > answer:    
            answer = reward // m


for y in range(n):
    for x in range(n):
        for depth in range(n):
            dig(x, y, depth)

print(answer)