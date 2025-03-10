a, b = map(int, input().split())
n = input()

def from_base_to_decimal(n, b):
    num = 0

    for i in range(len(n)):
        num += (b ** i * int(n[-1 - i]))

    return num

def from_decimal_to_base(n, b):
    number = n
    digits = []

    while True:
        if number < b:
            digits.append(str(number))
            break
        digits.append(str(number % b))
        number //= b
    
    return ''.join(digits[::-1])

print(from_decimal_to_base(from_base_to_decimal(n, a), b))
