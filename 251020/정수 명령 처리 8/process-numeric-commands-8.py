from collections import deque

N = int(input())
A = deque([])

for _ in range(N):
    line = input().split()
    if line[0] == "push_front":
        A.appendleft(int(line[1]))
    elif line[0] == "push_back":
        A.append(int(line[1]))
    elif line[0] == "pop_front":
        print(A.popleft())
    elif line[0] == "pop_back":
        print(A.pop())
    elif line[0] == "size":
        print(len(A))
    elif line[0] == "empty":
        if len(A) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == "front":
        print(A[0])
    elif line[0] == "back":
        print(A[-1])
