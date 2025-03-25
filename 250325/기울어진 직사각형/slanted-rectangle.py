n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

dx = [1, -1, -1, 1]
dy = [-1, -1, 1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def traverse(x, y, k):
    global answer

    for length1 in range(1, k):
        visited = [[0] * n for _ in range(n)]
        visited[y][x] = 1

        length2 = k - length1

        can_establish = True
        for d in range(4):
            if d % 2 == 0:
                for _ in range(length1):
                    nx, ny = x + dx[d], y + dy[d]
                    if in_range(nx, ny):
                        x, y = nx, ny
                        visited[ny][nx] = 1
                    else:
                        can_establish = False
            else:
                for _ in range(length2):
                    nx, ny = x + dx[d], y + dy[d]
                    if in_range(nx, ny):
                        x, y = nx, ny
                        visited[ny][nx] = 1
                    else:
                        can_establish = False

        if can_establish:
            sum_of_value = sum([
                grid[y][x]
                for y in range(n)
                for x in range(n)
                if visited[y][x] == 1
            ])

            if sum_of_value > answer:
                answer = sum_of_value
                ''' print(x, y, sum_of_value, length1, length2)

                for row in visited:
                    for col in row:
                        print(col, end=' ')
                    print()
                print()'''
                
for y in range(n):
    for x in range(n):
        for k in range(2, n + 2):
            traverse(x, y, k)

print(answer)
