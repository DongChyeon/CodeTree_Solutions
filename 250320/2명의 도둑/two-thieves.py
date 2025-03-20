n, m, c = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def get_combinations_with_repetition(n, count):
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

def get_combinations(n, count):
    thing_combinations = []
    thing_comb = []

    def choose_thing(depth, start, n):
        if depth == count:
            thing_combinations.append(thing_comb[:])
            return
        for i in range(start, n):
            thing_comb.append(i)
            choose_thing(depth + 1, i + 1, n)
            thing_comb.pop()
    choose_thing(0, 0, n)

    return thing_combinations

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def calc(thiefs_y):
    max_val = 0

    thiefs_x_combinations = []
    for i in range(1, m + 1):
        for comb in get_combinations(n, i):
            if comb[-1] - comb[0] < m:
                thiefs_x_combinations.append(comb)

    for comb_1 in thiefs_x_combinations:
        for comb_2 in thiefs_x_combinations:
            visited = [[False] * n for _ in range(n)]

            weight = 0
            for x_1 in comb_1:
                if in_range(x_1, thiefs_y[0]) and weight + things[thiefs_y[0]][x_1] <= c and not visited[thiefs_y[0]][x_1]:
                    visited[thiefs_y[0]][x_1] = True
                    weight += things[thiefs_y[0]][x_1]

            weight = 0
            for x_2 in comb_2:
                if in_range(x_2, thiefs_y[1]) and weight + things[thiefs_y[1]][x_2] <= c and not visited[thiefs_y[1]][x_2]:
                    visited[thiefs_y[1]][x_2] = True
                    weight += things[thiefs_y[1]][x_2]

            value = 0
            for y in range(n):
                for x in range(n):
                    if visited[y][x]:
                        value += things[y][x] ** 2

            max_val = max(max_val, value)
            
    return max_val

combinations = get_combinations_with_repetition(n, 2)
for comb in combinations:
    answer = max(answer, calc(comb))

print(answer)