import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = -sys.maxsize - 1

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def solution(x1, y1, w1, h1, x2, y2, w2, h2):
    visited = [[False] * m for _ in range(n)]

    for y in range(y1, y1 + h1):
        for x in range(x1, x1 + w1):
            if not in_range(x, y) or visited[y][x]:
                return -sys.maxsize - 1
            else:
                visited[y][x] = True

    for y in range(y2, y2 + h2):
        for x in range(x2, x2 + w2):
            if not in_range(x, y) or visited[y][x]:
                return -sys.maxsize - 1
            else:
                visited[y][x] = True

    return sum([
        grid[y][x]
        for y in range(n)
        for x in range(m)
        if visited[y][x]
    ])

for y1 in range(n):
    for x1 in range(m):
        for y2 in range(n):
            for x2 in range(m):
                for w1 in range(1, m + 1):
                    for h1 in range(1, n + 1):
                        for w2 in range(1, m + 1):
                            for h2 in range(1, n + 1):
                                answer = max(answer, solution(x1, y1, w1, h1, x2, y2, w2, h2))

print(answer)