# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
direction = input()

# Please write your code here.
if direction == 'L' or direction == 'R':
    for row in range(4):
        temp = []

        if direction == 'L':
            i = 0
            while i < 4:
                if grid[row][i] == 0:
                    i += 1
                elif i < 3 and grid[row][i] == grid[row][i + 1]:
                    temp.append(grid[row][i] * 2)
                    i += 2
                else:
                    temp.append(grid[row][i])
                    i += 1
        else:
            i = 3
            while i > -1:
                if grid[row][i] == 0:
                    i -= 1
                elif i > 0 and grid[row][i] == grid[row][i - 1]:
                    temp.append(grid[row][i] * 2)
                    i -= 2
                else:
                    temp.append(grid[row][i])
                    i -= 1
    
        if direction == 'L':
            while len(temp) < 4:
                temp.append(0)
            grid[row] = temp
        else:
            while len(temp) < 4:
                temp.append(0)
            grid[row] = temp[::-1]

else:
    for col in range(4):
        temp = []

        if direction == 'U':
            i = 0
            while i < 4:
                if grid[i][col] == 0:
                    i += 1
                elif i < 3 and grid[i][col] == grid[i + 1][col]:
                    temp.append(grid[i][col] * 2)
                    i += 2
                else:
                    temp.append(grid[i][col])
                    i += 1
        else:
            i = 3
            while i > -1:
                if grid[i][col] == 0:
                    i -= 1
                elif i > 0 and grid[i][col] == grid[i - 1][col]:
                    temp.append(grid[i][col] * 2)
                    i -= 2
                else:
                    temp.append(grid[i][col])
                    i -= 1
    
        if direction == 'U':
            while len(temp) < 4:
                temp.append(0)
            for i in range(4):
                grid[i][col] = temp[i]
        else:
            while len(temp) < 4:
                temp.append(0)
            for i in range(4):
                grid[i][col] = temp[i][::-1]

for row in grid:
    for col in row:
        print(col, end=' ')
    print()
