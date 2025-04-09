n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove_blocks(start, end):
    global blocks

    for i in range(start - 1, end):
        blocks[i] = 0

    temp = []
    for block in blocks:
        if block != 0:
            temp.append(block)

    blocks = temp

remove_blocks(s1, e1)
remove_blocks(s2, e2)

print(len(blocks))
for block in blocks:
    print(block)
