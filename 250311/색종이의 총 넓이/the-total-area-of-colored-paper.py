n = int(input())
field = [[0] * 201 for _ in range(201)]

# Please write your code here.
offset = 100
for _ in range(n):
    x1, y1 = map(int, input().split())
    
    for y in range(y1 + offset , y1 + offset + 8):
        for x in range(x1 + offset, x1 + offset + 8):
            field[y][x] = 1

answer = 0
for row in field:
    for num in row:
        if num == 1:
            answer += 1

print(answer)