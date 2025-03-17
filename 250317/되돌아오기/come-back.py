N = int(input())
x, y = 0, 0

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

mapper = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3,
}

def solution(n):
    time = 0

    direction, distance = input().split()

    for _ in range(int(distance)):
        time += 1
        nx, ny = x + dx[mapper[direction]], y + dy[mapper[direction]]

        x, y = nx, ny
        
        if x == 0 and y == 0:
            return time

    return -1    

print(solution(N))