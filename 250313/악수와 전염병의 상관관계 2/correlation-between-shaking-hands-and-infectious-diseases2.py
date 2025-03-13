N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda x: x[0])

answer = [0] * N
answer[P - 1] = 1
infection_counts = [K] * N

for t, x, y in handshakes:
    if answer[x - 1] == 1 and answer[y - 1] == 1:
        if infection_counts[x - 1] > 0:
            infection_counts[x - 1] -= 1
        if infection_counts[y - 1] > 0:
            infection_counts[y - 1] -= 1
    elif answer[x - 1] == 1 and infection_counts[x - 1] > 0:
        answer[y - 1] = 1
        infection_counts[x - 1] -= 1
    elif answer[y - 1] == 1 and infection_counts[y - 1] > 0:
        answer[x - 1] = 1
        infection_counts[y - 1] -= 1

for x in answer:
    print(x, end='')