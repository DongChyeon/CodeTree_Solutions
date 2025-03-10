N = input()

def convert_to_decimal(n):
    num = 0

    for i in range(len(n)):
        num += 2 ** i * int(n[-1 - i])

    return num

def convert_to_binary(n):
    number = n
    digits = []

    while True:
        if number < 2:
            digits.append(str(number))
            break
        digits.append(str(number % 2))
        number //= 2

    return ''.join(digits[::-1])
    
print(convert_to_binary(convert_to_decimal(N) * 17))