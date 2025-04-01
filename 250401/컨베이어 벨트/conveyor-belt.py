n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = u + d

for _ in range(t):
    temp = belt[-1]
    for i in range(2 * n - 1, 0, -1):
        belt[i] = belt[i - 1]
    belt[0] = temp

print(' '.join(map(str, belt[0:n])))
print(' '.join(map(str, belt[n::])))