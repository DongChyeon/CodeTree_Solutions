n = int(input())
answer = 0

combinations = []
numbers = []
def choose_number(depth, n):
    if depth == n:
        combinations.append(''.join(numbers))
        return
    elif depth > n:
        return

    for i in range(1, 5):
        for _ in range(i):
            numbers.append(str(i))
        choose_number(depth + i, n)
        for _ in range(i):
            numbers.pop()

choose_number(0, n)

print(len(combinations))