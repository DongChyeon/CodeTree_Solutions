n, m, c = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def get_combinations(n, count):
    thing_combinations = []
    thing_comb = []

    def choose_thing(depth, start, n):
        if depth == count:
            thing_combinations.append(thing_comb[:])
            return
        for i in range(n):
            thing_comb.append(i)
            choose_thing(depth + 1, i, n)
            thing_comb.pop()
    choose_thing(0, 0, n)

    return thing_combinations

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def calc(thiefs_x, thiefs_y):
    value = 0
    
    for i in range(2):
        weight = 0
        for j in range(m):
            if in_range(thiefs_x[i] + j, thiefs_y[i]) and weight + things[thiefs_y[i]][thiefs_x[i] + j] <= c:
                weight += things[thiefs_y[i]][thiefs_x[i] + j]
                value += things[thiefs_y[i]][thiefs_x[i] + j] ** 2
            else:
                break

    return value

combinations = get_combinations(n, 2)
for comb in combinations:
    thief1_y, thief2_y = comb
    
    for thief1_x, thief2_x in combinations:
        thiefs_x = [thief1_x, thief2_x]
        thiefs_y = [thief1_y, thief2_y]

        if thief1_y == thief2_y:
            if abs(thief1_x - thief2_x) < m:
                continue
            answer = max(answer, calc(thiefs_x, thiefs_y))
        else:
            answer = max(answer, calc(thiefs_x, thiefs_y))

print(answer)