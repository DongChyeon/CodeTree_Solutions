n = int(input())
A = list(map(int, input().split()))

answer = 10000

for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i - j) * A[j]
    if dist < answer:
        answer = dist

print(answer)