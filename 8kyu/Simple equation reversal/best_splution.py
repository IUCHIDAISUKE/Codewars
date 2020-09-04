import re


def solve(eq):
    return "".join(re.split("([*+-/])", eq)[::-1])


print(solve("100*b/y"))
