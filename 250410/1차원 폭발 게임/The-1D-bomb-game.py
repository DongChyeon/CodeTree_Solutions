n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def get_end_index_of_explosion(start_index, current_number):
    for end_index in range(start_index + 1, len(numbers)):
        if numbers[end_index] != current_number:
            return end_index - 1

    return len(numbers) - 1

while True:
    did_explode = False
    current_index = 0

    while current_index < len(numbers):
        end_index = get_end_index_of_explosion(current_index, numbers[current_index])

        if end_index - current_index + 1 >= m:
            del numbers[current_index:end_index + 1]
            did_explode = True
        else:
            current_index = end_index + 1

    if not did_explode:
        break

print(len(numbers))
for num in numbers:
    print(num)
