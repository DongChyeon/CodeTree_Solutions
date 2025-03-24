n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for y in range(n):
    curr = grid[y][0]
    curr_cnt = 1

    if curr_cnt >= m:
        answer += 1
        continue

    for x in range(1, n):
        if grid[y][x] == curr:
            curr_cnt += 1
            if curr_cnt >= m:
                answer += 1
                break
        else:
            curr = grid[y][x]
            curr_cnt = 1

for x in range(n):
    curr = grid[0][x]
    curr_cnt = 1

    if curr_cnt >= m:
        answer += 1
        continue

    for y in range(1, n):
        if grid[y][x] == curr:
            curr_cnt += 1
            if curr_cnt >= m:
                answer += 1
                break
        else:
            curr = grid[y][x]
            curr_cnt = 1

print(answer)