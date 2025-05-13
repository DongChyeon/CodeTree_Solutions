from collections import deque

def solution():
    n, m, k = map(int, input().split())
    tail_length = 0
    tail_pos = deque([])

    grid = [[0 for _ in range(n)] for _ in range(n)]
    grid[0][0] = 1
    x, y = 0, 0

    answer = 0 

    for _ in range(m):
        r, c = map(int, input().split())
        grid[r - 1][c - 1] = 2

    def print_grid():
        for row in grid:
            for col in row:
                print(col, end=' ')
            print()
        print()

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    direction_mapper = {
        'U': 0,
        'D': 1,
        'L': 2,
        'R': 3
    }

    for _ in range(k):
        direction, distance = input().split()
        distance = int(distance)
        
        for _ in range(distance):
            #print_grid()
            answer += 1
            nx, ny = x + dx[direction_mapper[direction]], y + dy[direction_mapper[direction]]

            if not in_range(nx, ny):
                return answer
            elif grid[ny][nx] == 2:
                grid[ny][nx] = 1
                tail_length += 1
                tail_pos.append((x, y))
                x, y = nx, ny
            else:
                if tail_length == 0:
                    grid[y][x] = 0
                else:
                    tail_x, tail_y = tail_pos.popleft()
                    grid[tail_y][tail_x] = 0
                    tail_pos.append((x, y))

                if grid[ny][nx] == 1:
                    return answer

                grid[ny][nx] = 1
                x, y = nx, ny
                
    return answer

print(solution())