K, N = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(depth):
    if depth == N:
        print_answer()
        return

    for num in range(1, K + 1):
        answer.append(num)
        choose(depth + 1)
        answer.pop()

choose(0)
        