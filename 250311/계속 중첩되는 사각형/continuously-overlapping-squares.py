n = int(input())
field = [[0] * 201 for _ in range(201)]
offset = 100

for i in range(n):
    a, b, c, d = map(int, input().split())
    is_red = i % 2 == 0

    for y in range(b + offset, d + offset):
        for x in range(a + offset, c + offset):
            if is_red:
                field[y][x] = 1
            else:
                field[y][x] = 2

answer = 0
for row in field:
    for color in row:
        if color == 2:
            answer += 1

print(answer)