n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for y in range(n):
    for x in range(n - 2):
        count = 0
        for i in range(3):
            count += grid[y][x + i]
        answer = max(count, answer)

print(answer)