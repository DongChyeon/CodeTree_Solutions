equation = input()
operators = [
    equation[i]
    for i in range(len(equation))
    if equation[i] == '+' or equation[i] == '-' or equation[i] == '*'
]
answer = 0

number_combinations = []
numbers = []
def choose_number(depth, n):
    if depth == len(operators) + 1:
        number_combinations.append(numbers[:])
        return

    for i in range(1, n + 1):
        numbers.append(i)
        choose_number(depth + 1, n)
        numbers.pop()
choose_number(0, 4)

for combination in number_combinations:
    val = combination[0]

    for i in range(1, len(combination)):
        operator = operators[i - 1]
        if operator == '+':
            val += combination[i]
        elif operator == '-':
            val -= combination[i]
        elif operator == '*':
            val *= combination[i]
    
    answer = max(answer, val)

print(answer)