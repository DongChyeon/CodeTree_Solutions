n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for y in range(n - 2):
    for x in range(n - 2):
        count = 0
        for i in range(3):
            for j in range(3):
                count += grid[y + i][x + j]
        answer = max(answer, count)

print(answer)