COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

T = int(input())
dir_mapper = { 'U': 0, 'D': 1, 'R': 2, 'L': 3 }
next_marbles_index = [[BLANK for _ in range(COORD_SIZE + 1)] for _ in range(COORD_SIZE + 1)]

marbles = []
next_marbles = []

last_collision_time = -1

def move(marble):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x, y, w, dir_idx, num = marble
    nx, ny = x + dx[dir_idx], y + dy[dir_idx]

    return (nx, ny, w, dir_idx, num)

def find_duplicate_marble(marble):
    target_x, target_y, _, _, _ = marble

    return next_marbles_index[target_y][target_x]

def collide(marble1, marble2):
    _, _, weight1, _, num1 = marble1
    _, _, weight2, _, num2 = marble2

    if weight1 > weight2 or (weight1 == weight2 and num1 > num2):
        return marble1
    else:
        return marble2

def is_out_of_active_coordinate(marble):
    x, y, _, _, _ = marble
    return x < 0 or x > COORD_SIZE or y < 0 or y > COORD_SIZE

def push_next_marble(marble, curr_time):
    global last_collision_time

    if is_out_of_active_coordinate(marble):
        return

    index = find_duplicate_marble(marble)

    if index == BLANK:
        next_marbles.append(marble)

        x, y, _, _, _ = marble
        next_marbles_index[y][x] = len(next_marbles) - 1
    else:
        next_marbles[index] = collide(next_marbles[index], marble)
        last_collision_time = curr_time

for _ in range(T):
    N = int(input())
    last_collision_time = -1

    # 위치 초기화
    for i in range(N):
        xi, yi, wi, di = input().split()
        
        dir_idx = dir_mapper[di]
        x = int(xi) * 2 + OFFSET
        y = int(yi) * 2 + OFFSET
        w = int(wi)

        marbles.append((x, y, w, dir_idx, i + 1))

    for t in range(1, COORD_SIZE + 1):
        for marble in marbles:
            next_marble = move(marble)
            push_next_marble(next_marble, t)

        marbles = next_marbles[:]

        for x, y, _, _, _ in next_marbles:
            next_marbles_index[y][x] = BLANK

        next_marbles = []

    print(last_collision_time)