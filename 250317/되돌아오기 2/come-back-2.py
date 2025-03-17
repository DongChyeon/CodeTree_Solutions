def solution(inst):
    x, y = 0, 0

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    cur_idx = 0

    for i in range(len(inst)):
        if inst[i] == 'L':
            cur_idx = (cur_idx - 1 + 4) % 4
        elif inst[i] == 'R':
            cur_idx = (cur_idx + 1) % 4
        elif inst[i] == 'F':
            x += dx[cur_idx]
            y += dy[cur_idx]
            
            if x == 0 and y == 0:
                return i + 1

    return -1 

inst = input()

print(solution(inst))