n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dig(x, y, k):
    global answer

    cost = k ** 2 + (k + 1) ** 2
    num_of_gold = sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(x - i) + abs(y - j) <= k
    ])

    if num_of_gold * m >= cost:
        answer = max(answer, num_of_gold)

for y in range(n):
    for x in range(n):
        for k in range(2 * (n - 1) + 1):
            dig(x, y, k)

print(answer)