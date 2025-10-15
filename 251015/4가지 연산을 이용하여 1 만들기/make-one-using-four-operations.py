from collections import deque

N = int(input())
MAX = 2 * N + 2
visited = [False] * MAX
visited[N] = True

def bfs():
    queue = deque([(N, 0)])

    while queue:
        num, cnt = queue.popleft()
        if num == 1:
            return cnt

        if num % 3 == 0:
            nxt = num // 3
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, cnt + 1))

        if num % 2 == 0:
            nxt = num // 2
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, cnt + 1))

        nxt = num - 1
        if nxt >= 0 and not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, cnt + 1))

        nxt = num + 1
        if nxt < MAX and not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, cnt + 1))
        
    return -1

print(bfs())