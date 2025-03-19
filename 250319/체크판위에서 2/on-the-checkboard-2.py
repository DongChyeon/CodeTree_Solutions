R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
answer = 0

start_color = grid[0][0]
end_color = grid[R - 1][C - 1]

for y1 in range(1, R - 2):
    for x1 in range(1, C - 2):
        if grid[y1][x1] != start_color:
            for y2 in range(y1 + 1, R - 1):
                for x2 in range(x1 + 1, C - 1):
                    if grid[y2][x2] != end_color:
                        answer += 1

print(answer)