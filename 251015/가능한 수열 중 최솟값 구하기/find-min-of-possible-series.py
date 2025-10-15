n = int(input())
curr = '4'

def is_possible(curr):
    for length in range(1, len(curr) // 2 + 1):
        for start in range(len(curr) - 1):
            if curr[start:start + length] == curr[start + length:start + 2 * length]:
                return False

    return True

def dfs(curr, depth, last_char):
    if depth == n :
        if is_possible(curr):
            print(curr)
            exit(0)
        return

    for num in ['4', '5', '6']:
        if num != last_char:
            curr += num
            dfs(curr, depth + 1, num)
            curr = curr[:-1]

dfs(curr, 1, '4')