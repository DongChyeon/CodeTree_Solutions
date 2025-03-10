binary = input()
answer = 0

for i in range(len(binary)):
    answer += int(binary[-1 - i]) * (2 ** i)

print(answer)