n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
answer = 0

def dfs(vertex):    
    global answer

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            answer += 1
            dfs(curr_v)

visited[1] = True
dfs(1)

print(answer)