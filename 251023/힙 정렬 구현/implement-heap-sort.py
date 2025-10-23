n = int(input())
arr = [0] + list(map(int, input().split()))

def heapify(arr, n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[largest] < arr[l]:
        largest = l

    if r <= n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heap_sort(arr, n):
    mid = n // 2
    for i in range(mid, 0, -1):
        heapify(arr, n, i)

    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i - 1, 1)

heap_sort(arr, n)
print(' '.join(map(str, arr[1:])))