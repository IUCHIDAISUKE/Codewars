def solve(st, a, b):
    if b >= len(st):
        return st[:a]+st[a:][::-1]
    return st[:a] + st[a: b + 1][::-1] + st[b + 1:]
