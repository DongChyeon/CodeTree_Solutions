n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def traverse(x, y, w, h):
    dx = [1, -1, -1, 1]
    dy = [-1, -1, 1, 1]

    total = 0
    for i in range(4):
        if i % 2 == 0:
            for _ in range(w):
                nx, ny = x + dx[i], y + dy[i]
                if in_range(nx, ny):
                    x, y = nx, ny
                    total += grid[y][x]
                else:
                    return 0
        else:
            for _ in range(h):
                nx, ny = x + dx[i], y + dy[i]
                if in_range(nx, ny):
                    x, y = nx, ny
                    total += grid[y][x]
                else:
                    return 0
    
    return total

                
for y in range(n):
    for x in range(n):
        for w in range(1, n):
            for h in range(1, n):
                answer = max(answer, traverse(x, y, w, h))

print(answer)
