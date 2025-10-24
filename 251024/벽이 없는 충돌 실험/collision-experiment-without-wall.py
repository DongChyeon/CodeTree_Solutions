from collections import defaultdict

T = int(input())
dir_mapper = { 'U': 0, 'D': 1, 'R': 2, 'L': 3 }
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(T):
    N = int(input())
    positions = {}

    for i in range(N):
        xi, yi, wi, di = input().split()
        
        dir_idx = dir_mapper[di]
        x = int(xi) * 2
        y = int(yi) * 2
        w = int(wi)

        positions[(x, y)] = (w, i, dir_idx) # 무게, 순서, 방향

    answer = 0
    for t in range(1, 4001):
        new_positions = defaultdict(list)
        for (x, y), (w, seq, dir_idx) in positions.items():
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]
            new_positions[(nx, ny)].append((w, seq, dir_idx))

        positions.clear()
        for (nx, ny), lst in new_positions.items():
            if len(lst) > 1:
                answer = t
                w, seq, dir_idx = max(lst, key = lambda b: (b[0], b[1]))
                positions[(nx, ny)] = (w, seq, dir_idx)
            else:
                positions[(nx, ny)] = lst[0]

    if answer > 0:
        print(answer)

    if answer == 0:
        print(-1)