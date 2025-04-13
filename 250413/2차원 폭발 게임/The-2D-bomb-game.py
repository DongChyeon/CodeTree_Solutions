n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def print_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
    print()

def drop():
    for col in range(n):
        temp = [
            grid[row][col]
            for row in range(n)
            if grid[row][col] != 0
        ]

        for row in range(n - len(temp)):
            grid[row][col] = 0
        for row in range(n - len(temp), n):
            grid[row][col] = temp[row - (n - len(temp))]

def rotate():
    new_grid = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            new_grid[y][x] = grid[n - x - 1][y]

    for y in range(n):
        for x in range(n):
            grid[y][x] = new_grid[y][x]
    
    drop()

def get_last_index_of_value(start_index, col):
    value = grid[start_index][col]
    last_index = start_index

    while last_index < n - 1 and grid[last_index + 1][col] == value:
        last_index += 1
    
    return last_index

def explode(m):
    while True:
        has_explode = False
        
        for col in range(n):
            for i in range(n):
                if grid[i][col] == 0:
                    continue

                last_index = get_last_index_of_value(i, col)
            
                if last_index - i >= m - 1:
                    for row in range(i, last_index + 1):
                        grid[row][col] = 0
                    i = last_index + 1

                    has_explode = True
        drop()

        if not has_explode:
            break

for _ in range(k):
    explode(m)
    rotate()
explode(m)

answer = 0
for row in grid:
    for col in row:
        if col != 0:
            answer += 1
print(answer)