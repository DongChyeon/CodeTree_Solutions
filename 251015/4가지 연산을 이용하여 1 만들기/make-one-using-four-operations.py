from collections import deque

N = int(input())
visited = [False] * (N + 1)
visited[N] = True

def in_range(num):
    return 0 <= num <= N

def bfs():
    queue = deque([(N, 0)])

    while queue:
        num, cnt = queue.popleft()
        if num == 1:
            return cnt

        if num % 3 == 0 and not visited[num // 3]:
            visited[num // 3] = True
            queue.append((num // 3, cnt + 1))
        if num % 2 == 0 and not visited[num // 2]:
            visited[num // 2] = True
            queue.append((num // 2, cnt + 1))
        if in_range(num - 1) and not visited[num - 1]:
            visited[num - 1] = True
            queue.append((num - 1, cnt + 1))
        if in_range(num + 1) and not visited[num + 1]:
            visited[num + 1] = True
            queue.append((num + 1, cnt + 1))
        
    return -1

print(bfs())