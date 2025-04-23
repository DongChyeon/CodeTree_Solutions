from collections import deque

n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)]
directions = list(input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 두번쨰 인덱스가 아랫면
dice_horizontal = deque([4, 6, 3])
dice_vertical = deque([2, 6, 5, 1])

x, y = c - 1, r - 1
grid[y][x] = dice_horizontal[1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction_mapper = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3
}

for direction in directions:
    nx, ny = x + dx[direction_mapper[direction]], y + dy[direction_mapper[direction]]
    if in_range(nx, ny):
        x, y = nx, ny
        
        if direction == 'L':
            dice_horizontal.rotate(1)
            dice_vertical[1] = dice_horizontal[1]
            dice_horizontal[0], dice_vertical[3] = dice_vertical[3], dice_horizontal[0]
        elif direction == 'R':
            dice_horizontal.rotate(-1)
            dice_vertical[1] = dice_horizontal[1]
            dice_horizontal[2], dice_vertical[3] = dice_vertical[3], dice_horizontal[2]
        elif direction == 'U':
            dice_vertical.rotate(-1)
            dice_horizontal[1] = dice_vertical[1]
        elif direction == 'D':
            dice_vertical.rotate(1)
            dice_horizontal[1] = dice_vertical[1]

        #print(dice_horizontal)
        #print(dice_vertical)

        grid[y][x] = dice_horizontal[1]
            
answer = 0
for y in range(n):
    for x in range(n):
        #print(grid[y][x], end=' ')
        answer += grid[y][x]
    #print()

print(answer)
