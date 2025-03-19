n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb_pos = [
    (j, i)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 1
]
dx = [
    [0, 0, 0, 0],
    [0, 1, 0, -1], 
    [1, 1, -1, -1]
]
dy = [ 
    [-2, -1, 1, 2],
    [-1, 0, 1, 0],
    [-1, 1, 1, -1]
]

bomb_combinations = []

bomb_comb = []
def choose_bomb(depth, n):
    if depth == n:
        bomb_combinations.append(list(bomb_comb))
        return
    for i in range(3):
        bomb_comb.append(i)
        choose_bomb(depth + 1, n)
        bomb_comb.pop()

answer = 0

choose_bomb(0, len(bomb_pos))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for bombs in bomb_combinations:
    destroyed = []

    for i in range(len(bomb_pos)):
        x, y = bomb_pos[i]
        destroyed.append((x, y))

        for j in range(4):
            nx, ny = x + dx[bombs[i]][j], y + dy[bombs[i]][j]
            if in_range(nx, ny):
                destroyed.append((nx, ny))

    answer = max(answer, len(set(destroyed)))
        
print(answer)