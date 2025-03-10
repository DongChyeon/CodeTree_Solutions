N = int(input())
digits = []

while True:
    if N < 2:
        digits.append(N)
        break

    digits.append(N % 2)
    N //= 2

for digit in digits[::-1]:
    print(digit, end='')
