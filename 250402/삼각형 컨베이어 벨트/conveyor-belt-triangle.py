n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = l + r + d

for _ in range(t):
    temp = belt[-1]
    for i in range(3 * n - 1, 0, -1):
        belt[i] = belt[i - 1]
    belt[0] = temp

print(' '.join(map(str, belt[:n])))
print(' '.join(map(str, belt[n:2 * n])))
print(' '.join(map(str, belt[2 * n:])))
