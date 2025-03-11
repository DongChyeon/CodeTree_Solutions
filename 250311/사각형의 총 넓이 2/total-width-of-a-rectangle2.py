n = int(input())
offset = 100
field = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = 1

answer = 0
for row in field:
    for num in row:
        if num == 1:
            answer += 1

print(answer)