n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)

visited = [False] * n
answer = 0

def dfs(vertex):    
    global answer

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            if curr_v != 0:
                answer += 1
            visited[curr_v] = True
            dfs(curr_v)

dfs(0)
print(answer)