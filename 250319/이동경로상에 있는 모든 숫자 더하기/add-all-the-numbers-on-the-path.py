N, T = map(int, input().split())
instructions = input()
board = [list(map(int, input().split())) for _ in range(N)]

x, y = (N - 1) // 2, (N - 1) // 2
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir_idx = 0

answer = board[y][x]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for inst in instructions:
    if inst == 'L':
        dir_idx = (dir_idx - 1 + 4) % 4
    elif inst == 'R':
        dir_idx = (dir_idx + 1) % 4
    elif inst == 'F':
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        if in_range(nx, ny):
            x, y = nx, ny
            answer += board[y][x]

print(answer)