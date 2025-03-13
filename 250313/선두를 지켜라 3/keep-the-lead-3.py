N, M = map(int, input().split())

dx_a = []
dx_b = []

for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        dx_a.append(v)

for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        dx_b.append(v)

ax = [dx_a[0]]
bx = [dx_b[0]]

# 0: A가 선두 / 1: B가 선두 / 2: A, B 동시 선두
comb = 0
if ax > bx:
    comb = 0
elif ax < bx:
    comb = 1
else:
    comb = 2

answer = 1

for i in range(1, len(dx_a)):
    cur_a = ax[i - 1] + dx_a[i]
    cur_b = bx[i - 1] + dx_b[i]

    new_comb = 0
    if cur_a > cur_b:
        new_comb = 0
    elif cur_a < cur_b:
        new_comb = 1
    else:
        new_comb = 2

    if comb != new_comb:
        comb = new_comb
        answer += 1

    ax.append(cur_a)
    bx.append(cur_b)

print(answer)