n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def simulate():
    global numbers

    if len(numbers) == 0:
        return False

    count = 1
    last_number = numbers[0]

    is_continue = False
    for i in range(1, len(numbers)):
        if last_number == numbers[i]:
            count += 1
        else:
            if count >= m:
                is_continue = True
                for j in range(i - count, i):
                    numbers[j] = 0

            count = 1
            last_number = numbers[i]
    if count >= m:
        is_continue = True
        for j in range(len(numbers) - count, len(numbers)):
            numbers[j] = 0

    numbers = [num for num in numbers if num != 0]

    return is_continue

while True:
    is_continue = simulate()
    if not is_continue:
        break

print(len(numbers))
for num in numbers:
    print(num)
