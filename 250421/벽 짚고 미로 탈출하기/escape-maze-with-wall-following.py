n = int(input())
y, x = map(int, input().split())
y, x = y - 1, x - 1

grid = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited[y][x] = True

answer = 0

dir_idx = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_arounded_by_walls(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not in_range(nx, ny) or grid[ny][nx] == '.':
            return False

    return True

def is_wall_on_right(x, y):
    temp_dir_idx = (dir_idx + 1) % 4
    nx, ny = x + dx[temp_dir_idx], y + dy[temp_dir_idx]

    return in_range(nx, ny) and grid[ny][nx] == '#'

def rotate_left():
    global dir_idx

    dir_idx = (dir_idx + 3) % 4

def rotate_right():
    global dir_idx

    dir_idx = (dir_idx + 1) % 4

while True:
    nx, ny = x + dx[dir_idx], y + dy[dir_idx]

    if in_range(nx, ny):
        # 이동 위치에 벽이 있다면 반시계 방향 회전
        if grid[ny][nx] == '#':
            if is_arounded_by_walls(x, y):
                answer = -1
                break
            rotate_left()

        # 이동 후 오른쪽에 벽이 없다면 시계 방향 회전 후 한칸 이동
        else:
            if visited[ny][nx]:
                answer = -1
                break

            x, y = nx, ny
            visited[y][x] = True
            answer += 1

            if not is_wall_on_right(nx, ny):
                rotate_right()
                x, y = x + dx[dir_idx], y + dy[dir_idx]
                visited[y][x] = True
                answer += 1
    else:
        answer += 1
        break

print(answer)