n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
field = [0] * 101
for segment in segments:
    for i in range(segment[0], segment[1] + 1):
        field[i] += 1

print(max(field))