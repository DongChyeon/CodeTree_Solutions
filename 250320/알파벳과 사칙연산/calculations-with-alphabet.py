import sys

equation = input()
operands = [
    equation[i]
    for i in range(len(equation))
    if equation[i].islower()
]

answer = -sys.maxsize - 1

number_combinations = []
numbers = []
def choose_number(depth, n):
    if depth == len(operands):
        number_combinations.append(numbers[:])
        return

    for i in range(1, n + 1):
        numbers.append(i)
        choose_number(depth + 1, n)
        numbers.pop()
choose_number(0, 4)

def is_operator(ch):
    return equation[i] == '+' or equation[i] == '-' or equation[i] == '*'

for combination in number_combinations:
    operand_dict = dict(zip(operands, combination))

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

print(answer)