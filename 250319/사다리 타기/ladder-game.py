n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key = lambda x : x[1])

def play_ladder(n, edges):
    temp = [0] * n
    for start in range(n):
        x_pos = start
        for edge in edges:
            if edge[0] - 1 == x_pos:
                x_pos = edge[0]
            elif edge[0] == x_pos:
                x_pos = edge[0] - 1
        temp[x_pos] = start
    
    return ''.join(map(str, temp))

goal = play_ladder(n, edges)

def get_combinations(n, m):
    ladder_combinations = []
   
    ladder_comb = []
    def choose_ladder(depth, start, n):
        if depth == n:
            ladder_combinations.append(ladder_comb[:])
            return
        for i in range(start, m):
            ladder_comb.append(edges[i])
            choose_ladder(depth + 1, i + 1, n)
            ladder_comb.pop()

    choose_ladder(0, 0, n)

    return ladder_combinations

find_answer = False
for i in range(0, m + 1):
    combinations = get_combinations(i, m)
    for comb in combinations:
        if play_ladder(n, comb) == goal:
            print(i)
            find_answer = True
            break
    if find_answer:
        break
