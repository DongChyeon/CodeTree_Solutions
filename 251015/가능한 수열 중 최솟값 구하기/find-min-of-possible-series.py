n = int(input())
curr = '4'

def is_possible(curr):
    half = len(curr) // 2

    for i in range(1, half + 1):
        if curr[-i:] == curr[-2 * i:-i]:
            return False

    return True

def dfs(curr, depth, last_char):
    if depth == n :
        print(curr)
        exit(0)

    for num in ['4', '5', '6']:
        curr += num
        if is_possible(curr):
            dfs(curr, depth + 1, num)
        curr = curr[:-1]

dfs(curr, 1, '4')