import re


def solve(eq):
    tmp = re.split("[*+-/]", eq)
    li = [i for i in eq if i not in tmp and not i.isdigit()]
    res = ""
    for i in zip(tmp[::-1], li[::-1]):
        res += i[0] + i[1]
    res += tmp[::-1][-1]
    return res
