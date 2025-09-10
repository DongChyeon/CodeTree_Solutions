n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

people_num = 0
people_nums = list()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[y][x] or grid[y][x] == 0:
        return False

    return True

def dfs(x, y):
    global people_num

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[ny][nx] = True
            people_num += 1
            dfs(nx, ny)

for y in range(n):
    for x in range(n):
        if can_go(x, y):
            visited[y][x] = True
            people_num = 1

            dfs(x, y)

            people_nums.append(people_num)

print(len(people_nums))
for num in sorted(people_nums):
    print(num)