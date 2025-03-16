n = int(input())

x, y = 0, 0
directions = ['W', 'S', 'N', 'E']
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(n):
    direction, distance = input().split()

    dir_idx = directions.index(direction)
    x += dx[dir_idx] * int(distance)
    y += dy[dir_idx] * int(distance)

print(x, y)