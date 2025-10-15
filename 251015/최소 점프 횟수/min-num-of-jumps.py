from collections import deque

n = int(input())
num = list(map(int, input().split()))

def bfs():
    queue = deque([(0, 0)])
    while queue:
        pos, cnt = queue.popleft()
        if pos == n - 1:
            return cnt
        for i in range(num[pos], 0, -1):
            next_pos = pos + i
            queue.append((next_pos, cnt + 1))
    
    return -1

print(bfs())