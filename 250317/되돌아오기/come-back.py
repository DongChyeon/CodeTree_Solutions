def solution(n):
    x, y = 0, 0

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    mapper = {
        'W': 0,
        'S': 1,
        'N': 2,
        'E': 3,
    }

    time = 0

    for i in range(n):
        direction, distance = input().split()

        for _ in range(int(distance)):
            time += 1
            nx, ny = x + dx[mapper[direction]], y + dy[mapper[direction]]

            x, y = nx, ny
            
            if x == 0 and y == 0:
                return time

    return -1    

N = int(input())
print(solution(N))