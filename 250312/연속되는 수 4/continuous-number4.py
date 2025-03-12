n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
count = 1
last_number = arr[0]
answer = 0

for i in range(1, n):
    if arr[i] > last_number:
        count += 1
        answer = max(answer, count)
    else:
        count = 1
    last_number = arr[i]

print(answer)