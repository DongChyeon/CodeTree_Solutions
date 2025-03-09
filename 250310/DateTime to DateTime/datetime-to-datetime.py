a, b, c = map(int, input().split())
print(max((a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11), -1))