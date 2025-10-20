n = int(input())
arr = list(input().split())

max_pos = 0
for num in arr:
    if len(num) > max_pos:
        max_pos = len(str(num))

for i in range(len(arr)):
    arr[i] = str(arr[i]).zfill(max_pos)

for pos in range(max_pos - 1, -1, -1):
    arr_new = [[] for _ in range(10)]
    for i in range(len(arr)):
        digit = int(arr[i][pos])
        arr_new[digit].append(arr[i])

    store_arr = []
    for i in range(10):
        for j in range(len(arr_new[i])):
            store_arr.append(arr_new[i][j])

    arr = store_arr

for num in arr:
    print(int(num), end=' ')
