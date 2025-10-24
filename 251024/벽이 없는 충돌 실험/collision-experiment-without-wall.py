T = int(input())
dir_mapper = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}
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
        new_positions = { }
        for (x, y), balls in positions.items():
            w, seq, dir_idx = balls
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]

            if (nx, ny) not in new_positions:
                new_positions[(nx, ny)] = (w, seq, dir_idx)
            else:
                answer = t

                cur_w, cur_seq, cur_dir_idx = new_positions[(nx, ny)]
                if w > cur_w:
                    new_positions[(nx, ny)] = (w, seq, dir_idx)
                elif w == cur_w and seq > cur_seq:
                    new_positions[(nx, ny)] = (w, seq, dir_idx)
        positions = new_positions

    if answer > 0:
        print(answer)

    if answer == 0:
        print(-1)