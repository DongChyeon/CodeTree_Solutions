# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
direction = input()

# Please write your code here.
if direction == 'L' or direction == 'R':
    for row in range(4):
        numbers = [num for num in grid[row] if num != 0]
        temp = []

        if direction == 'L':
            i = 0
            while i < len(numbers):
                if numbers[i] == 0:
                    i += 1
                elif i < len(numbers) -1 and numbers[i] == numbers[i + 1]:
                    temp.append(numbers[i] * 2)
                    i += 2
                else:
                    temp.append(numbers[i])
                    i += 1
        else:
            i = len(numbers) - 1
            while i > -1:
                if grid[row][i] == 0:
                    i -= 1
                elif i > 0 and numbers[i] == numbers[i - 1]:
                    temp.append(numbers[i] * 2)
                    i -= 2
                else:
                    temp.append(numbers[i])
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
        numbers = [grid[row][col] for row in range(4) if grid[row][col] != 0]
        temp = []

        if direction == 'U':
            i = 0
            while i < len(numbers):
                if numbers[i] == 0:
                    i += 1
                elif i < len(numbers) -1 and numbers[i] == numbers[i + 1]:
                    temp.append(numbers[i] * 2)
                    i += 2
                else:
                    temp.append(numbers[i])
                    i += 1
        else:
            i = len(numbers) - 1
            while i > -1:
                if numbers[i] == 0:
                    i -= 1
                elif i > 0 and numbers[i] == numbers[i - 1]:
                    temp.append(numbers[i] * 2)
                    i -= 2
                else:
                    temp.append(numbers[i])
                    i -= 1
    
        if direction == 'U':
            while len(temp) < 4:
                temp.append(0)
            for i in range(4):
                grid[i][col] = temp[i]
        else:
            while len(temp) < 4:
                temp.append(0)
            temp = temp[::-1]
            for i in range(4):
                grid[i][col] = temp[i]

for row in grid:
    for col in row:
        print(col, end=' ')
    print()
