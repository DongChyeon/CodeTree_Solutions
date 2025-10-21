n = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

merged_arr = [0] * n

def merge(arr, low, mid, high):
    i, j = low, mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        merged_arr[k] = arr[j]
        j += 1
        k += 1

    for x in range(low, high + 1):
        arr[x] = merged_arr[x]

merge_sort(arr, 0, n - 1)
print(' '.join(map(str, arr)))