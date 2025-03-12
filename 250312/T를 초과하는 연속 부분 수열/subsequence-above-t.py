n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
is_bigger = (arr[0] > t)
if is_bigger:
    answer = 1
else:
    answer = 0

for i in range(1, n):
    if arr[i] > t:
        count += 1
        answer = max(answer, count)
    else:
        count = 1

print(answer)