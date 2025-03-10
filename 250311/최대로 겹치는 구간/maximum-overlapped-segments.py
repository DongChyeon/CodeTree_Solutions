n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

field = [0] * 201
for segment in segments:
    for i in range(segment[0] + 100, segment[1] + 100):
        field[i] += 1

print(max(field))