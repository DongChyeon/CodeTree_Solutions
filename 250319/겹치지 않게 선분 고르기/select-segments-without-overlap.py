n = int(input())
x1, x2 = [], []
global answer

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

answer = 0
segment_combinations = []
segments = []

def choose_segment(depth, start, n):
    global answer
    answer = max(answer, len(segments))

    if depth == n:
        segment_combinations.append(list(segments))
        return

    visited = [False] * 1001
    for i in range(start, n):
        for segment in segments:
            for x in range(segment[0], segment[1] + 1):
                visited[x] = True

        is_overlap = False
        for x in range(x1[i], x2[i] + 1):
            if visited[x]:
                is_overlap = True
                break

        if not is_overlap:
            segments.append((x1[i], x2[i]))
            choose_segment(depth + 1, i + 1, n)
            segments.pop()

choose_segment(0, 0, n)

print(answer)