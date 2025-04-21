n = int(input())
y, x = map(int, input().split())
y, x = y - 1, x - 1

dir_idx = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = [list(map(str, input())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
visited[y][x] = dir_idx

answer = 0

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
        # 같은 방향으로 해당 위치를 방문한 적이 있다면 -1 반환
        if visited[ny][nx] == dir_idx:
            answer = -1
            break

        # 이동 위치에 벽이 있다면 반시계 방향 회전
        if grid[ny][nx] == '#':
            if is_arounded_by_walls(x, y):
                answer = -1
                break
            rotate_left()
        # 이동 후 오른쪽에 벽이 없다면 시계 방향 회전 후 한칸 이동
        else:
            x, y = nx, ny
            visited[y][x] = dir_idx
            answer += 1
            
            if not is_wall_on_right(nx, ny):
                rotate_right()
                x, y = x + dx[dir_idx], y + dy[dir_idx]
                visited[y][x] = dir_idx
                answer += 1
    else:
        answer += 1
        break

print(answer)