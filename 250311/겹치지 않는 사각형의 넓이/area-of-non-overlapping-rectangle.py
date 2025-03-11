field = [[0] * 2001 for _ in range(2001)]
offset = 1000

# Please write your code here.
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    
    for y in range(y1 + offset, y2 + offset):
        for x in range(x1 + offset, x2 + offset):
            field[y][x] = 1

x1, y1, x2, y2 = map(int, input().split())
for y in range(y1 + offset, y2 + offset):
    for x in range(x1 + offset, x2 + offset):
        field[y][x] = 0

answer = 0
for row in field:
    for num in row:
        if num == 1:
            answer += 1

print(answer)
