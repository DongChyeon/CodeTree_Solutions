N, M, K = map(int, input().split())
penalty = [0] * (N + 1)
has_penalty = False

for _ in range(M):
    student_number = int(input())

    penalty[student_number] += 1
    if penalty[student_number] == K:
        has_penalty = True
        print(student_number)
        break

if not has_penalty:
    print(-1)