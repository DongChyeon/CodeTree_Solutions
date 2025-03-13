def move_to_direction(current_position, direction):
    position = current_position

    if direction == 'L':
        position -= 1
    else:
        position += 1

    return position

n, m = map(int, input().split())

dx_a, dx_b = [], []

for _ in range(n):
    time, direction = input().split()
    for _ in range(int(time)):
        dx_a.append(direction)

for _ in range(m):
    time, direction = input().split()
    for _ in range(int(time)):
        dx_b.append(direction)

ax, bx = [], []
ax.append(move_to_direction(0, dx_a[0]))
bx.append(move_to_direction(0, dx_b[0]))

answer = 0

iterate_count = max(len(dx_a), len(dx_b))
for i in range(1, iterate_count):

    if i < len(dx_a):
        a_position = move_to_direction(ax[i - 1], dx_a[i])
        ax.append(a_position)
    else:
        ax.append(ax[i - 1])
    
    if i < len(dx_b) - 1:
        b_position = move_to_direction(bx[i - 1], dx_b[i])
        bx.append(b_position)
    else:
        bx.append(bx[i - 1])

    if ax[i] == bx[i] and ax[i - 1] != bx[i - 1]:
        answer += 1

print(answer)
