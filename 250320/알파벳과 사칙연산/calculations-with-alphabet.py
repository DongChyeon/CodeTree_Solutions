import sys

equation = input()
operands = set([
    equation[i]
    for i in range(len(equation))
    if equation[i].islower()
])

answer = -sys.maxsize - 1

def is_operator(ch):
    return ch == '+' or ch == '-' or ch == '*'

def choose_number(depth, numbers, n):
    global answer

    if depth == len(operands):
        operand_dict = dict(zip(operands, numbers[:]))
        val = operand_dict[equation[0]]

        for i in range(1, len(equation)):
            if is_operator(equation[i]):
                operator = equation[i]
                if operator == '+':
                    val += operand_dict[equation[i + 1]]
                    i += 1
                elif operator == '-':
                    val -= operand_dict[equation[i + 1]]
                    i += 1
                elif operator == '*':
                    val *= operand_dict[equation[i + 1]]
                    i += 1
        
        answer = max(answer, val)
        return

    for i in range(1, n + 1):
        numbers.append(i)
        choose_number(depth + 1, numbers, n)
        numbers.pop()

choose_number(0, [], 4)

print(answer)