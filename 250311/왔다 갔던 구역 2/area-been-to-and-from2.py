n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

field = [0] * 2001
current_index = 1001

for i in range(n):
    direction = dir[i]
    dx = x[i]

    for j in range(dx):
        if direction == 'L':
            current_index -= 1
            field[current_index] += 1
        else:
            field[current_index] += 1
            current_index += 1
            
answer = 0
for area in field:
    if (area > 1):
        answer += 1

print(answer)
