def print_visited():
    for row in visited:
        for col in row:
            print(col, end=' ')
        print()

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

village_count = 0
people = []
curr_people_count = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global village_count
    global curr_people_count

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and visited[ny][nx] == 0 and grid[ny][nx] == 1:
            curr_people_count += 1
            visited[ny][nx] = village_count
            dfs(nx, ny)

for y in range(n):
    for x in range(n):
        if visited[y][x] == 0 and grid[y][x] == 1:
            if curr_people_count > 0: people.append(curr_people_count)
            curr_people_count = 1

            village_count += 1
            visited[y][x] = village_count

            dfs(x, y)

people.append(curr_people_count)

print(village_count)
for count in sorted(people):
    print(count)