answer = []

def print_answer():
    for x in answer:
        print(x, end=' ')
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(1, k + 1):
        if curr_num > 2:
            if answer[-1] != i or answer[-2] != i:
                answer.append(i)
                choose(curr_num + 1)
                answer.pop()
        else:
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()

k, n = map(int, input().split())
choose(1)
