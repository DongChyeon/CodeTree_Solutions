n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

best_val = [
    [-1] * (n - m + 1)
    for _ in range(n)
]

temp = list()
max_val = 0
answer = 0

def find_max_val(curr_depth, curr_weight, curr_val):
    global max_val

    if curr_depth == m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return

    find_max_val(curr_depth + 1, curr_weight, curr_val)

    find_max_val(curr_depth + 1, curr_weight + temp[curr_depth], curr_val + temp[curr_depth] ** 2)

def find_max(x, y):
    global temp, max_val

    if best_val[y][x] != -1:
        return best_val[y][x]

    temp = weight[y][x:x + m]

    max_val = 0
    find_max_val(0, 0, 0)

    best_val[y][x] = max_val
    
    return max_val

def intersect(start1, end1, start2, end2):
    return not (end1 < start2 or end2 < start1)

def is_posssible(x1, y1, x2, y2):
    if y1 != y2:
        return True

    if intersect(x1, x1 + m - 1, x2, x2 + m - 1):
        return False

    return False

for y1 in range(n):
    for x1 in range(n - m + 1):
        for y2 in range(2):
            for x2 in range(n - m + 1):
                if is_posssible(x1, y1, x2, y2):
                    answer = max(answer, find_max(x1, y1) + find_max(x2, y2))

print(answer)