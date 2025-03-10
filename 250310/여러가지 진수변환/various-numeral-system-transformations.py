N, B = map(int, input().split())
digits = []

# Please write your code here.
while True:
    if N < B:
        digits.append(N)
        break
    digits.append(N % B)
    N //= B

for digit in digits[::-1]:
    print(digit, end='')