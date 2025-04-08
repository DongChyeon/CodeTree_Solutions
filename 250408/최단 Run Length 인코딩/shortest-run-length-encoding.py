from collections import deque
import sys

A = deque(list(input()))
answer = sys.maxsize

temp = deque(list(A))

for i in range(len(A)):
    if i != 0:
        temp.rotate(1)

    encoding = []
    last_ch = temp[0]
    count = 1
    for j in range(0, len(temp)):
        if temp[j] == last_ch:
            count += 1
        else:
            encoding.append(last_ch)
            encoding.append(count)

            last_ch = temp[j]
            count = 1

    encoding.append(last_ch)
    encoding.append(count)

    answer = min(answer, len(''.join(map(str, encoding))))

print(answer)