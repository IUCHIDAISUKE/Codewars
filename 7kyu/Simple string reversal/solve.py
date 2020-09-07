def solve(s):
    ss = list(s)
    rs = [i for i in s[::-1] if i != ' ']
    for num, i in enumerate(ss):
        if i != ' ':
            continue
        rs.insert(num, i)
    return ''.join(rs)
