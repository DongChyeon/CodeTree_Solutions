n = int(input())
arr = [int(input()) for _ in range(n)]

last_number = arr[0]
count = 1
answer = 1

for i in range(1, len(arr)):
    if last_number == arr[i]:
        count += 1
        answer = max(answer, count)
    else :
        count = 1
        last_number = arr[i]

print(answer)