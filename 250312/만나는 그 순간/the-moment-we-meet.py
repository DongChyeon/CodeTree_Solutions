n, m = map(int, input().split())

a = []
for _ in range(n):
    direction, time = input().split()
    for _ in range(int(time)):
        a.append(direction)

b = []
for _ in range(m):
    direction, time = input().split()
    for _ in range(int(time)):
        b.append(direction)

ax, bx = 0, 0
iterate_count = max(len(a), len(b))
can_meet = False
for i in range(iterate_count):
    if i < len(a) - 1:
        if a[i] == 'L':
            ax -= 1
        elif a[i] == 'R':
            ax += 1

    if i < len(b) - 1:
        if b[i] == 'L':
            bx -= 1
        elif b[i] == 'R':
            bx += 1

    if ax == bx:
        print(i + 1)
        can_meet = True
        break

if not can_meet:
    print(-1)    
