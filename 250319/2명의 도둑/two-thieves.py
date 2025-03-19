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

    visited = [[False] * n for _ in range(n)]
    
    for i in range(2):
        weight = 0
        for j in range(m):
            if in_range(thiefs_x[i] + j, thiefs_y[i]) and weight + things[thiefs_y[i]][thiefs_x[i] + j] <= c and not visited[thiefs_y[i]][thiefs_x[i] + j]:
                visited[thiefs_y[i]][thiefs_x[i] + j] = True
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

        answer = max(answer, calc(thiefs_x, thiefs_y))

print(answer)