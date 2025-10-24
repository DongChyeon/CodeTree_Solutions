n, m, t = map(int, input().split())

BLANK = -1
next_marble_index = [[BLANK for _ in range(n + 1)] for _ in range(n + 1)]

dir_mapper = { 'U': 0, 'L': 1, 'D': 2, 'R': 3 }

marbles = []
next_marbles = []

def print_grid():
    for row in next_marble_index:
        for col in row:
            print(col, end=' ')
        print()
    print()

def out_of_range(x, y):
    return x < 1 or x > n or y < 1 or y > n

def collide(marble1, marble2):
    num1, weight1, dir_idx1, x1, y1 = marble1
    num2, weight2, dir_idx2, x2, y2 = marble2

    if num1 > num2:
        return (num1, weight1 + weight2, dir_idx1, x1, y1)
    else:
        return (num2, weight1 + weight2, dir_idx2, x2, y2)

def move(marble):
    num, weight, dir_idx, x, y = marble

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    nx, ny = x + dx[dir_idx], y + dy[dir_idx]

    # 막다른 길이라면 방향 전환
    if out_of_range(nx, ny):
        dir_idx = (dir_idx + 2) % 4
        nx, ny = x, y
    
    if next_marble_index[ny][nx] != BLANK:
        marble = collide(marbles[next_marble_index[ny][nx]], (num, weight, dir_idx, nx, ny))
        next_marbles[next_marble_index[ny][nx]] = marble
    else:
        next_marbles.append((num, weight, dir_idx, nx, ny))
        next_marble_index[ny][nx] = len(next_marbles) - 1

for i in range(m):
    ri, ci, di, wi = input().split()
    x = int(ci)
    y = int(ri)
    w = int(wi)

    marbles.append((i + 1, w, dir_mapper[di], x, y))  # 번호, 무게, 방향, x, y 저장

for _ in range(t):
    for marble in marbles:
        move(marble)

    marbles = next_marbles[:]

    for _, _, _, x, y in next_marbles:
        next_marble_index[y][x] = BLANK

    next_marbles = []

print(len(marbles), max(marbles, key=lambda x: x[1])[1])