n, m = map(int, input().split())
nx, mx = [], []

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        nx.append(v)

for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        mx.append(v)

answer = 0

ax, bx = nx[0], mx[0]

a_is_head = ax > bx
a_is_tail = ax < bx

for i in range(1, len(nx)):
    ax += nx[i]
    bx += mx[i]

    if ax > bx:
        if a_is_tail:
            answer += 1
        a_is_head = True
        a_is_tail = False
    elif ax < bx:
        if a_is_head:
            answer += 1
        a_is_tail = True
        a_is_head = False

print(answer)
        