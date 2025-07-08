n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

selected = []
pos = [1] * k

def choose(curr_num):
    global answer

    if curr_num == n + 1:
        count = 0
        for p in pos:
            if p >= m:
                count += 1
                
        answer = max(answer, count)
        return

    for i in range(k):
        if pos[i] < m:
            pos[i] += nums[curr_num - 1]
            selected.append(i)
            choose(curr_num + 1)
            pos[i] -= nums[curr_num - 1]
            selected.pop()

choose(1)
print(answer)