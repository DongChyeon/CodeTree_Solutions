N = int(input())
arr = [int(input()) for _ in range(N)]

count = 1
is_last_number_positive = arr[0] > 0

answer = 1

for i in range(1, N):
    if is_last_number_positive == (arr[i] > 0):
        count += 1
        answer = max(answer, count)
    else:
        count = 1
        is_last_number_positive = (arr[i] > 0)

print(answer)