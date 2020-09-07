def solve(s):
    cnt = 0
    for c in s:
        if c.isupper():
            cnt += 1
    return s.upper() if 2 * cnt > len(s) else s.lower()
