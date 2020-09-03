def add(num1, num2):
    res = ""
    while num1 + num2 > 0:
        res = str(num1 % 10 + num2 % 10) + res
        num1 //= 10
        num2 //= 10
    return int(res) if res else 0
