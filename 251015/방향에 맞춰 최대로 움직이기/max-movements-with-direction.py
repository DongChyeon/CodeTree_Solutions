dirs = [(0,0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1) ]
answer = 0

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

visited[r - 1][c - 1] = True

def dfs(x, y, dir_num, move_num):
    global answer

    answer = max(answer, move_num)

    nx, ny = x, y
    dx, dy = dirs[dir_num]

    while True:
        nx, ny = nx + dx, ny + dy

        if not in_range(nx, ny):
            break

        if num[y][x] < num[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, move_dir[ny][nx], move_num + 1)
            visited[ny][nx] = False

dfs(c - 1, r - 1, move_dir[r - 1][c - 1], 0)

print(answer)
